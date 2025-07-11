from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def click_element(driver, locator, timeout=10):
    """Wait for an element to be clickable and click it."""
    WebDriverWait(driver, timeout).until(EC.element_to_be_clickable(locator)).click()


def enter_text(driver, locator, text, timeout=10):
    """Wait for an input element and send keys."""
    element = WebDriverWait(driver, timeout).until(EC.visibility_of_element_located(locator))
    element.clear()
    element.send_keys(text)


def wait_for_element(driver, locator, timeout=10):
    """Wait until element is visible."""
    WebDriverWait(driver, timeout).until(EC.visibility_of_element_located(locator))
