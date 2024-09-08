import allure
from links import Urls
from locators.feed_page_locators import FeedLocators
from data import Modal


# класс с автотестом
class TestFeedPage:

    @allure.title('Проверка перехода с ленты заказов по кнопке <Конструктор>')
    def test_constructor(self, feed_page):
        feed_page.click_constructor()

        assert feed_page.get_url_wait(Urls.URL_MAIN) == Urls.URL_MAIN

    @allure.title('Проверка, что у заказа с ленты заказов есть модальное окно с дополнительной информацией')
    def test_order_modal(self, feed_page):
        feed_page.click_last_order()
        modal_status = feed_page.get_attribute(FeedLocators.MODAL_ORDER, 'class')

        assert modal_status == Modal.CLASS_OPENED
