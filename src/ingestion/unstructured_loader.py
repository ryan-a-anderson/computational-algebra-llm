from pathlib import Path

import json
from unstructured.partition.auto import partition
from unstructured.partition.text import partition_text


PROJECT_ROOT = Path(__file__).resolve().parents[2]
INPUT_DIR = PROJECT_ROOT / "data" / "raw"
OUTPUT_DIR = PROJECT_ROOT / "data" / "processed" / "unstructured_output"


def _elements_to_text(elements) -> str:
    chunks = [str(element).strip() for element in elements if str(element).strip()]
    return "\n\n".join(chunks).strip() + "\n"


def load_with_unstructured(input_dir: Path = INPUT_DIR, output_dir: Path = OUTPUT_DIR) -> None:
    input_dir = Path(input_dir)
    output_dir = Path(output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)

    files = sorted([p for p in input_dir.rglob("*") if p.is_file()])
    if not files:
        print(f"No files found in {input_dir}.")
        return

    for file_path in files:
        print(f"Processing: {file_path}")

        try:
            if file_path.suffix.lower() == ".json":
                with file_path.open("r", encoding="utf-8") as f:
                    obj = json.load(f)
                elements = partition_text(text=json.dumps(obj, ensure_ascii=False, indent=2))
            else:
                elements = partition(filename=str(file_path), strategy="fast")  # fast means no OCR

            output_content = _elements_to_text(elements)

            if not output_content.strip():
                print(f"Skipping {file_path.name}: no extractable text without OCR")
                continue

        except Exception as exc:
            print(f"Skipping {file_path.name}: could not parse without OCR ({exc})")
            continue

        rel_path = file_path.relative_to(input_dir).with_suffix(".txt")
        output_path = output_dir / rel_path
        output_path.parent.mkdir(parents=True, exist_ok=True)

        with output_path.open("w", encoding="utf-8") as f:
            f.write(output_content)

        print(f"Saved: {output_path}")


if __name__ == "__main__":
    load_with_unstructured()