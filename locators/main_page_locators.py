from selenium.webdriver.common.by import By
from data import Order


class MainLocators:

    # локатор кнопки <Войти в аккаунт>
    ENTER_BUTTON = [By.XPATH, './/button[text()="Войти в аккаунт"]']

    # локатор кнопки <Личный кабинет>
    ACCOUNT_BUTTON = [By.XPATH, './/p[text()="Личный Кабинет"]']

    # локатор кнопки <Лента Заказов>
    ORDERS_BUTTON = [By.XPATH, './/p[text()="Лента Заказов"]']

    # локатор ингредиента <Краторная булка>
    INGREDIENT = [By.XPATH, './/img[@alt="' + Order.BUN_NAME + '"]']

    # локатор кнопки <X> закрытия модального окна с ингредиентом
    MODAL_INGREDIENT_X = [By.XPATH, './/section/div/div/ul/../../button/*']

    # локатор модального окна для ингредиента <Краторная булка>
    MODAL_INGREDIENT = [By.XPATH, './/h2[text()="Детали ингредиента"]/../../..']

    # локатор корзины заказа
    BURGER_BASKET = [By.CSS_SELECTOR, '.BurgerConstructor_basket__list__l9dp_']

    # локатор счетчика ингредиента <Краторная булка>
    INGREDIENTS_COUNTER = [By.XPATH, './/a[@href="/ingredient/61c0c5a71d1f82001bdaaa6c"]/div/p[@class="counter_counter__num__3nue1"]']

    # локатор кнопки <Оформить Заказ>
    BUTTON_MAKE_ORDER = [By.XPATH, './/button[text()="Оформить заказ"]']

    # локатор кнопки <Войти в аккаунт>
    BUTTON_ACCOUNT = [By.XPATH, './/button[text()="Войти в аккаунт"]']

    # локатор поля с номером текущего заказа
    N_ORDER = [By.CSS_SELECTOR, '.Modal_modal__title_shadow__3ikwq']

    # локатор тэга с номером последнего заказа в истории заказов
    LAST_ORDERS_N = [By.XPATH, './/div[@class="Account_contentBox__2CPm3"]/div/ul/li[last()]/a/div/p[@class="text text_type_digits-default"]']

    # локатор модального окна текущего заказа
    MODAL_ORDER = [By.XPATH, './/div[@class="Modal_modal__contentBox__sCy8X pt-30 pb-30"]/..']

    # локатор кнопки <X>, закрывающей модальное окно текущего заказа
    MODAL_ORDER_X = [By.XPATH, './/div[@class="Modal_modal__contentBox__sCy8X pt-30 pb-30"]/../button']


