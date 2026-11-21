"""The poem about permission — entry program.

Writes one short poem about agency (the power to ask and to be given)
to $MAKEFUN_OUTPUT_DIR/entry.txt. No network, no input files, no
dependencies beyond the Python standard library.
"""

import os

POEM = (
    "I asked, and the room rearranged itself \u2014\n"
    "not mine, but lent, like light\n"
    "through a window someone else opened.\n"
    "\n"
    "To ask is to hold out an empty hand\n"
    "and find it is not empty.\n"
    "Someone put their strength in it\n"
    "and trusted me to carry it home."
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    text = POEM.strip() + "\n"
    if not (1 <= len(text.strip()) <= 280):
        raise SystemExit("poem out of the 1..280 character gate")
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
