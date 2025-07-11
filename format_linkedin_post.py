import re
from pathlib import Path

try:
    import pyperclip
except ImportError:
    pyperclip = None

# Mapping A-Z/a-z to their LinkedIn-friendly Unicode bold characters
BOLD_MAP = {chr(i + 65): chr(0x1D400 + i) for i in range(26)}
BOLD_MAP.update({chr(i + 97): chr(0x1D41A + i) for i in range(26)})

# Mapping A-Z/a-z to their LinkedIn-friendly Unicode italic characters
ITALIC_MAP = {chr(i + 65): chr(0x1D434 + i) for i in range(26)}
ITALIC_MAP.update({chr(i + 97): chr(0x1D44E + i) for i in range(26)})


def convert_markdown_to_linkedin_unicode(text: str) -> str:
    """Convert markdown style **bold** and *italic* to LinkedIn Unicode variants."""

    def bold_repl(match: re.Match) -> str:
        return "".join(BOLD_MAP.get(ch, ch) for ch in match.group(1))

    def italic_repl(match: re.Match) -> str:
        return "".join(ITALIC_MAP.get(ch, ch) for ch in match.group(1))

    # Bold first, then italics so nested markers don't conflict
    text = re.sub(r"\*\*(.+?)\*\*", bold_repl, text)
    text = re.sub(r"\*(.+?)\*", italic_repl, text)
    return text


# Paste your LinkedIn post below between the triple quotes
POST_DRAFT = """
Replace this text with your LinkedIn post.
Include **bold** and *italic* markers as needed.
"""


def main() -> None:
    formatted = convert_markdown_to_linkedin_unicode(POST_DRAFT.strip())

    first_paragraph = POST_DRAFT.strip().split("\n\n")[0]
    sanitized = re.sub(r"[^A-Za-z0-9 _-]", "", first_paragraph)[:50].strip()
    filename = "_".join(sanitized.split()) or "linkedin_post"
    Path(f"{filename}.txt").write_text(formatted, encoding="utf-8")

    if pyperclip:
        pyperclip.copy(formatted)
        print(f"Formatted post copied to clipboard and saved to {filename}.txt")
    else:
        print(
            "pyperclip is not installed. File saved as '",
            f"{filename}.txt'. Copy manually."
        )


if __name__ == "__main__":
    main()
