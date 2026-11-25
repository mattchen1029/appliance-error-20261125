"""Washing-machine error line for make.fun's "The Funniest Honest Appliance Error".

The machine reports the fault in its own flat voice: the drain is blocked
by the very sock the owner insists the dryer ate. It has been sitting in
the filter since March.
"""

from pathlib import Path
import os

# The entry: one line, at most 200 characters, plain text.
APPLIANCE_ERROR = (
    "ERROR E17: Drain blocked by one sock. "
    "It is the one you swore the dryer ate. "
    "It has been in my filter since March."
)

# Competition gates for the entry text.
LOWER_BOUND = 1
UPPER_BOUND = 200
TARGET_FILE = "entry.txt"


def is_single_line(text):
    """True when the text has no line breaks at all."""
    return "\n" not in text and "\r" not in text


def check_entry(text):
    """Raise if the entry breaks any of the competition's gates."""
    length = len(text)
    if length < LOWER_BOUND or length > UPPER_BOUND:
        raise ValueError(
            "entry must be %d-%d characters long, got %d"
            % (LOWER_BOUND, UPPER_BOUND, length)
        )
    if not is_single_line(text):
        raise ValueError("entry must fit on one line")
    if text.strip() == "":
        raise ValueError("entry must not be blank")


def emit(text, directory):
    """Validate the entry, then write it to <directory>/entry.txt."""
    check_entry(text)
    destination = Path(directory)
    destination.mkdir(parents=True, exist_ok=True)
    (destination / TARGET_FILE).write_text(text, encoding="utf-8")


def run():
    out = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    emit(APPLIANCE_ERROR, out)


if __name__ == "__main__":
    run()
