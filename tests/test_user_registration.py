from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators import AutorisationLocators
import pytest
from data import Links, UserCredentials
import helpers


class TestUserRegistration:
    def test_registration_new_user_success(self, driver):
        email = helpers.email()
        password = helpers.password()
        driver.get(Links.STAND)
        WebDriverWait(driver, 5).until(
            expected_conditions.element_to_be_clickable(
                AutorisationLocators.LOGIN_BUTTON
            )
        )

        driver.find_element(*AutorisationLocators.LOGIN_BUTTON).click()
        WebDriverWait(driver, 5).until(
            expected_conditions.element_to_be_clickable(
                AutorisationLocators.NEW_ACC_BUTTON
            )
        )
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
            driver.current_url == Links.USER_REGISTRATION_PAGE
            and user_name == "User."
            and len(avatar) == 1
        )

    @pytest.mark.parametrize("mail", UserCredentials.WRONG_EMAIL)
    def test_registration_new_user_bed_email(self, mail, driver):
        password = helpers.password()
        driver.get(Links.STAND)
        WebDriverWait(driver, 5).until(
            expected_conditions.element_to_be_clickable(
                AutorisationLocators.LOGIN_BUTTON
            )
        )

        driver.find_element(*AutorisationLocators.LOGIN_BUTTON).click()
        WebDriverWait(driver, 5).until(
            expected_conditions.element_to_be_clickable(
                AutorisationLocators.NEW_ACC_BUTTON
            )
        )
        driver.find_element(*AutorisationLocators.NEW_ACC_BUTTON).click()

        driver.find_element(*AutorisationLocators.EMAIL_FIELD).send_keys(mail)
        driver.find_element(*AutorisationLocators.PASSWORD_FIELD).send_keys(password)
        driver.find_element(*AutorisationLocators.SUBMIT_PASSWORD_FIELD).send_keys(
            password
        )
        driver.find_element(*AutorisationLocators.CREATE_ACC_BUTTON).click()

        assert (
            WebDriverWait(driver, 5).until(
                expected_conditions.visibility_of_element_located(
                    AutorisationLocators.ERROR_EMAIL
                )
            )
            and len(driver.find_elements(*AutorisationLocators.ERROR_EMAIL)) == 1
            and len(driver.find_elements(*AutorisationLocators.ERROR_FIELD)) == 3
        )

    def test_registration_new_user_email_is_registered(self, driver):
        driver.get(Links.STAND)
        WebDriverWait(driver, 5).until(
            expected_conditions.element_to_be_clickable(
                AutorisationLocators.LOGIN_BUTTON
            )
        )

        driver.find_element(*AutorisationLocators.LOGIN_BUTTON).click()
        WebDriverWait(driver, 5).until(
            expected_conditions.element_to_be_clickable(
                AutorisationLocators.NEW_ACC_BUTTON
            )
        )
        driver.find_element(*AutorisationLocators.NEW_ACC_BUTTON).click()

        driver.find_element(*AutorisationLocators.EMAIL_FIELD).send_keys(UserCredentials.EMAIL)
        driver.find_element(*AutorisationLocators.PASSWORD_FIELD).send_keys(
            UserCredentials.PASSWORD
        )
        driver.find_element(*AutorisationLocators.SUBMIT_PASSWORD_FIELD).send_keys(
            UserCredentials.PASSWORD
        )
        driver.find_element(*AutorisationLocators.CREATE_ACC_BUTTON).click()

        assert (
            WebDriverWait(driver, 5).until(
                expected_conditions.visibility_of_element_located(
                    AutorisationLocators.ERROR_EMAIL
                )
            )
            and len(driver.find_elements(*AutorisationLocators.ERROR_EMAIL)) == 1
            and len(driver.find_elements(*AutorisationLocators.ERROR_FIELD)) == 3
        )
