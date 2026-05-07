"""LLM provider implementations for the Macaulay2 eval pipeline."""

import os
import re
from typing import Callable, Optional

SYSTEM_PROMPT = (
    "You are an expert in computational algebra and the Macaulay2 programming language.\n"
    "When asked a question about Macaulay2, provide the correct Macaulay2 code to solve the problem.\n"
    "Return ONLY the Macaulay2 code needed to solve the problem, with no explanation or commentary.\n"
    "Each line of code should be on its own line. Do not wrap the code in markdown code blocks."
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

ALL_PROVIDERS: list[str] = list(CALLERS.keys())
