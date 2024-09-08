from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class ResetPassLocators:


    # локатор поля для ввода <Введите новый пароль>
    NEW_PASS_FIELD = [By.XPATH, './/input[@name="Введите новый пароль"]']

    # локатор кнопки с глазом на поле для ввода нового пароля
    EYE_BUTTON = [By.XPATH, './/div[@class="input__icon input__icon-action"]']
