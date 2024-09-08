import allure
from links import Urls
from data import Modal, Order


# класс с автотестом
class TestMainPage:

    @allure.title('Проверка неавторизованного перехода с главной формы по кнопке <личный кабинет>')
    def test_account_button(self, main_page):
        main_page.click_account()

        assert main_page.get_url_wait(Urls.URL_LOGIN) == Urls.URL_LOGIN

    @allure.title('Проверка перехода с главной формы по кнопке <Лента Заказов>')
    def test_feed_button(self, main_page):
        main_page.click_orders()

        assert main_page.get_url_wait(Urls.URL_FEED) == Urls.URL_FEED

    @allure.title('Проверка если нажать ингредиент, появится дополнительная информация  в модальном окне')
    def test_modal_ingredient(self, main_page):
        main_page.click_ingredient()

        assert main_page.get_status_modal() == Modal.CLASS_OPENED

    @allure.title('Проверка если нажать крестик при просмотре дополнительной информации, модальное окно закроется')
    def test_modal_ingredient_x(self, main_page):
        main_page.click_ingredient()
        main_page.click_x()
        status_modal = main_page.get_status_modal()

        assert status_modal == Modal.CLASS_CLOSED

    @allure.title('Проверка если перетащить ингредиент (булку) в корзину, его счетчик увеличится (на 2)')
    def test_ingredient_counter(self, main_page):
        counter_start = main_page.get_counter()
        main_page.add_ingredient_to_basket()
        counter_end = main_page.get_counter()

        assert int(counter_end) - int(counter_start) == 2

    @allure.title('Проверка что оформленный заказ отображается в истории заказов и в ленте заказов')
    def test_current_order_in_the_feed(self, main_page):
        main_page.authorize()
        main_page.make_order()
        num_1 = main_page.get_current_orders_num()
        main_page.go_orders_history()
        num_2 = main_page.get_last_history_orders_num()
        main_page.click_orders()
        main_page.scroll_to_last_order(num_2)
        name_last_burger = main_page.get_name_from_last_order(num_2)
        expected_name = Order.BURGER_NAME

        assert "#0" + str(num_1) == num_2 and name_last_burger == expected_name

    @allure.title('Проверка что авторизованному пользователю доступно оформление заказа')
    def test_authorized_make_order(self, main_page):
        main_page.authorize()

        assert main_page.button_make_order_is_visible()

    @allure.title('Проверка что в ленте заказов появляется № текущего заказа в поле <В работе> и счетчики заказов увеличились')
    def test_current_order_in_the_work(self, main_page):
        main_page.authorize()
        main_page.click_orders()
        total_cnt_start = main_page.get_total_orders_count()
        today_cnt_start = main_page.get_today_orders_count()
        main_page.wait_ready_to_work()
        main_page.click_constructor()
        main_page.make_order()
        num = main_page.get_current_orders_num()
        main_page.click_orders()
        n_order_in_work = main_page.get_orders_in_work()
        total_cnt_end = main_page.get_total_orders_count()
        today_cnt_end = main_page.get_today_orders_count()

        assert n_order_in_work == '0' + num and total_cnt_end > total_cnt_start and today_cnt_end > today_cnt_start
