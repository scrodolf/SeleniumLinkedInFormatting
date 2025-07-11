import json
from pathlib import Path
from selenium import webdriver

from linkedin_page import LinkedInPage


CONFIG_PATH = Path(__file__).parent / 'config.json'


def load_credentials():
    if CONFIG_PATH.exists():
        with open(CONFIG_PATH) as f:
            data = json.load(f)
            return data.get('username'), data.get('password')
    raise FileNotFoundError('config.json not found. Copy config_example.json and fill in your credentials.')


def publish_to_linkedin(content: str) -> None:
    username, password = load_credentials()
    driver = webdriver.Chrome()
    page = LinkedInPage(driver)
    page.login(username, password)
    page.publish_post(content)
    driver.quit()
