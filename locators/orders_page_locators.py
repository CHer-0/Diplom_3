from selenium.webdriver.common.by import By


class OrdersLocators:

    # локатор последнего заказа с номером
    ORDER_N = [By.XPATH, './/p[text()="{}"]']
