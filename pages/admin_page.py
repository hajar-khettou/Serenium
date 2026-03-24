from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import TimeoutException
from pages.base_page import BasePage
from config import LONG_TIMEOUT


class AdminPage(BasePage):

    ROOMS_LINK = (By.LINK_TEXT, "Rooms")
    REPORT_LINK = (By.LINK_TEXT, "Report")
    BRANDING_LINK = (By.LINK_TEXT, "Branding")
    MESSAGES_LINK = (By.CSS_SELECTOR, "a[href='#/admin/messages']")
    LOGOUT_BUTTON = (By.LINK_TEXT, "Logout")
    ADMIN_PANEL = (By.CSS_SELECTOR, "div.container-fluid")
    FRONT_PAGE_LINK = (By.LINK_TEXT, "Front Page")

    ROOM_NUMBER_INPUT = (By.ID, "roomName")
    ROOM_TYPE_SELECT = (By.ID, "type")
    ROOM_ACCESSIBLE_SELECT = (By.ID, "accessible")
    ROOM_PRICE_INPUT = (By.ID, "roomPrice")
    WIFI_CHECKBOX = (By.ID, "wifiCheckbox")
    TV_CHECKBOX = (By.ID, "tvCheckbox")
    RADIO_CHECKBOX = (By.ID, "radioCheckbox")
    REFRESHMENTS_CHECKBOX = (By.ID, "refreshCheckbox")
    SAFE_CHECKBOX = (By.ID, "safeCheckbox")
    VIEWS_CHECKBOX = (By.ID, "viewsCheckbox")
    CREATE_ROOM_BUTTON = (By.ID, "createRoom")

    ROOM_ROWS = (By.CSS_SELECTOR, "div[data-testid='roomlisting']")
    ROOM_DELETE_BUTTON = (By.CSS_SELECTOR, "span.roomDelete")
    ROOM_EDIT_BUTTON = (By.CSS_SELECTOR, "button.btn.btn-outline-primary")

    MESSAGE_ROWS = (By.CSS_SELECTOR, "div.messages div.row")
    MESSAGE_DELETE_BUTTON = (By.CSS_SELECTOR, "span.fa-trash")

    ERROR_MESSAGE = (By.CSS_SELECTOR, "div.alert.alert-danger")

    def is_admin_loaded(self) -> bool:
        return self.is_element_visible(self.ROOM_NUMBER_INPUT, timeout=LONG_TIMEOUT)

    def click_rooms(self):
        self.click(self.ROOMS_LINK)

    def click_messages(self):
        self.click(self.MESSAGES_LINK)

    def click_branding(self):
        self.click(self.BRANDING_LINK)

    def logout(self):
        self.click(self.LOGOUT_BUTTON)

    def create_room(self, room_number: str, room_type: str, accessible: str, price: str,
                    amenities: list = None):
        self.type_text(self.ROOM_NUMBER_INPUT, room_number)

        type_select = Select(self.wait_for_element_visible(self.ROOM_TYPE_SELECT))
        type_select.select_by_visible_text(room_type)

        accessible_select = Select(self.wait_for_element_visible(self.ROOM_ACCESSIBLE_SELECT))
        accessible_select.select_by_visible_text(accessible)

        self.type_text(self.ROOM_PRICE_INPUT, price)

        if amenities:
            amenity_map = {
                "wifi": self.WIFI_CHECKBOX,
                "tv": self.TV_CHECKBOX,
                "radio": self.RADIO_CHECKBOX,
                "refreshments": self.REFRESHMENTS_CHECKBOX,
                "safe": self.SAFE_CHECKBOX,
                "views": self.VIEWS_CHECKBOX,
            }
            for amenity in amenities:
                locator = amenity_map.get(amenity.lower())
                if locator:
                    self.click(locator)

        self.click(self.CREATE_ROOM_BUTTON)

    def get_room_count(self) -> int:
        try:
            rooms = self.wait_for_elements_visible(self.ROOM_ROWS)
            return len(rooms)
        except TimeoutException:
            return 0

    def room_exists(self, room_number: str) -> bool:
        try:
            rows = self.wait_for_elements_visible(self.ROOM_ROWS)
            return any(room_number in row.text for row in rows)
        except TimeoutException:
            return False

    def delete_last_room(self):
        try:
            delete_buttons = self.wait_for_elements_visible(self.ROOM_DELETE_BUTTON)
            if delete_buttons:
                delete_buttons[-1].click()
        except TimeoutException:
            pass

    def get_message_count(self) -> int:
        messages = self.wait_for_elements_visible(self.MESSAGE_ROWS)
        return len(messages)

    def is_error_displayed(self) -> bool:
        return self.is_element_visible(self.ERROR_MESSAGE, timeout=5)

    def is_logout_successful(self) -> bool:
        from pages.login_page import LoginPage
        login = LoginPage(self.driver)
        return login.is_element_visible(LoginPage.USERNAME_INPUT, timeout=LONG_TIMEOUT)
