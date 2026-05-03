from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators import AutorisationLocators
import data


class TestUserLogout:

    def test_logout_user_success(self, driver):
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
        driver.find_element(*AutorisationLocators.SIGNOUT_BUTTON).click()

        WebDriverWait(driver, 5).until(
            expected_conditions.element_to_be_clickable(
                AutorisationLocators.LOGIN_BUTTON
            )
        )
        user_name = driver.find_elements(*AutorisationLocators.USER_NAME)
        avatar = driver.find_elements(*AutorisationLocators.USER_AVATAR)

        assert (
            driver.current_url == data.URL
            and not len(user_name)
            and not len(avatar)
            and driver.find_element(*AutorisationLocators.LOGIN_BUTTON).text
            == "Вход и регистрация"
        )

        driver.quit()
