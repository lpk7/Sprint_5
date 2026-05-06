from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators import AutorisationLocators
from data import Links


class TestCreateAdNotLogin:
    def test_create_ad_user_is_not_login_fail(self, driver):
        driver.get(Links.STAND)

        WebDriverWait(driver, 5).until(
            expected_conditions.element_to_be_clickable(
                AutorisationLocators.NEW_PUBLISH_BUTTON
            )
        )

        driver.find_element(*AutorisationLocators.NEW_PUBLISH_BUTTON).click()
        WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located(
                AutorisationLocators.POPUP_HEADING
            )
        )

        assert (
            driver.find_element(*AutorisationLocators.POPUP_HEADING).text
            == "Чтобы разместить объявление, авторизуйтесь"
        )
