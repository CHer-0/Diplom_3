import allure
from links import Urls


# класс с автотестом
class TestLoginPage:

    @allure.title('Проверка перехода по надписи со ссылкой <Восстановить пароль>')
    def test_forgot_pass_button(self, login_page):
        login_page.click_forgot_pass()

        assert login_page.get_url_wait(Urls.URL_FORGOT_PASS) == Urls.URL_FORGOT_PASS

    @allure.title('Проверка перехода в <личный кабинет> под действующей учетной записью пользователя')
    def test_account(self, login_page):
        login_page.set_account_and_enter()

        assert login_page.get_url_wait(Urls.URL_ACCOUNT) == Urls.URL_ACCOUNT
