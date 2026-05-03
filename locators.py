from selenium.webdriver.common.by import By


class AutorisationLocators:
    # Кнопка вход и регистрация
    LOGIN_BUTTON = By.XPATH, ".//button[contains(text(), 'Вход')]"
    # Кнопка нет аккаунта
    NEW_ACC_BUTTON = By.XPATH, '//button[contains(text(), "Нет")]'
    # Поля формы регистрации
    EMAIL_FIELD = By.XPATH, '//*[@name="email"]'
    PASSWORD_FIELD = By.XPATH, '//*[@name="password"]'
    SUBMIT_PASSWORD_FIELD = By.XPATH, '//*[@name="submitPassword"]'

    # Кнопка создать аккаунт
    CREATE_ACC_BUTTON = By.XPATH, '//button[contains(text(), "Создать")]'
    # Аватар и имя пользователя
    USER_AVATAR = By.CSS_SELECTOR, ".circleSmall"
    USER_NAME = By.CSS_SELECTOR, ".name"
    # Ошибка под полем email
    ERROR_EMAIL = (
        By.XPATH,
        "//form//input[@placeholder='Введите Email']/parent::div/parent::div/following-sibling::span[text()='Ошибка']",
    )
    ERROR_FIELD = By.XPATH, "//div[@class='input_inputError__fLUP9']"
    # Кнопка Вход
    SIGNIN_BUTTON = By.XPATH, '//button[text()="Войти"]'
    # Кнопка Выйти
    SIGNOUT_BUTTON = By.XPATH, '//button[text()="Выйти"]'
    # Кнопка Разместить объявление
    NEW_PUBLISH_BUTTON = By.XPATH, '//button[contains(text(), "Разместить")]'
    # Заголовок модалки про авторизация
    POPUP_HEADING = By.CSS_SELECTOR, ".h1"

    # Поля формы создания:
    # Название
    NAME_FIELD = By.XPATH, '//*[@placeholder="Название"]'
    # Описание товара
    DISCPIPTION_FIELD = By.XPATH, '//*[@placeholder="Описание товара"]'
    # Стоимость
    PRICE_FIELD = By.XPATH, '//*[@name="price"]'
    # Категория
    CATEGORIES_MENU_BUTTON = (
        By.XPATH,
        '//input[@name="category"]/following-sibling::button',
    )
    CATEGORIES_ITEM_BUTTON = By.XPATH, "//span[text()='Садоводство']/parent::button"
    # Город
    CITY_MENU_BUTTON = By.XPATH, '//input[@name="city"]/following-sibling::button'
    CITY_ITEM_BUTTON = By.XPATH, "//span[text()='Новосибирск']/parent::button"
    # Состояние товара
    RADIO_BUTTON = By.XPATH, "//label[@class='h2' and text()='Б/У']/parent::div"

    # Кнопка Опубликовать
    PUBLISH_BUTTON = By.XPATH, '//button[text()="Опубликовать"]'

    # Профиль пользователя
    USER_PROFILE_BUTTON = By.XPATH, "//button[@class='circleSmall']"
    # Мои объявления
    MY_ADS = By.XPATH, '//h1[text()="Мои объявления"]'
    NEW_ADS = By.XPATH, '//div[@class="about"]/h2'
