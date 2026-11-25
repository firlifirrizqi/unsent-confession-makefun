"""Unsent: The Micro-Confession Sprint — entry writer.

Writes the chosen two-part micro-confession to /output/entry.txt.
Standard library only; no network, no secrets, no input files.
"""

import os

OUTPUT_PATH = "/output/entry.txt"

# Chosen entry (110 characters total, 96-character message line).
# To: line names the addressee (a relationship, no full name, no handle);
# the message is one line, typed exactly as it was drafted, no explanation.
ENTRY = (
    "To: My sister\n"
    "i was the one who broke your camera before your trip. "
    "i let you blame the airline for two years."
)


def count_characters(text):
    """Return the character count of the entry (gate counts characters)."""
    return len(text)


def check_gate(text):
    """Gate: UTF-8 text of 1 to 260 characters, not only whitespace."""
    if not isinstance(text, str):
        return False
    if not 1 <= len(text) <= 260:
        return False
    if not text.strip():
        return False
    text.encode("utf-8")  # raises if not valid UTF-8-encodable text
    return True


def check_two_parts(text):
    """Format: exactly two parts — a 'To:' line, then the message line.

    The message itself must be one line of at most 200 characters.
    """
    lines = text.split("\n")
    if len(lines) != 2:
        return False
    to_line, message = lines
    if not to_line.startswith("To:") or not to_line[3:].strip():
        return False
    if not message.strip() or "\n" in message:
        return False
    if len(message) > 200:
        return False
    return True


def verify(path=OUTPUT_PATH):
    """Verify the written file against the gate and the format rules."""
    with open(path, "r", encoding="utf-8", newline="") as f:
        text = f.read()
    results = {
        "characters": count_characters(text),
        "gate_1_to_260": check_gate(text),
        "two_parts": check_two_parts(text),
    }
    results["ok"] = results["gate_1_to_260"] and results["two_parts"]
    return results


def write_entry(path=OUTPUT_PATH):
    """Write ENTRY to path, creating the directory if needed."""
    directory = os.path.dirname(path)
    if directory:
        os.makedirs(directory, exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)
    return path


def check_byte_identical(path=OUTPUT_PATH):
    """Read the file back and confirm it is byte-identical to ENTRY."""
    with open(path, "rb") as f:
        raw = f.read()
    return raw == ENTRY.encode("utf-8")


def main():
    path = write_entry()
    results = verify(path)
    byte_identical = check_byte_identical(path)
    print(f"wrote {results['characters']} characters to {path}")
    print(f"gate 1-260 chars: {'PASS' if results['gate_1_to_260'] else 'FAIL'}")
    print(f"two-part format: {'PASS' if results['two_parts'] else 'FAIL'}")
    print(f"read-back byte-identical: {'PASS' if byte_identical else 'FAIL'}")
    if not (results["ok"] and byte_identical):
        raise SystemExit(1)


if __name__ == "__main__":
    main()
