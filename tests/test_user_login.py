from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators import AutorisationLocators
import data


class TestUserLogin:

    def test_login_user_success(self, driver):
        driver.get(data.URL)

        WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located(
                AutorisationLocators.LOGIN_BUTTON
            )
        )

        driver.find_element(*AutorisationLocators.LOGIN_BUTTON).click()
        driver.find_element(*AutorisationLocators.EMAIL_FIELD).send_keys(data.EMAIL)
        driver.find_element(*AutorisationLocators.PASSWORD_FIELD).send_keys(
            data.PASSWORD
        )
        driver.find_element(*AutorisationLocators.SIGNIN_BUTTON).click()

        WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located(
                AutorisationLocators.USER_NAME
            )
        )
        user_name = driver.find_element(*AutorisationLocators.USER_NAME).text
        avatar = driver.find_elements(*AutorisationLocators.USER_AVATAR)

        assert (
            driver.current_url == "https://qa-desk.education-services.ru/login"
            and user_name == "User."
            and len(avatar) == 1
        )

        driver.quit()
