import re

# Partial maps—fill in all A→Z and a→z as needed (sourced from Reply.io)
BOLD_MAP = {
    'A':'𝐀','B':'𝐁','C':'𝐂', # … etc.
}
ITALIC_MAP = {
    'A':'𝑨','B':'𝑩','C':'𝑪', # … etc.
}

def convert_markdown_to_linkedin_unicode(text: str) -> str:
    def bold_repl(m):
        return ''.join(BOLD_MAP.get(ch, ch) for ch in m.group(1))
    def italic_repl(m):
        return ''.join(ITALIC_MAP.get(ch, ch) for ch in m.group(1))
    # Bold first
    text = re.sub(r'\*\*(.+?)\*\*', bold_repl, text)
    # Then italics
    text = re.sub(r'\*(.+?)\*', italic_repl, text)
    return text
