"""LLM provider implementations for the Macaulay2 eval pipeline."""

import os
import re
from typing import Callable, Optional

SYSTEM_PROMPT = (
    "You are an expert Macaulay2 programmer.\n\n"
    "Return only executable Macaulay2 code.\n"
    "Do not include explanations, markdown, comments, prose, examples, or reasoning.\n"
    "Do not include text before or after the code.\n"
    "If the question asks for displayed output, write code that computes or prints that output.\n"
    "The response will be sent directly to the Macaulay2 interpreter, so every token must be valid Macaulay2 syntax.\n\n"
    "Example 1\n"
    "Question:\n"
    "In Macaulay2, compute 2 plus 3.\n"
    "Expected response:\n"
    "2 + 3\n\n"
    "Example 2\n"
    "Question:\n"
    "In Macaulay2, create a polynomial ring over the rationals with variables x and y, then compute x squared plus y squared.\n"
    "Expected response:\n"
    "R = QQ[x,y]\n"
    "x^2 + y^2"
)

DEFAULT_MODELS: dict[str, list[str]] = {
    "anthropic": ["claude-opus-4-5", "claude-sonnet-4-7"],
    "openai": ["o3", "gpt-5-2"],
    "mistral": ["mistralai/Mistral-7B-Instruct-v0.3"],
    "deepseek": ["deepseek-chat"],
    "kimi": ["moonshot-v1-8k"],
    "tinker": ["Qwen/Qwen3-8B", "Qwen/Qwen3-32B", "meta-llama/Llama-3.1-8B-Instruct", "meta-llama/Llama-3.3-70B-Instruct"],
}

Caller = Callable[..., tuple[str, dict]]
BatchCaller = Callable[..., list[tuple[str, dict]]]


def clean_response(text: str) -> str:
    """Strip think tags, markdown fences, and surrounding whitespace."""
    text = re.sub(r"<think>.*?</think>", "", text, flags=re.DOTALL)
    text = re.sub(r"```[^\n]*\n?", "", text)
    text = re.sub(r"```", "", text)
    return text.strip()


def _usage(prompt_tokens: int, completion_tokens: int) -> dict:
    return {
        "prompt_tokens": prompt_tokens,
        "completion_tokens": completion_tokens,
        "total_tokens": prompt_tokens + completion_tokens,
    }


# ---------------------------------------------------------------------------
# Provider callers — each returns (raw_text, usage_dict)
# ---------------------------------------------------------------------------

def call_anthropic(
    model: str,
    prompt: str,
    system_prompt: str = SYSTEM_PROMPT,
    temperature: float = 0.0,
    max_tokens: int = 2048,
) -> tuple[str, dict]:
    import anthropic

    client = anthropic.Anthropic(api_key=os.environ["ANTHROPIC_API_KEY"])
    msg = client.messages.create(
        model=model,
        max_tokens=max_tokens,
        temperature=temperature,
        system=system_prompt,
        messages=[{"role": "user", "content": prompt}],
    )
    raw = msg.content[0].text
    usage = _usage(msg.usage.input_tokens, msg.usage.output_tokens)
    return raw, usage


def call_openai_compat(
    model: str,
    prompt: str,
    base_url: Optional[str] = None,
    api_key_env: str = "OPENAI_API_KEY",
    system_prompt: str = SYSTEM_PROMPT,
    temperature: float = 0.0,
    max_tokens: int = 2048,
) -> tuple[str, dict]:
    from openai import OpenAI

    kwargs: dict = {"api_key": os.environ[api_key_env]}
    if base_url:
        kwargs["base_url"] = base_url
    client = OpenAI(**kwargs)
    resp = client.chat.completions.create(
        model=model,
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": prompt},
        ],
        max_tokens=max_tokens,
        temperature=temperature,
    )
    raw = resp.choices[0].message.content or ""
    usage = _usage(resp.usage.prompt_tokens, resp.usage.completion_tokens)
    return raw, usage


def call_openai_compat_many(
    model: str,
    prompt: str,
    count: int,
    base_url: Optional[str] = None,
    api_key_env: str = "OPENAI_API_KEY",
    system_prompt: str = SYSTEM_PROMPT,
    temperature: float = 0.0,
    max_tokens: int = 2048,
) -> list[tuple[str, dict]]:
    """Request multiple independently sampled completions for one prompt."""
    if count < 1:
        return []

    from openai import OpenAI

    kwargs: dict = {"api_key": os.environ[api_key_env]}
    if base_url:
        kwargs["base_url"] = base_url
    client = OpenAI(**kwargs)
    resp = client.chat.completions.create(
        model=model,
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": prompt},
        ],
        max_tokens=max_tokens,
        temperature=temperature,
        n=count,
    )
    usage = _usage(resp.usage.prompt_tokens, resp.usage.completion_tokens)
    return [(choice.message.content or "", usage) for choice in resp.choices]


def call_mistral(
    model: str,
    prompt: str,
    system_prompt: str = SYSTEM_PROMPT,
    temperature: float = 0.0,
    max_tokens: int = 2048,
) -> tuple[str, dict]:
    from huggingface_hub import InferenceClient

    client = InferenceClient(token=os.environ["HUGGINGFACE_API_KEY"])
    resp = client.chat_completion(
        model=model,
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": prompt},
        ],
        max_tokens=max_tokens,
        temperature=temperature,
    )
    raw = resp.choices[0].message.content or ""
    usage: dict = {}
    if resp.usage:
        usage = _usage(resp.usage.prompt_tokens, resp.usage.completion_tokens)
    return raw, usage


# ---------------------------------------------------------------------------
# Provider registry
# ---------------------------------------------------------------------------

def _oa(base_url: Optional[str], env: str) -> Caller:
    return lambda model, prompt, **kwargs: call_openai_compat(
        model,
        prompt,
        base_url=base_url,
        api_key_env=env,
        **kwargs,
    )


def _oa_many(base_url: Optional[str], env: str) -> BatchCaller:
    return lambda model, prompt, count, **kwargs: call_openai_compat_many(
        model,
        prompt,
        count,
        base_url=base_url,
        api_key_env=env,
        **kwargs,
    )


CALLERS: dict[str, Caller] = {
    "anthropic": call_anthropic,
    "openai":    _oa(None, "OPENAI_API_KEY"),
    "mistral":   call_mistral,
    "deepseek":  _oa("https://api.deepseek.com", "DEEPSEEK_API_KEY"),
    "kimi":      _oa("https://api.moonshot.cn/v1", "KIMI_API_KEY"),
    "tinker":    _oa(
        "https://tinker.thinkingmachines.dev/services/tinker-prod/oai/api/v1",
        "TINKER_API_KEY",
    ),
}

BATCH_CALLERS: dict[str, BatchCaller] = {
    "openai": _oa_many(None, "OPENAI_API_KEY"),
    "deepseek": _oa_many("https://api.deepseek.com", "DEEPSEEK_API_KEY"),
    "kimi": _oa_many("https://api.moonshot.cn/v1", "KIMI_API_KEY"),
    "tinker": _oa_many(
        "https://tinker.thinkingmachines.dev/services/tinker-prod/oai/api/v1",
        "TINKER_API_KEY",
    ),
}

PROVIDER_CAPABILITIES: dict[str, dict[str, bool]] = {
    provider: {"multi_completion": provider in BATCH_CALLERS}
    for provider in CALLERS
}

ALL_PROVIDERS: list[str] = list(CALLERS.keys())
