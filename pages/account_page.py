import allure
from pages.base_page import BasePage
from locators.account_page_locators import AccountLocators
from locators.login_page_locators import LoginLocators
from data import Account


class AccountPage(BasePage):

    @allure.step('Нажимаем кнопку <История заказов> на странице личного кабинета')
    def click_order_history(self):
        self.dem_overlay()
        self.click_on_element(AccountLocators.ORDERS_LINK)

    @allure.step('Нажимаем кнопку <Выход> на странице личного кабинета')
    def click_exit_button(self):
        self.dem_overlay()
        self.click_on_element(AccountLocators.EXIT_BUTTON)

    def prepare_account(self):
        self.set_text_to_element(LoginLocators.EMAIL_FIELD, Account.EMAIL)
        self.set_text_to_element(LoginLocators.PASSWORD_FIELD, Account.PASS)
        self.click_on_element(LoginLocators.ENTER_BUTTON)
        self.dem_overlay()
        self.click_on_element(LoginLocators.ACCOUNT_BUTTON)
        self.dem_overlay()
