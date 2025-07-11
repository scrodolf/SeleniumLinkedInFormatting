from selenium import webdriver
from time import sleep
from typing import Optional

from linkedin_page import LinkedInPage


def publish_to_linkedin(content: str, username: str, password: str,
                        driver: Optional[webdriver.Chrome] = None) -> None:
    """Open a browser, log in and publish ``content`` to LinkedIn."""
    owns_driver = driver is None
    if owns_driver:
        driver = webdriver.Chrome()

    page = LinkedInPage(driver)
    page.login(username, password)
    page.publish_post(content)
    sleep(5)  # let LinkedIn process it

    if owns_driver:
        driver.quit()
