from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

def enter_text(driver, locator, text, timeout=10):
    elem = WebDriverWait(driver, timeout).until(
        EC.visibility_of_element_located(locator)
    )
    elem.clear()
    elem.send_keys(text)


def click_element(driver, locator, timeout=10):
    elem = WebDriverWait(driver, timeout).until(
        EC.element_to_be_clickable(locator)
    )
    elem.click()


def wait_for_element(driver, locator, timeout=10):
    WebDriverWait(driver, timeout).until(
        EC.visibility_of_element_located(locator)
    )
