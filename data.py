import random


BASE_URL = "https://qa-desk.education-services.ru/"
DEFAULT_PASSWORD = "1234567890"
INVALID_EMAIL = "@.con"

EXPECTED_USER_NAME = "User."
ERROR_TEXT = "Ошибка"
AUTH_REQUIRED_TEXT = "Чтобы разместить объявление, авторизуйтесь"

ADVERT_NAME_PREFIX = "Горшок"
ADVERT_DESCRIPTION = "Тестовое описание товара"
ADVERT_PRICE = "11111"


def generate_random_email():
    return f"user_{random.randint(1000, 9999)}@gmail.com"


def generate_random_advert_name():
    return f"{ADVERT_NAME_PREFIX}_{random.randint(1000, 9999)}"
