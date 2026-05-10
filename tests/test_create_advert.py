from selenium.webdriver.support import expected_conditions as EC

from data import (
    ADVERT_DESCRIPTION,
    ADVERT_PRICE,
    AUTH_REQUIRED_TEXT,
    generate_random_advert_name,
)
from locators import (
    LoginPageLocators,
    MainPageLocators,
    NewListingPageLocators,
    ProfilePageLocators,
)


class TestCreateAdvert:
    def test_create_advert_by_unauthorized_user(self, driver, browser_wait):
        driver.find_element(*MainPageLocators.CREATE_LISTING_BUTTON).click()

        assert browser_wait.until(
            EC.visibility_of_element_located(LoginPageLocators.AUTH_REQUIRED_TITLE),
            message="Окно авторизации не отобразилось",
        )

        print(f"Окно авторизации отобразилось")

    def test_create_advert_by_authorized_user(self, browser_wait, add_user):
        driver = add_user
        advert_name = generate_random_advert_name()
        driver.find_element(*MainPageLocators.CREATE_LISTING_BUTTON).click()
        browser_wait.until(
            EC.visibility_of_element_located(NewListingPageLocators.NEW_LISTING_TITLE)
        )

        driver.find_element(*NewListingPageLocators.LISTING_NAME_INPUT).send_keys(
            advert_name
        )
        driver.find_element(*NewListingPageLocators.DESCRIPTION_INPUT).send_keys(
            ADVERT_DESCRIPTION
        )
        driver.find_element(*NewListingPageLocators.PRICE_INPUT).send_keys(ADVERT_PRICE)
        driver.find_element(*NewListingPageLocators.CATEGORY_DROPDOWN).click()
        browser_wait.until(
            EC.element_to_be_clickable(NewListingPageLocators.TECHNOLOGY_CATEGORY)
        ).click()
        driver.find_element(*NewListingPageLocators.CITY_DROPDOWN).click()
        browser_wait.until(
            EC.element_to_be_clickable(NewListingPageLocators.EKATERINBURG_CITY)
        ).click()
        driver.find_element(*NewListingPageLocators.NEW_CONDITION_RADIO).click()
        browser_wait.until(
            EC.element_to_be_clickable(NewListingPageLocators.USED_CONDITION_RADIO)
        ).click()

        publish_button = browser_wait.until(
            EC.element_to_be_clickable(NewListingPageLocators.PUBLISH_BUTTON)
        )
        driver.execute_script(
            "arguments[0].scrollIntoView();",
            publish_button,
        )
        publish_button.click()

        browser_wait.until(
            EC.invisibility_of_element_located(NewListingPageLocators.PUBLISH_BUTTON)
        )

        driver.execute_script("window.scrollTo(0, 0);")

        user_avatar = browser_wait.until(
            EC.element_to_be_clickable(ProfilePageLocators.USER_AVATAR)
        )
        # driver.execute_script("arguments[0].scrollIntoView();", user_avatar)
        user_avatar.click()

        browser_wait.until(
            EC.visibility_of_element_located(ProfilePageLocators.PROFILE_TITLE)
        )

        user_adverts_title = browser_wait.until(
            EC.visibility_of_element_located(ProfilePageLocators.USER_ADVERTS_TITLE)
        )

        driver.execute_script("arguments[0].scrollIntoView();", user_adverts_title)

        assert browser_wait.until(
            EC.visibility_of_element_located(
                ProfilePageLocators.advert_title(advert_name)
            )
        )
