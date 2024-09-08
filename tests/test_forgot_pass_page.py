import allure
from links import Urls


# класс с автотестом
class TestForgotPass:

    @allure.title('Проверка перехода по кнопке <Восстановить>')
    def test_restore_button(self, forgot_pass_page):
        forgot_pass_page.click_restore()

        assert forgot_pass_page.get_url_wait(Urls.URL_RESET_PASS) == Urls.URL_RESET_PASS
