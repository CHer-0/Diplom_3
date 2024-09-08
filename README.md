## Дипломный проект. Задание 3: UI-тесты

### Автотесты для проверки графического интерфейса сайта для заказа бургера в Stellar Burgers

### Реализованные сценарии

Созданы UI-тесты, покрывающие страницы page-object модели `account_page`, `base_page`, `feed_page`, `forgot_pass_page`, `login_page`, `main_page`, `reset_pass_page`

Отчет создан в allure-pytest. Тесты в Chrome выполнились на 100% (отчет: `allure_results/`)

### Структура проекта

- `pages` - пакет, содержащий методы, разделенные по классам модели page-object:
	`account_page`, 
	`base_page`, 
	`feed_page`, 
	`forgot_pass_page`, 
	`login_page`, 
	`main_page`, 
	`reset_pass_page`.
- `locators` - пакет, содержащий локаторы элементов, используемых при тестировании, разделенные по классам модели page-object:
	`account_page_locators`, 
	`feed_page_locators`, 
	`forgot_pass_page_locators`, 
	`login_page_locators`, 
	`main_page_locators`, 
	`orders_page_locators`, 
	`reset_pass_page_locators`.
- `tests` - пакет, содержащий тесты, разделенные по классам модели page-object:
	`test_account_page`, 
	`test_feed_page`, 
	`test_forgot_pass_page`, 
	`test_login_page`, 
	`test_main_page`, 
	`test_reset_pass_page`.
- `scripts` - пакет, содержащий js-скрипт для реализации метода `drag&drop`, работающего в обоих тестовых браузерах (Chrome и Firefox)
- links.py - файл, содержащий ссылки всех тестируемых страниц Stellar Burgers
- data.py -  файл, содержащий тестовые данные
- conftest.py - файл, содержащий необходимые для автотестов фикстуры
### Запуск автотестов

**Установка зависимостей**

> `$ pip install -r requirements.txt`

**Запуск автотестов и создание allure-отчета**

>  `$ allure serve allure_results `

# UI-тесты, разделенные по классам:

  # Класс TestAccountPage:

    # Проверка перехода с личного кабинета по ссылке <история заказов>
    test_order_history

    # Проверка перехода с личного кабинета по кнопке <выход>
    test_exit_account

  # Класс TestFeedPage:

    # Проверка перехода с ленты заказов по кнопке <Конструктор>
    test_constructor

    # Проверка, что у заказа с ленты заказов есть модальное окно с дополнительной информацией
    test_order_modal
	
  # Класс TestForgotPass:

    # Проверка перехода по кнопке <Восстановить>
    test_restore_button
	
  # Класс TestLoginPage:

    # Проверка перехода по надписи со ссылкой <Восстановить пароль>
    test_forgot_pass_button

    # Проверка перехода в <личный кабинет> под действующей учетной записью пользователя
    test_account
	
  # Класс TestMainPage:

    # Проверка неавторизованного перехода с главной формы по кнопке <личный кабинет>
    test_account_button

    # Проверка перехода с главной формы по кнопке <Лента Заказов>
    test_feed_button

    # Проверка если нажать ингредиент, появится дополнительная информация  в модальном окне
    test_modal_ingredient

    # Проверка если нажать крестик при просмотре дополнительной информации, модальное окно закроется
    test_modal_ingredient_x

    # Проверка если перетащить ингредиент (булку) в корзину, его счетчик увеличится (на 2)
    test_ingredient_counter

    # Проверка что оформленный заказ отображается в истории заказов и в ленте заказов
    test_current_order_in_the_feed

    # Проверка что авторизованному пользователю доступно оформление заказа
    test_authorized_make_order

    # Проверка что в ленте заказов появляется № текущего заказа в поле <В работе> и счетчики заказов увеличились
    test_current_order_in_the_work

  # Класс TestResetPass:

    # Проверка, что клик по кнопке показать/скрыть пароль делает поле активным — подсвечивает его
    test_eye_button