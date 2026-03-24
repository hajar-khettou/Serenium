import pytest
import time
from pages.home_page import HomePage
from pages.login_page import LoginPage
from pages.admin_page import AdminPage
from config import VALID_BOOKING, VALID_MESSAGE, ADMIN_USERNAME, ADMIN_PASSWORD


@pytest.fixture
def logged_in_admin(driver):
    login = LoginPage(driver)
    login.open_admin_login()
    login.login(username=ADMIN_USERNAME, password=ADMIN_PASSWORD)
    admin = AdminPage(driver)
    admin.is_admin_loaded()
    return admin


class TestBookingHappyPath:

    def test_valid_booking(self, driver):
        home = HomePage(driver)
        home.open_home()
        home.click_book_first_room()
        home.fill_booking_form(
            firstname=VALID_BOOKING["firstname"],
            lastname=VALID_BOOKING["lastname"],
            email=VALID_BOOKING["email"],
            phone=VALID_BOOKING["phone"],
        )
        home.submit_booking()
        assert home.is_booking_confirmed(), \
            "La confirmation de réservation n'est pas affichée après une réservation valide."


class TestContactHappyPath:

    def test_valid_contact_message(self, driver):
        home = HomePage(driver)
        home.open_home()
        home.scroll_to_contact()
        home.fill_contact_form(
            name=VALID_MESSAGE["name"],
            email=VALID_MESSAGE["email"],
            phone=VALID_MESSAGE["phone"],
            subject=VALID_MESSAGE["subject"],
            description=VALID_MESSAGE["description"],
        )
        home.submit_contact()
        assert home.is_contact_success_displayed(), \
            "Le message de confirmation du contact n'est pas affiché."


class TestAdminLoginHappyPath:

    def test_valid_admin_login(self, driver):
        login = LoginPage(driver)
        admin = AdminPage(driver)
        login.open_admin_login()
        login.login(username=ADMIN_USERNAME, password=ADMIN_PASSWORD)
        assert admin.is_admin_loaded(), \
            "Le tableau de bord admin n'est pas accessible après connexion."


class TestRoomManagementHappyPath:

    def test_create_room(self, logged_in_admin):
        admin = logged_in_admin
        room_number = str(int(time.time()) % 301 + 200)
        admin.create_room(
            room_number=room_number,
            room_type="Double",
            accessible="true",
            price="120",
            amenities=["wifi", "tv", "safe"],
        )
        admin.driver.refresh()
        admin.is_admin_loaded()
        assert admin.room_exists(room_number), \
            f"La chambre {room_number} n'a pas été créée."

    def test_delete_room(self, logged_in_admin):
        admin = logged_in_admin
        admin.create_room(
            room_number="888",
            room_type="Single",
            accessible="false",
            price="80",
            amenities=["wifi"],
        )
        admin.driver.refresh()
        admin.is_admin_loaded()
        initial_count = admin.get_room_count()
        admin.delete_last_room()
        admin.driver.refresh()
        admin.is_admin_loaded()
        new_count = admin.get_room_count()
        assert new_count < initial_count, \
            f"La chambre n'a pas été supprimée. Avant: {initial_count}, Après: {new_count}"


class TestReservationManagementHappyPath:

    def test_view_reservations_in_admin(self, logged_in_admin):
        admin = logged_in_admin
        assert admin.is_element_visible(admin.ROOM_NUMBER_INPUT, timeout=40), \
            "Le panneau admin ne charge pas correctement."
