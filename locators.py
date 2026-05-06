from selenium.webdriver.common.by import By


class MainPageLocators:
    LOGIN_BUTTON = (By.XPATH, "//button[text()='Вход и регистрация']")
    CREATE_LISTING_BUTTON = (By.XPATH, "//button[text()='Разместить объявление']")


class LoginPageLocators:
    EMAIL_INPUT = (By.NAME, "email")
    PASSWORD_INPUT = (By.NAME, "password")
    CREATE_ACCOUNT_BUTTON = (By.XPATH, "//button[text()='Нет аккаунта']")
    LOGIN_BUTTON = (By.XPATH, "//button[text()='Войти']")
    LOGIN_TITLE = (By.XPATH, "//h1[text()='Войти']")
    AUTH_REQUIRED_TITLE = (
        By.XPATH,
        "//h1[text()='Чтобы разместить объявление, авторизуйтесь']",
    )


class RegistrationPageLocators:
    REGISTRATION_TITLE = (By.XPATH, "//h1[text()='Зарегистрироваться']")
    CREATE_ACCOUNT_BUTTON = (By.XPATH, "//button[text()='Создать аккаунт']")
    HAVE_ACCOUNT_BUTTON = (By.XPATH, "//button[text()='Уже есть аккаунт']")
    CONFIRM_PASSWORD_INPUT = (By.NAME, "submitPassword")


class NewListingPageLocators:
    NEW_LISTING_TITLE = (By.XPATH, "//h1[text()='Новое объявление']")
    LISTING_NAME_INPUT = (By.NAME, "name")
    CATEGORY_DROPDOWN = (
        By.XPATH,
        "//div[2]/div[1]/button[contains(@class, 'dropDownMenu_arrowDown')]",
    )
    TECHNOLOGY_CATEGORY = (By.XPATH, "//span[text()='Технологии']")
    CITY_DROPDOWN = (
        By.XPATH,
        "//div[3]/div[1]/button[contains(@class, 'dropDownMenu_arrowDown')]",
    )
    EKATERINBURG_CITY = (By.XPATH, "//span[text()='Екатеринбург']")
    NEW_CONDITION_RADIO = (By.CLASS_NAME, "radioUnput_inputActive__eC-HY")
    USED_CONDITION_RADIO = (By.CLASS_NAME, "radioUnput_inputRegular__FbVbr")
    DESCRIPTION_INPUT = (By.CSS_SELECTOR, ".textarea_inputStandart__IoNxq.spanGlobal")
    PRICE_INPUT = (By.NAME, "price")
    PUBLISH_BUTTON = (By.XPATH, "//button[text()='Опубликовать']")


class ProfilePageLocators:
    USER_NAME = (By.XPATH, "//h3[text()='User.']")
    USER_AVATAR = (By.CLASS_NAME, "circleSmall")
    LOGOUT_BUTTON = (By.CSS_SELECTOR, ".btnSmall")
    PROFILE_TITLE = (By.XPATH, "//h1[text()='Мой профиль']")
    USER_ADVERTS_TITLE = (By.XPATH, "//h1[text()='Мои объявления']")

    @staticmethod
    def advert_title(advert_name):
        return (By.XPATH, f"//h2[text()='{advert_name}']")


class ErrorLocators:
    ERROR_TEXT = (By.XPATH, "//span[text()='Ошибка']")
    EMAIL_INPUT_ERROR = (
        By.XPATH,
        "//div[1]/div/div[contains(@class, 'input_inputError')]",
    )
    PASSWORD_INPUT_ERROR = (
        By.XPATH,
        "//div[2]/div/div[contains(@class, 'input_inputError')]",
    )
    CONFIRM_PASSWORD_INPUT_ERROR = (
        By.XPATH,
        "//div[3]/div/div[contains(@class, 'input_inputError')]",
    )
