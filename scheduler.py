import os
import schedule
import time

from conversion import convert_markdown_to_linkedin_unicode
from publish import publish_to_linkedin

POST_DRAFT = """Hey everyone,
I’m excited about **our new launch** next week—*stay tuned*!"""

def job():
    formatted = convert_markdown_to_linkedin_unicode(POST_DRAFT)
    user = os.getenv("LINKEDIN_USER")
    pwd = os.getenv("LINKEDIN_PASS")
    if not user or not pwd:
        raise RuntimeError("Please set LINKEDIN_USER and LINKEDIN_PASS")
    publish_to_linkedin(formatted, user, pwd)

# Schedule once, one hour from now
schedule.every(1).hours.do(job)

# Keep the script alive
while True:
    schedule.run_pending()
    time.sleep(1)
