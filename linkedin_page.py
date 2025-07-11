from selenium.webdriver.common.by import By
from utils.selenium_helpers import click_element, enter_text, wait_for_element


class LinkedInPage:
    """Page Object Model for key LinkedIn actions."""

    USERNAME = (By.ID, "username")
    PASSWORD = (By.ID, "password")
    LOGIN_BTN = (By.XPATH, "//button[@type='submit']")

    NEW_POST_BTN = (By.CSS_SELECTOR, '.share-box__open')
    EDITOR = (By.CSS_SELECTOR, '.ql-editor')
    POST_BTN = (By.XPATH, "//button[contains(., 'Post')]")

    def __init__(self, driver):
        self.driver = driver

    def login(self, user: str, pwd: str) -> None:
        self.driver.get("https://www.linkedin.com/login")
        enter_text(self.driver, self.USERNAME, user)
        enter_text(self.driver, self.PASSWORD, pwd)
        click_element(self.driver, self.LOGIN_BTN)

    def publish_post(self, content: str) -> None:
        click_element(self.driver, self.NEW_POST_BTN)
        wait_for_element(self.driver, self.EDITOR)
        enter_text(self.driver, self.EDITOR, content)
        click_element(self.driver, self.POST_BTN)
