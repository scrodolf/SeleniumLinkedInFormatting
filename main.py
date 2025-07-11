import os

from conversion import convert_markdown_to_linkedin_unicode
from publish import publish_to_linkedin


if __name__ == "__main__":
    user = os.getenv("LINKEDIN_USER")
    pwd = os.getenv("LINKEDIN_PASS")
    if not user or not pwd:
        raise RuntimeError("Please set LINKEDIN_USER and LINKEDIN_PASS")

    post = input("Paste the text you want to post on LinkedIn:\n")
    formatted = convert_markdown_to_linkedin_unicode(post)
    publish_to_linkedin(formatted, user, pwd)
