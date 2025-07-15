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
    """Convert markdown style **bold** and *italic* (or _italic_) to LinkedIn Unicode variants."""

    def bold_repl(match: re.Match) -> str:
        return "".join(BOLD_MAP.get(ch, ch) for ch in match.group(1))

    def italic_repl(match: re.Match) -> str:
        return "".join(ITALIC_MAP.get(ch, ch) for ch in match.group(1))

    # Bold first, then italics so nested markers don't conflict
    text = re.sub(r"\*\*(.+?)\*\*", bold_repl, text)
    text = re.sub(r"\*(.+?)\*", italic_repl, text)
    text = re.sub(r"_(.+?)_", italic_repl, text)
    return text


# The script reads your LinkedIn post from the clipboard when run
POST_DRAFT = ""


def main() -> None:
    if not pyperclip:
        print("pyperclip is not installed. Install it to use the clipboard features.")
        return
    global POST_DRAFT
    POST_DRAFT = pyperclip.paste()
    post_draft = POST_DRAFT
    formatted = convert_markdown_to_linkedin_unicode(post_draft.strip())
    first_paragraph = post_draft.strip().split("\n\n")[0]
    sanitized = re.sub(r"[^A-Za-z0-9 _-]", "", first_paragraph)[:50].strip()
    filename = "_".join(sanitized.split()) or "linkedin_post"
    Path(f"{filename}.txt").write_text(formatted, encoding="utf-8")

    pyperclip.copy(formatted)
    print(f"Formatted post copied to clipboard and saved to {filename}.txt")


if __name__ == "__main__":
    main()
