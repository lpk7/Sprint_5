from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators import AutorisationLocators
from data import Links, UserCredentials
import helpers


class TestCreateAd:
    def test_create_ad_success(self, driver):
        name = "Продам мопед"
        price = helpers.price()
        driver.get(Links.STAND)

        WebDriverWait(driver, 5).until(
            expected_conditions.element_to_be_clickable(
                AutorisationLocators.LOGIN_BUTTON
            )
        )

        driver.find_element(*AutorisationLocators.LOGIN_BUTTON).click()
        WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located(
                AutorisationLocators.POPUP_HEADING
            )
        )

        driver.find_element(*AutorisationLocators.EMAIL_FIELD).send_keys(UserCredentials.EMAIL)
        driver.find_element(*AutorisationLocators.PASSWORD_FIELD).send_keys(
            UserCredentials.PASSWORD
        )
        driver.find_element(*AutorisationLocators.SIGNIN_BUTTON).click()

        WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located(
                AutorisationLocators.USER_NAME
            )
        )

        driver.find_element(*AutorisationLocators.NEW_PUBLISH_BUTTON).click()
        driver.find_element(*AutorisationLocators.NAME_FIELD).send_keys(name)
        driver.find_element(*AutorisationLocators.CATEGORIES_MENU_BUTTON).click()
        driver.find_element(*AutorisationLocators.CATEGORIES_ITEM_BUTTON).click()
        driver.find_element(*AutorisationLocators.RADIO_BUTTON).click()
        driver.find_element(*AutorisationLocators.CITY_MENU_BUTTON).click()
        driver.find_element(*AutorisationLocators.CITY_ITEM_BUTTON).click()
        driver.find_element(*AutorisationLocators.DISCPIPTION_FIELD).send_keys(
            "Мопед на ходу, с документами. небольшой пробег 90 на обкатке, с новым китайским двигателем ф 100, зажигание эллектронное, расход 3 литра на 100км, хорошо сохранился до наших дней, благнаодаря сухому гаражу и заботливаему хозяину. Хороший подарок на ДР"
        )
        driver.find_element(*AutorisationLocators.PRICE_FIELD).send_keys(price)
        driver.find_element(*AutorisationLocators.PUBLISH_BUTTON).click()

        WebDriverWait(driver, 5).until(expected_conditions.url_to_be(Links.STAND))

        driver.find_element(*AutorisationLocators.USER_PROFILE_BUTTON).click()
        WebDriverWait(driver, 5).until(
            expected_conditions.element_to_be_clickable(AutorisationLocators.NEW_ADS)
        )
        ads = driver.find_elements(*AutorisationLocators.NEW_ADS)

        assert any(ad.text == "Продам мопед" for ad in ads)
