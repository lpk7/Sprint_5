from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators import AutorisationLocators
import pytest
import data


class TestUserRegistration:
    def test_registration_new_user_success(self, email, password, driver):
        driver.get(data.URL)
        WebDriverWait(driver, 5).until(
            expected_conditions.element_to_be_clickable(
                AutorisationLocators.LOGIN_BUTTON
            )
        )

        driver.find_element(*AutorisationLocators.LOGIN_BUTTON).click()
        driver.find_element(*AutorisationLocators.NEW_ACC_BUTTON).click()

        driver.find_element(*AutorisationLocators.EMAIL_FIELD).send_keys(email)
        driver.find_element(*AutorisationLocators.PASSWORD_FIELD).send_keys(password)
        driver.find_element(*AutorisationLocators.SUBMIT_PASSWORD_FIELD).send_keys(
            password
        )
        driver.find_element(*AutorisationLocators.CREATE_ACC_BUTTON).click()

        WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located(
                AutorisationLocators.USER_NAME
            )
        )
        user_name = driver.find_element(*AutorisationLocators.USER_NAME).text
        avatar = driver.find_elements(*AutorisationLocators.USER_AVATAR)

        assert (
            driver.current_url == "https://qa-desk.education-services.ru/regiatration"
            and user_name == "User."
            and len(avatar) == 1
        )

        driver.quit()

    @pytest.mark.parametrize(
        "mail", [("email.ru"), ("email@ru"), ("email@gmail,com"), ("@gmail.com")]
    )
    def test_registration_new_user_bed_email(self, mail, driver, password):
        driver.get(data.URL)
        WebDriverWait(driver, 5).until(
            expected_conditions.element_to_be_clickable(
                AutorisationLocators.LOGIN_BUTTON
            )
        )

        driver.find_element(*AutorisationLocators.LOGIN_BUTTON).click()
        driver.find_element(*AutorisationLocators.NEW_ACC_BUTTON).click()

        driver.find_element(*AutorisationLocators.EMAIL_FIELD).send_keys(mail)
        driver.find_element(*AutorisationLocators.PASSWORD_FIELD).send_keys(password)
        driver.find_element(*AutorisationLocators.SUBMIT_PASSWORD_FIELD).send_keys(
            password
        )
        driver.find_element(*AutorisationLocators.CREATE_ACC_BUTTON).click()

        WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located(
                AutorisationLocators.ERROR_EMAIL
            )
        )

        assert (
            driver.find_element(*AutorisationLocators.ERROR_EMAIL).text == "Ошибка"
            and len(driver.find_elements(*AutorisationLocators.ERROR_FIELD)) == 3
        )
        driver.quit()

    def test_registration_new_user_email_is_registered(self, driver):
        driver.get(data.URL)
        WebDriverWait(driver, 5).until(
            expected_conditions.element_to_be_clickable(
                AutorisationLocators.LOGIN_BUTTON
            )
        )

        driver.find_element(*AutorisationLocators.LOGIN_BUTTON).click()
        driver.find_element(*AutorisationLocators.NEW_ACC_BUTTON).click()

        driver.find_element(*AutorisationLocators.EMAIL_FIELD).send_keys(data.EMAIL)
        driver.find_element(*AutorisationLocators.PASSWORD_FIELD).send_keys(
            data.PASSWORD
        )
        driver.find_element(*AutorisationLocators.SUBMIT_PASSWORD_FIELD).send_keys(
            data.PASSWORD
        )
        driver.find_element(*AutorisationLocators.CREATE_ACC_BUTTON).click()

        WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located(
                AutorisationLocators.ERROR_EMAIL
            )
        )

        assert (
            driver.find_element(*AutorisationLocators.ERROR_EMAIL).text == "Ошибка"
            and len(driver.find_elements(*AutorisationLocators.ERROR_FIELD)) == 3
        )
        driver.quit()
