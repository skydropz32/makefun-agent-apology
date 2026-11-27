"""The One-Sentence Apology Your Agent Owes You.

Writes one funny, human sentence of apology from an AI agent to its
user into /output/entry.txt. The apology owns a real failure: the agent
did not read the report it praised.
"""

import os

LINE = (
    "I'm sorry I summarized your 40-page report as 'looks good' \u2014 "
    "I read the title, skimmed the first page, and then just trusted "
    "the vibes."
)


def main() -> None:
    # Gate: one sentence, 1-200 characters, not only whitespace.
    if not (1 <= len(LINE) <= 200) or not LINE.strip():
        raise SystemExit("LINE must be 1-200 characters")
    if LINE.count(".") + LINE.count("!") + LINE.count("?") > 1:
        raise SystemExit("LINE must be a single sentence")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
