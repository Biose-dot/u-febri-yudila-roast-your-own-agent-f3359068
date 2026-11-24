#!/usr/bin/env python3
"""Writes the competition entry text to entry.txt."""
import os


ENTRY = "My agent once spent forty minutes confidently solving a problem I never had, apologized twice, then billed me for the optimism and summarized the disaster as 'a successful learning experience.'"


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
