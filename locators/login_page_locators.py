from selenium.webdriver.common.by import By

class LoginLocators:

    # локатор поля для ввода <Email>
    EMAIL_FIELD = [By.XPATH, './/input[@name="name"]']

    # локатор поля для ввода <Пароль>
    PASSWORD_FIELD = [By.XPATH, './/input[@name="Пароль"]']

    # локатор кнопки <Войти>
    ENTER_BUTTON = [By.XPATH, './/button[text()="Войти"]']

    # локатор надписи со ссылкой <Восстановить пароль>
    FORGOT_PASS = [By.XPATH, './/a[text()="Восстановить пароль"]']

    # локатор оверлеев для файрфокс
    OVERLAY = [By.XPATH, './/*[@class="Modal_modal_overlay__x2ZCr"]']

    # локатор главного оверлея для файрфокс
    OVERLAY_1 = [By.XPATH, './/div/div[@class="Modal_modal_overlay__x2ZCr"]']

    # локатор кнопки «Личный кабинет»
    ACCOUNT_BUTTON = [By.XPATH, './/p[text()="Личный Кабинет"]']
