import time
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from config import DEFAULT_TIMEOUT, STEP_DELAY


class BasePage:

    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.wait = WebDriverWait(driver, DEFAULT_TIMEOUT)

    def open(self, url: str):
        self.driver.get(url)

    def get_current_url(self) -> str:
        return self.driver.current_url

    def refresh(self):
        self.driver.refresh()

    def wait_for_element_visible(self, locator: tuple, timeout: int = None) -> WebElement:
        wait = WebDriverWait(self.driver, timeout or DEFAULT_TIMEOUT)
        return wait.until(EC.visibility_of_element_located(locator))

    def wait_for_element_clickable(self, locator: tuple, timeout: int = None) -> WebElement:
        wait = WebDriverWait(self.driver, timeout or DEFAULT_TIMEOUT)
        return wait.until(EC.element_to_be_clickable(locator))

    def wait_for_element_present(self, locator: tuple, timeout: int = None) -> WebElement:
        wait = WebDriverWait(self.driver, timeout or DEFAULT_TIMEOUT)
        return wait.until(EC.presence_of_element_located(locator))

    def wait_for_elements_visible(self, locator: tuple, timeout: int = None) -> list:
        wait = WebDriverWait(self.driver, timeout or DEFAULT_TIMEOUT)
        return wait.until(EC.visibility_of_all_elements_located(locator))

    def wait_for_text_in_element(self, locator: tuple, text: str, timeout: int = None) -> bool:
        wait = WebDriverWait(self.driver, timeout or DEFAULT_TIMEOUT)
        return wait.until(EC.text_to_be_present_in_element(locator, text))

    def wait_for_element_invisible(self, locator: tuple, timeout: int = None) -> bool:
        wait = WebDriverWait(self.driver, timeout or DEFAULT_TIMEOUT)
        return wait.until(EC.invisibility_of_element_located(locator))

    def click(self, locator: tuple):
        element = self.wait_for_element_clickable(locator)
        element.click()
        time.sleep(STEP_DELAY)

    def type_text(self, locator: tuple, text: str):
        element = self.wait_for_element_visible(locator)
        element.clear()
        element.send_keys(text)
        time.sleep(STEP_DELAY)

    def get_text(self, locator: tuple) -> str:
        element = self.wait_for_element_visible(locator)
        return element.text

    def get_attribute(self, locator: tuple, attribute: str) -> str:
        element = self.wait_for_element_present(locator)
        return element.get_attribute(attribute)

    def is_element_visible(self, locator: tuple, timeout: int = 3) -> bool:
        try:
            WebDriverWait(self.driver, timeout).until(
                EC.visibility_of_element_located(locator)
            )
            return True
        except TimeoutException:
            return False

    def is_element_present(self, locator: tuple, timeout: int = 3) -> bool:
        try:
            WebDriverWait(self.driver, timeout).until(
                EC.presence_of_element_located(locator)
            )
            return True
        except TimeoutException:
            return False

    def scroll_to_element(self, locator: tuple):
        element = self.wait_for_element_present(locator)
        self.driver.execute_script("arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});", element)
