import allure
from links import Urls


# класс с автотестом
class TestAccountPage:

    @allure.title('Проверка перехода с личного кабинета по ссылке <история заказов>')
    def test_order_history(self, account_page):
        account_page.prepare_account()
        account_page.click_order_history()

        assert account_page.get_url_wait(Urls.URL_ORDERS) == Urls.URL_ORDERS

    @allure.title('Проверка перехода с личного кабинета по кнопке <выход>')
    def test_exit_account(self, account_page):
        account_page.prepare_account()
        account_page.click_exit_button()

        assert account_page.get_url_wait(Urls.URL_LOGIN) == Urls.URL_LOGIN
