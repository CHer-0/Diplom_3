from selenium.webdriver.common.by import By


class AccountLocators:

    # локатор поля для ввода <Имя>
    EMAIL_FIELD = [By.XPATH, './/input[@name="name"]']

    # локатор поля для ввода <Пароль>
    PASSWORD_FIELD = [By.XPATH, './/input[@name="Пароль"]']

    # локатор кнопки <Выход>
    EXIT_BUTTON = [By.XPATH, './/button[text()="Выход"]']

    # локатор надписи со ссылкой <История заказов>
    ORDERS_LINK = [By.XPATH, './/a[text()="История заказов"]']
