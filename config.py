BASE_URL = "https://automationintesting.online/"
ADMIN_URL = "https://automationintesting.online/admin/"

ADMIN_USERNAME = "admin"
ADMIN_PASSWORD = "password"

DEFAULT_TIMEOUT = 10
LONG_TIMEOUT = 20
STEP_DELAY = 1.5

VALID_BOOKING = {
    "firstname": "Hajar",
    "lastname": "Khettou",
    "email": "hajar.khettou@epita.fr",
    "phone": "06123456787",
}

VALID_MESSAGE = {
    "name": "Christina Lopes",
    "email": "christina.lopes@epita.fr",
    "phone": "06987654327",
    "subject": "Question sur une réservation",
    "description": "Bonjour, je souhaite avoir des informations sur la disponibilité des chambres pour le mois de juillet.",
}

INVALID_LOGIN = {
    "username": "wrong_user",
    "password": "wrong_pass",
}

EMPTY_BOOKING = {
    "firstname": "",
    "lastname": "",
    "email": "",
    "phone": "",
}

INVALID_BOOKING = {
    "firstname": "A",
    "lastname": "",
    "email": "invalid-email",
    "phone": "123",
}