from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class ForgotPassLocators:

    # локатор поля для ввода <Email>
    EMAIL_FIELD = [By.XPATH, './/input[@name="name"]']

    # локатор кнопки <Войти>
    ENTER_LINK = [By.XPATH, './/a[text()="Войти"]']

    # локатор надписи со ссылкой <Восстановить пароль>
    RESTORE_BUTTON = [By.XPATH, './/button[text()="Восстановить"]']

    # локатор поля для ввода <Введите новый пароль>
    NEW_PASS_FIELD = [By.XPATH, './/input[@name="Введите новый пароль"]']

    # локатор кнопки с глазом на поле для ввода нового пароля
    EYE_BUTTON = [By.XPATH, './/div/svg[@fill="#F2F2F3"]/path']

    # локатор оверлея для файрфокс
    OVERLAY_1 = [By.XPATH, './/div/div[@class="Modal_modal_overlay__x2ZCr"]']

    # локатор оверлея для файрфокс
    OVERLAY_2 = [By.XPATH, './/section/div[@class="Modal_modal_overlay__x2ZCr"]']

