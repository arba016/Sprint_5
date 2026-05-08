from selenium.webdriver.support import expected_conditions as EC

from locators import ProfilePageLocators


class TestUserLogout:
    def test_user_logout(self, browser_wait, add_user):
        driver = add_user
        browser_wait.until(
            EC.element_to_be_clickable(ProfilePageLocators.LOGOUT_BUTTON)
        ).click()

        assert browser_wait.until(
            EC.invisibility_of_element_located(ProfilePageLocators.USER_NAME)
        )
        assert browser_wait.until(
            EC.invisibility_of_element_located(ProfilePageLocators.USER_AVATAR)
        )
