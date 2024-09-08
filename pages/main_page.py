import allure
from pages.base_page import BasePage
from locators.main_page_locators import MainLocators
from locators.login_page_locators import LoginLocators
from locators.account_page_locators import AccountLocators
from locators.orders_page_locators import OrdersLocators
from locators.feed_page_locators import FeedLocators
from data import Account


class MainPage(BasePage):

    @allure.step('Нажимаем кнопку "Личный кабинет" в верхнем углу главной страницы')
    def click_account(self):
        self.dem_overlay()
        self.scroll_to(MainLocators.ACCOUNT_BUTTON)
        self.dem_overlay()
        self.click_on_element(MainLocators.ACCOUNT_BUTTON)
        self.dem_overlay()

    @allure.step('Нажимаем кнопку <Лента заказов> в верху главной страницы')
    def click_orders(self):
        self.dem_overlay()
        self.click_on_element(MainLocators.ORDERS_BUTTON)

    @allure.step('Нажимаем на ингредиент "Краторная булка N-200i" на главной странице')
    def click_ingredient(self):
        self.click_on_element(MainLocators.INGREDIENT)

    @allure.step('Нажимаем на ингредиент на главной странице и закрываем окошко, нажав на крестик <X>')
    def click_x(self):
        self.click_on_element(MainLocators.MODAL_INGREDIENT_X)

    @allure.step('Получаем статус модального окна с информацией об ингредиенте')
    def get_status_modal(self):
        status = self.get_attribute(MainLocators.MODAL_INGREDIENT, 'class')
        return status

    @allure.step('Перетаскиваем ингредиент в корзину заказа')
    def add_ingredient_to_basket(self):
        self.drag_drop_element(MainLocators.INGREDIENT, MainLocators.BURGER_BASKET)

    @allure.step('Получаем количество добавленных ингредиентов')
    def get_counter(self):
        return self.get_text_from_element(MainLocators.INGREDIENTS_COUNTER)

    @allure.step('Авторизуемся под заранее созданным тестовым пользователем')
    def authorize(self):
        self.click_on_element(MainLocators.BUTTON_ACCOUNT)
        self.dem_overlay()
        self.set_text_to_element(LoginLocators.EMAIL_FIELD, Account.EMAIL)
        self.set_text_to_element(LoginLocators.PASSWORD_FIELD, Account.PASS)
        self.click_on_element(LoginLocators.ENTER_BUTTON)
        self.dem_overlay()

    @allure.step('Проверяем, что кнопка <Оформить Заказ> выводится на экран')
    def button_make_order_is_visible(self):
        elt = self.find_element_and_wait(MainLocators.BUTTON_MAKE_ORDER)
        return elt.is_displayed

    @allure.step('Добавляем ингредиент для тестового бургера в корзину и нажимаем кнопку <Оформить Заказ>')
    def make_order(self):
        self.add_ingredient_to_basket()
        self.click_on_element(MainLocators.BUTTON_MAKE_ORDER)

    @allure.step('Ждем, пока в модальном окне текущего заказа 9999 сменится на № текущего заказа, передаем его в тест и закрываем модальное окно')
    def get_current_orders_num(self):
        self.find_element_and_wait(MainLocators.MODAL_ORDER)
        self.dem_overlay_1()
        self.find_no_element_text_wait(MainLocators.N_ORDER, '9999')
        num = self.get_text_from_element(MainLocators.N_ORDER)
        self.click_on_element(MainLocators.MODAL_ORDER_X)
        self.dem_overlay()
        return num

    @allure.step('Переходим в Личный кабинет, а затем - в историю заказов')
    def go_orders_history(self):
        self.dem_overlay()
        self.click_account()
        self.dem_overlay()
        self.click_on_element(AccountLocators.ORDERS_LINK)
        self.dem_overlay()

    @allure.step('Получаем № последнего заказа в истории своих заказов')
    def get_last_history_orders_num(self):
        return self.get_text_from_element(MainLocators.LAST_ORDERS_N)

    @allure.step('Переходим к последнему заказу в истории своих заказов')
    def scroll_to_last_order(self, num):
        last_order_locator = self.format_locator(OrdersLocators.ORDER_N, num)
        self.scroll_to(last_order_locator)

    @allure.step('Получаем название бургера из последнего своего заказа в ленте заказов')
    def get_name_from_last_order(self, num):
        locator_order_feed_n = self.format_locator(FeedLocators.ORDER_FEED_NAME_N, num)
        return self.get_text_from_element(locator_order_feed_n)

    @allure.step('Получаем значение общего счетчика заказов')
    def get_total_orders_count(self):
        return self.get_text_from_element(FeedLocators.TOTAL_ORDERS)

    @allure.step('Получаем значение сегодняшнего счетчика заказов')
    def get_today_orders_count(self):
        return self.get_text_from_element(FeedLocators.TODAY_ORDERS)

    @allure.step('Ждем пока работа с текущими заказами закончится и статус поля <В работе> станет <Все текущие заказы готовы!>')
    def wait_ready_to_work(self):
        self.find_element_and_wait(FeedLocators.ORDER_IN_WORK_N)
        self.find_element_text_wait(FeedLocators.ORDER_IN_WORK_N, 'Все текущие заказы готовы!')

    @allure.step('Переходим по кнопке <Конструктор>')
    def click_constructor(self):
        self.click_on_element(FeedLocators.CONSTRUCTOR)
        self.dem_overlay()

    @allure.step('Получаем статус поля <В работе> с номером текущего заказа')
    def get_orders_in_work(self):
        self.find_element_and_wait(FeedLocators.ORDER_IN_WORK_N)
        self.find_no_element_text_wait(FeedLocators.ORDER_IN_WORK_N, 'Все текущие заказы готовы!')
        return self.get_text_from_element(FeedLocators.ORDER_IN_WORK_N)
