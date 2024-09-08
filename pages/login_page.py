import allure
from pages.base_page import BasePage
from locators.login_page_locators import LoginLocators
from data import Account


class LoginPage(BasePage):

    @allure.step('Нажимаем кнопку <Восстановить пароль> на странице логина')
    def click_forgot_pass(self):
        self.click_on_element(LoginLocators.FORGOT_PASS)
        self.dem_overlay()

    @allure.step('Заполняем Email и пароль и нажимаем кнопку <Войти> на странице логина')
    def set_account_and_enter(self):
        self.set_text_to_element(LoginLocators.EMAIL_FIELD, Account.EMAIL)
        self.set_text_to_element(LoginLocators.PASSWORD_FIELD, Account.PASS)
        self.click_on_element(LoginLocators.ENTER_BUTTON)
        self.dem_overlay()
        self.click_on_element(LoginLocators.ACCOUNT_BUTTON)
        self.dem_overlay()
