import allure
from pages.base_page import BasePage
from locators.forgot_pass_page_locators import ForgotPassLocators
from data import Account


class ForgotPassPage(BasePage):

    @allure.step('Вводим Email и нажимаем кнопку <Восстановить> на странице восстановления пароля')
    def click_restore(self):
        self.set_text_to_element(ForgotPassLocators.EMAIL_FIELD, Account.EMAIL)
        self.click_on_element(ForgotPassLocators.RESTORE_BUTTON)
