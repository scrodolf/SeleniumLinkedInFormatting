import re

BOLD_MAP = {
    **{chr(i): chr(0x1D400 + i - 65) for i in range(65, 91)},
    **{chr(i): chr(0x1D41A + i - 97) for i in range(97, 123)},
}

ITALIC_MAP = {
    **{chr(i): chr(0x1D434 + i - 65) for i in range(65, 91)},
    **{chr(i): chr(0x1D44E + i - 97) for i in range(97, 123)},
}

def convert_markdown_to_linkedin_unicode(text: str) -> str:
    def bold_repl(match: re.Match) -> str:
        return ''.join(BOLD_MAP.get(ch, ch) for ch in match.group(1))

    def italic_repl(match: re.Match) -> str:
        return ''.join(ITALIC_MAP.get(ch, ch) for ch in match.group(1))

    text = re.sub(r"\*\*(.+?)\*\*", bold_repl, text)
    text = re.sub(r"\*(.+?)\*", italic_repl, text)
    return text
