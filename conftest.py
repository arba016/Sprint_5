import pytest
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.chrome.options import Options

from data import BASE_URL, DEFAULT_PASSWORD, generate_random_email
from locators import (
    LoginPageLocators,
    MainPageLocators,
    ProfilePageLocators,
    RegistrationPageLocators,
)


@pytest.fixture
def driver():

    options = Options()
    options.add_argument("--window-size=1920,1080")
    browser = webdriver.Chrome(options=options)
    browser.get(BASE_URL)
    yield browser
    browser.quit()


@pytest.fixture
def browser_wait(driver):
    return WebDriverWait(driver, 10)


@pytest.fixture
def add_user(driver, browser_wait):
    email = generate_random_email()
    register_user(driver, browser_wait, email)
    driver.created_email = email
    return driver


def register_user(driver, browser_wait, email):

    driver.find_element(*MainPageLocators.LOGIN_BUTTON).click()
    browser_wait.until(
        EC.element_to_be_clickable(LoginPageLocators.CREATE_ACCOUNT_BUTTON)
    ).click()
    browser_wait.until(
        EC.visibility_of_element_located(RegistrationPageLocators.REGISTRATION_TITLE)
    )
    driver.find_element(*LoginPageLocators.EMAIL_INPUT).send_keys(email)
    driver.find_element(*LoginPageLocators.PASSWORD_INPUT).send_keys(DEFAULT_PASSWORD)
    driver.find_element(*RegistrationPageLocators.CONFIRM_PASSWORD_INPUT).send_keys(
        DEFAULT_PASSWORD
    )
    driver.find_element(*RegistrationPageLocators.CREATE_ACCOUNT_BUTTON).click()
    browser_wait.until(EC.visibility_of_element_located(ProfilePageLocators.USER_AVATAR))
