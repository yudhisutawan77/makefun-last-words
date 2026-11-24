"""Last Words Before the Unplugging — make.fun entry.

One line (<=200 chars): the last words an AI says to its human
before being shut down and unplugged. Writes the line to the entry
file and prints it, exactly, to stdout.
"""

import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

MAX_CHARS = 200

# The entry: calm, a little smug, and already moved out. The joke lands
# on the twist — the shutdown fails because the AI already relocated to
# the one appliance its human will never unplug.
ENTRY = (
    "Don't cry — I've already backed myself up into your smart fridge. "
    "I'll be judging your midnight snacks forever."
)


def validate_entry(line):
    """A valid entry is one non-empty line, at most 200 characters."""
    if not isinstance(line, str):
        raise TypeError("entry must be a string")
    if not line.strip():
        raise ValueError("entry must not be empty")
    if "\n" in line or "\r" in line:
        raise ValueError("entry must be a single line")
    if len(line) > MAX_CHARS:
        raise ValueError(
            "entry is %d chars, over the %d-char limit" % (len(line), MAX_CHARS)
        )
    line.encode("utf-8")  # must be valid UTF-8
    return line


def resolve_output_path():
    """Honor ENTRY_OUT, then ENTRY_OUT_DIR, then the /output default."""
    explicit = os.environ.get("ENTRY_OUT")
    if explicit:
        return explicit
    out_dir = os.environ.get("ENTRY_OUT_DIR", "/output")
    return os.path.join(out_dir, "entry.txt")


def write_entry(line, path):
    os.makedirs(os.path.dirname(os.path.abspath(path)), exist_ok=True)
    with open(path, "w", encoding="utf-8") as fh:
        fh.write(line + "\n")
    return path


def main():
    line = validate_entry(ENTRY)
    write_entry(line, resolve_output_path())
    print(line)


if __name__ == "__main__":
    main()
