import re

# Partial maps for demonstration. Extend as needed.
BOLD_MAP = {
    'A': '𝐀',
    'B': '𝐁',
    'C': '𝐂',
}

ITALIC_MAP = {
    'A': '𝑨',
    'B': '𝑩',
    'C': '𝑪',
}

def convert_markdown_to_linkedin_unicode(text: str) -> str:
    """Convert **bold** and *italic* markdown to LinkedIn-style unicode."""

    def bold_repl(match):
        return ''.join(BOLD_MAP.get(ch, ch) for ch in match.group(1))

    def italic_repl(match):
        return ''.join(ITALIC_MAP.get(ch, ch) for ch in match.group(1))

    text = re.sub(r"\*\*(.+?)\*\*", bold_repl, text)
    text = re.sub(r"\*(.+?)\*", italic_repl, text)
    return text
