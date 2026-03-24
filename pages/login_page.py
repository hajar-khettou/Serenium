from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from config import ADMIN_URL, LONG_TIMEOUT


class LoginPage(BasePage):

    USERNAME_INPUT = (By.ID, "username")
    PASSWORD_INPUT = (By.ID, "password")
    LOGIN_BUTTON = (By.ID, "doLogin")
    LOGIN_ERROR = (By.CSS_SELECTOR, "div.alert.alert-danger")

    def open_admin_login(self):
        self.open(ADMIN_URL)

    def login(self, username: str, password: str):
        self.type_text(self.USERNAME_INPUT, username)
        self.type_text(self.PASSWORD_INPUT, password)
        self.click(self.LOGIN_BUTTON)

    def is_login_error_displayed(self) -> bool:
        return self.is_element_visible(self.LOGIN_ERROR, timeout=5)
