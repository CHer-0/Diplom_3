from selenium.webdriver.common.by import By


class FeedLocators:
    # локатор кнопки <Конструктор>
    CONSTRUCTOR = [By.XPATH, './/p[text()="Конструктор"]']

    # локатор последнего заказа в
    LAST_ORDER = [By.XPATH, './/ul[@class ="OrderFeed_list__OLh59"]/li[1]']

    # локатор модального окна
    MODAL_ORDER = [By.XPATH, './/div[@class="Modal_orderBox__1xWdi Modal_modal__contentBox__sCy8X p-10"]/../..']

    # локатор названия бургера в заказе с определенным номером в ленте заказов
    ORDER_FEED_NAME_N = [By.XPATH, './/p[text()="{}"]/../../h2']

    # локатор поля, какие номера заказов в работе
    ORDER_IN_WORK_N = ([By.XPATH,
                        './/ul[@class="OrderFeed_orderListReady__1YFem OrderFeed_orderList__cBvyi"]/li[1]'])

    # локатор поля с общим счетчиком заказов за все время
    TOTAL_ORDERS = ([By.XPATH,
                     './/p[text()="Выполнено за все время:"]/../p[@class="OrderFeed_number__2MbrQ text text_type_digits-large"]'])

    # локатор поля со счетчиком заказов за сегодня
    TODAY_ORDERS = ([By.XPATH,
                     './/p[text()="Выполнено за сегодня:"]/../p[@class="OrderFeed_number__2MbrQ text text_type_digits-large"]'])
