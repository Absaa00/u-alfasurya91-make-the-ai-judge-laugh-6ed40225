"""Make the AI Judge Laugh — one-line office-life joke.

Deterministic, offline, no network, no randomness, no clock.
Writes the single joke line to /output/entry.txt and prints it.
"""

import os

JOKE = (
    "My boss says my job is AI-proof because robots can't survive "
    "meetings, so now I prove him right eight hours a day across "
    "four time zones."
)

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    # Competition rule: a single line, strictly under 200 characters.
    assert len(JOKE) < 200, "joke must stay under 200 characters"
    assert "\n" not in JOKE, "joke must be exactly one line"
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as handle:
        handle.write(JOKE + "\n")
    print(JOKE)


if __name__ == "__main__":
    main()
