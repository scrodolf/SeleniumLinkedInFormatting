from formatter import convert_markdown_to_linkedin_unicode
from publisher import publish_to_linkedin


def main():
    print("Paste your LinkedIn post and finish with an empty line:")
    lines = []
    while True:
        line = input()
        if not line:
            break
        lines.append(line)
    content = "\n".join(lines)
    formatted = convert_markdown_to_linkedin_unicode(content)
    publish_to_linkedin(formatted)


if __name__ == "__main__":
    main()
