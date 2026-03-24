from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from pages.base_page import BasePage
from config import BASE_URL, LONG_TIMEOUT


class HomePage(BasePage):

    ROOM_CARDS = (By.CSS_SELECTOR, "div.hotel-room-info")
    BOOK_BUTTON = (By.CSS_SELECTOR, "a.btn-primary[href*='reservation']")
    ROOM_IMAGE = (By.CSS_SELECTOR, "img.hotel-img")

    CALENDAR = (By.CSS_SELECTOR, "div.rbc-calendar")
    CALENDAR_NEXT_BUTTON = (By.CSS_SELECTOR, "button.rbc-btn-group button:last-child")

    FIRSTNAME_INPUT = (By.NAME, "firstname")
    LASTNAME_INPUT = (By.NAME, "lastname")
    EMAIL_INPUT = (By.NAME, "email")
    PHONE_INPUT = (By.NAME, "phone")
    BOOK_SUBMIT_BUTTON = (By.XPATH, "//button[normalize-space()='Reserve Now']")
    BOOKING_CONFIRMATION = (By.CSS_SELECTOR, "div.booking-card")
    BOOKING_SUCCESS_MESSAGE = (By.CSS_SELECTOR, "h3")
    BOOKING_ERROR = (By.CSS_SELECTOR, "div.alert.alert-danger")
    CLOSE_BOOKING_MODAL = (By.CSS_SELECTOR, "button.btn.btn-outline-primary.btn-block")

    CONTACT_NAME = (By.ID, "name")
    CONTACT_EMAIL = (By.ID, "email")
    CONTACT_PHONE = (By.ID, "phone")
    CONTACT_SUBJECT = (By.ID, "subject")
    CONTACT_DESCRIPTION = (By.ID, "description")
    CONTACT_SUBMIT = (By.XPATH, "//button[normalize-space()='Submit']")
    CONTACT_SUCCESS = (By.CSS_SELECTOR, "div.card.shadow")
    CONTACT_ERROR = (By.CSS_SELECTOR, "div.alert.alert-danger")

    def open_home(self):
        self.open(BASE_URL)

    def get_room_count(self) -> int:
        rooms = self.wait_for_elements_visible(self.ROOM_CARDS)
        return len(rooms)

    def click_book_first_room(self):
        buttons = self.wait_for_elements_visible(self.BOOK_BUTTON)
        buttons[0].click()

    def select_dates_by_drag(self):
        calendar = self.wait_for_element_visible(self.CALENDAR, timeout=LONG_TIMEOUT)
        cells = calendar.find_elements(By.CSS_SELECTOR, "div.rbc-day-bg")

        if len(cells) >= 7:
            actions = ActionChains(self.driver)
            start_cell = cells[9]
            end_cell = cells[12]
            actions.click_and_hold(start_cell).move_to_element(end_cell).release().perform()

    def fill_booking_form(self, firstname: str, lastname: str, email: str, phone: str):
        self.type_text(self.FIRSTNAME_INPUT, firstname)
        self.type_text(self.LASTNAME_INPUT, lastname)
        self.type_text(self.EMAIL_INPUT, email)
        self.type_text(self.PHONE_INPUT, phone)

    def submit_booking(self):
        self.click(self.BOOK_SUBMIT_BUTTON)

    def is_booking_confirmed(self) -> bool:
        return self.is_element_visible(self.BOOKING_CONFIRMATION, timeout=LONG_TIMEOUT)

    def get_booking_success_text(self) -> str:
        return self.get_text(self.BOOKING_SUCCESS_MESSAGE)

    def is_booking_error_displayed(self) -> bool:
        return self.is_element_visible(self.BOOKING_ERROR, timeout=5)

    def close_booking_modal(self):
        self.click(self.CLOSE_BOOKING_MODAL)

    def scroll_to_contact(self):
        self.scroll_to_element(self.CONTACT_NAME)

    def fill_contact_form(self, name: str, email: str, phone: str, subject: str, description: str):
        self.type_text(self.CONTACT_NAME, name)
        self.type_text(self.CONTACT_EMAIL, email)
        self.type_text(self.CONTACT_PHONE, phone)
        self.type_text(self.CONTACT_SUBJECT, subject)
        self.type_text(self.CONTACT_DESCRIPTION, description)

    def submit_contact(self):
        self.scroll_to_element(self.CONTACT_SUBMIT)
        self.click(self.CONTACT_SUBMIT)

    def is_contact_success_displayed(self) -> bool:
        return self.is_element_visible(self.CONTACT_SUCCESS, timeout=LONG_TIMEOUT)

    def get_contact_success_text(self) -> str:
        return self.get_text(self.CONTACT_SUCCESS)

    def is_contact_error_displayed(self) -> bool:
        return self.is_element_visible(self.CONTACT_ERROR, timeout=5)
