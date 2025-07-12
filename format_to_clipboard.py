import subprocess
from pathlib import Path
from linkedin_formatter import convert_markdown_to_linkedin_unicode

POST_DRAFT = """Hey everyone,
I’m excited about **our new launch** next week—*stay tuned*!"""


def save_to_clipboard(text: str) -> None:
    try:
        p = subprocess.run(['pbcopy'], input=text.encode('utf-8'), check=True)
    except FileNotFoundError:
        print('pbcopy not found. This script must be run on macOS to copy to clipboard.')


def sanitize_filename(title: str) -> str:
    sanitized = ''.join(ch if ch.isalnum() or ch == ' ' else '' for ch in title)
    sanitized = '_'.join(sanitized.strip().split())
    return sanitized[:50] if len(sanitized) > 50 else sanitized


def main() -> None:
    formatted = convert_markdown_to_linkedin_unicode(POST_DRAFT)
    save_to_clipboard(formatted)

    first_paragraph = POST_DRAFT.split("\n\n", 1)[0]
    filename = sanitize_filename(first_paragraph) or 'post'
    Path(f"{filename}.txt").write_text(formatted, encoding='utf-8')


if __name__ == '__main__':
    main()
