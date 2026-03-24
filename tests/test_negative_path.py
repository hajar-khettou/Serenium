import pytest
from pages.home_page import HomePage
from pages.login_page import LoginPage
from pages.admin_page import AdminPage
from config import INVALID_LOGIN, ADMIN_USERNAME, ADMIN_PASSWORD


def _open_booking_form(driver):
    home = HomePage(driver)
    home.open_home()
    home.click_book_first_room()
    home.select_dates_by_drag()
    return home


class TestBookingNegativePath:

    def test_booking_without_firstname(self, driver):
        home = _open_booking_form(driver)
        home.fill_booking_form(
            firstname="",
            lastname="lopes",
            email="test@epita.fr",
            phone="06123456789",
        )
        home.submit_booking()
        assert home.is_booking_error_displayed(), (
            "TC-004 FAIL : aucun message d'erreur affiché alors que le "
            "prénom est vide. Résultat attendu : 'firstname should not be blank'."
        )

    def test_booking_without_email(self, driver):
        home = _open_booking_form(driver)
        home.fill_booking_form(
            firstname="Christina",
            lastname="Lopes",
            email="",
            phone="06123456789",
        )
        home.submit_booking()
        assert home.is_booking_error_displayed(), (
            "TC-005 FAIL : aucun message d'erreur affiché alors que "
            "l'email est vide. Résultat attendu : 'must not be empty'."
        )

    def test_booking_with_invalid_email(self, driver):
        home = _open_booking_form(driver)
        home.fill_booking_form(
            firstname="Christina",
            lastname="Lopes",
            email="emailinvalide",
            phone="06123456789",
        )
        home.submit_booking()
        assert home.is_booking_error_displayed(), (
            "TC-006 FAIL (bug connu) : l'application n'affiche pas "
            "d'erreur pour un email invalide — la réservation est acceptée "
            "à tort. Résultat attendu : 'must be a well-formed email address'."
        )

    @pytest.mark.xfail(reason="BUG-001 : l'appli rejette les numéros à 10 chiffres", strict=True)
    def test_booking_with_short_phone(self, driver):
        home = _open_booking_form(driver)
        home.fill_booking_form(
            firstname="Christina",
            lastname="Lopes",
            email="test@epita.fr",
            phone="0612345678",
        )
        home.submit_booking()
        assert not home.is_booking_error_displayed(), (
            "TC-BUG-001 FAIL (bug connu) : un numéro à 10 chiffres est "
            "rejeté par l'application. Résultat attendu : la réservation "
            "doit être acceptée avec un numéro standard à 10 chiffres."
        )


class TestContactNegativePath:

    def test_contact_without_name(self, driver):
        home = HomePage(driver)
        home.open_home()
        home.scroll_to_contact()
        home.fill_contact_form(
            name="",
            email="test@epita.fr",
            phone="06123456789",
            subject="Sujet valide ici",
            description="Description suffisamment longue pour passer la validation minimale.",
        )
        home.submit_contact()
        assert home.is_contact_error_displayed(), (
            "TC-012 FAIL : aucun message d'erreur affiché alors que le "
            "nom est vide."
        )

    def test_contact_without_email(self, driver):
        home = HomePage(driver)
        home.open_home()
        home.scroll_to_contact()
        home.fill_contact_form(
            name="Christina Lopes",
            email="",
            phone="06123456789",
            subject="Sujet valide ici",
            description="Description suffisamment longue pour passer la validation minimale.",
        )
        home.submit_contact()
        assert home.is_contact_error_displayed(), (
            "TC-014 FAIL : aucun message d'erreur affiché alors que "
            "l'email est vide."
        )


class TestAdminLoginNegativePath:

    def test_login_with_wrong_credentials(self, driver):
        login = LoginPage(driver)
        admin = AdminPage(driver)
        login.open_admin_login()
        login.login(
            username=INVALID_LOGIN["username"],
            password=INVALID_LOGIN["password"],
        )
        assert login.is_login_error_displayed(), (
            "TC-016 FAIL : aucun message d'erreur affiché après une "
            "tentative de connexion avec de mauvais identifiants."
        )
        assert not admin.is_admin_loaded(), (
            "TC-016 FAIL : le panneau admin est accessible alors que les "
            "identifiants sont incorrects."
        )
