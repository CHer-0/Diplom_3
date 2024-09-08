import allure
from pages.base_page import BasePage
from locators.reset_pass_page_locators import ResetPassLocators
from locators.forgot_pass_page_locators import ForgotPassLocators
from data import Account


class ResetPassPage(BasePage):

    @allure.step('Нажимаем кнопку с глазом на странице смены пароля')
    def click_eye(self):
        self.click_on_element(ResetPassLocators.EYE_BUTTON)

    @allure.step('Возвращаем тэг <type> поля пароля')
    def type_pass(self):
        return self.get_attribute(ResetPassLocators.NEW_PASS_FIELD, 'type')

    @allure.step('Предварительный шаг для входа на страницу смены пароля-вводим Email на странице восстановления пароля')
    def prepare_reset_pass(self):
        self.set_text_to_element(ForgotPassLocators.EMAIL_FIELD, Account.EMAIL)
        self.click_on_element(ForgotPassLocators.RESTORE_BUTTON)
        self.dem_overlay()

    @allure.step('Передадим в поле ввода нового пароля тестовое значение на странице смены пароля')
    def set_new_pass(self):
        self.set_text_to_element(ForgotPassLocators.NEW_PASS_FIELD, Account.PASS)
