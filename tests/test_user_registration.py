from selenium.webdriver.support import expected_conditions as EC

from data import (
    DEFAULT_PASSWORD,
    ERROR_TEXT,
    EXPECTED_USER_NAME,
    INVALID_EMAIL,
    generate_random_email,
)
from locators import (
    ErrorLocators,
    LoginPageLocators,
    MainPageLocators,
    ProfilePageLocators,
    RegistrationPageLocators,
)


class TestUserRegistration:
    def test_user_registration(self, driver, browser_wait):
        email = generate_random_email()
        driver.find_element(*MainPageLocators.LOGIN_BUTTON).click()
        browser_wait.until(
            EC.element_to_be_clickable(LoginPageLocators.CREATE_ACCOUNT_BUTTON)
        ).click()
        browser_wait.until(
            EC.visibility_of_element_located(
                RegistrationPageLocators.REGISTRATION_TITLE
            )
        )

        driver.find_element(*LoginPageLocators.EMAIL_INPUT).send_keys(email)
        driver.find_element(*LoginPageLocators.PASSWORD_INPUT).send_keys(
            DEFAULT_PASSWORD
        )
        driver.find_element(
            *RegistrationPageLocators.CONFIRM_PASSWORD_INPUT
        ).send_keys(DEFAULT_PASSWORD)
        driver.find_element(*RegistrationPageLocators.CREATE_ACCOUNT_BUTTON).click()

        user_name = browser_wait.until(
            EC.visibility_of_element_located(ProfilePageLocators.USER_NAME)
        )
        user_avatar = browser_wait.until(
            EC.visibility_of_element_located(ProfilePageLocators.USER_AVATAR)
        )

        assert user_name.text == EXPECTED_USER_NAME
        assert user_avatar.is_displayed() is True

    def test_user_registration_with_invalid_email_format(self, driver, browser_wait):
        driver.find_element(*MainPageLocators.LOGIN_BUTTON).click()
        browser_wait.until(
            EC.element_to_be_clickable(LoginPageLocators.CREATE_ACCOUNT_BUTTON)
        ).click()
        browser_wait.until(
            EC.visibility_of_element_located(
                RegistrationPageLocators.REGISTRATION_TITLE
            )
        )

        driver.find_element(*LoginPageLocators.EMAIL_INPUT).send_keys(INVALID_EMAIL)
        driver.find_element(*RegistrationPageLocators.CREATE_ACCOUNT_BUTTON).click()

        error_text = browser_wait.until(
            EC.visibility_of_element_located(ErrorLocators.ERROR_TEXT)
        )
        email_input_error = browser_wait.until(
            EC.visibility_of_element_located(ErrorLocators.EMAIL_INPUT_ERROR)
        )
        password_input_error = browser_wait.until(
            EC.visibility_of_element_located(ErrorLocators.PASSWORD_INPUT_ERROR)
        )
        confirm_password_input_error = browser_wait.until(
            EC.visibility_of_element_located(
                ErrorLocators.CONFIRM_PASSWORD_INPUT_ERROR
            )
        )

        assert error_text.text == ERROR_TEXT
        assert email_input_error.is_displayed() is True
        assert password_input_error.is_displayed() is True
        assert confirm_password_input_error.is_displayed() is True

    def test_existing_user_registration(self, browser_wait, add_user):
        driver = add_user
        email = driver.created_email
        browser_wait.until(
            EC.element_to_be_clickable(ProfilePageLocators.LOGOUT_BUTTON)
        ).click()
        browser_wait.until(
            EC.element_to_be_clickable(MainPageLocators.LOGIN_BUTTON)
        ).click()
        browser_wait.until(
            EC.element_to_be_clickable(LoginPageLocators.CREATE_ACCOUNT_BUTTON)
        ).click()
        browser_wait.until(
            EC.visibility_of_element_located(
                RegistrationPageLocators.REGISTRATION_TITLE
            )
        )

        driver.find_element(*LoginPageLocators.EMAIL_INPUT).send_keys(email)
        driver.find_element(*LoginPageLocators.PASSWORD_INPUT).send_keys(
            DEFAULT_PASSWORD
        )
        driver.find_element(
            *RegistrationPageLocators.CONFIRM_PASSWORD_INPUT
        ).send_keys(DEFAULT_PASSWORD)
        driver.find_element(*RegistrationPageLocators.CREATE_ACCOUNT_BUTTON).click()

        error_text = browser_wait.until(
            EC.visibility_of_element_located(ErrorLocators.ERROR_TEXT)
        )
        email_input_error = browser_wait.until(
            EC.visibility_of_element_located(ErrorLocators.EMAIL_INPUT_ERROR)
        )
        password_input_error = browser_wait.until(
            EC.visibility_of_element_located(ErrorLocators.PASSWORD_INPUT_ERROR)
        )
        confirm_password_input_error = browser_wait.until(
            EC.visibility_of_element_located(
                ErrorLocators.CONFIRM_PASSWORD_INPUT_ERROR
            )
        )

        assert error_text.text == ERROR_TEXT
        assert email_input_error.is_displayed() is True
        assert password_input_error.is_displayed() is True
        assert confirm_password_input_error.is_displayed() is True
