from selenium.webdriver.support import expected_conditions as EC

from data import DEFAULT_PASSWORD, EXPECTED_USER_NAME
from locators import LoginPageLocators, MainPageLocators, ProfilePageLocators


class TestUserLogin:
    def test_user_login(self, browser_wait, add_user):
        driver = add_user
        email = driver.created_email
        browser_wait.until(
            EC.element_to_be_clickable(ProfilePageLocators.LOGOUT_BUTTON)
        ).click()
        browser_wait.until(
            EC.element_to_be_clickable(MainPageLocators.LOGIN_BUTTON)
        ).click()
        browser_wait.until(
            EC.visibility_of_element_located(LoginPageLocators.LOGIN_TITLE)
        )

        driver.find_element(*LoginPageLocators.EMAIL_INPUT).send_keys(email)
        driver.find_element(*LoginPageLocators.PASSWORD_INPUT).send_keys(
            DEFAULT_PASSWORD
        )
        driver.find_element(*LoginPageLocators.LOGIN_BUTTON).click()

        assert browser_wait.until(
            EC.visibility_of_element_located(ProfilePageLocators.USER_NAME)
        )

        assert browser_wait.until(
            EC.visibility_of_element_located(ProfilePageLocators.USER_AVATAR)
        )
