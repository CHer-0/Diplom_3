import allure
from pages.base_page import BasePage
from locators.feed_page_locators import FeedLocators


class FeedPage(BasePage):

    @allure.step('Нажимаем кнопку <Конструктор> на странице с лентой заказов')
    def click_constructor(self):
        self.click_on_element(FeedLocators.CONSTRUCTOR)
        self.dem_overlay()

    @allure.step('Нажимаем на последний заказ на странице с лентой заказов')
    def click_last_order(self):
        self.click_on_element(FeedLocators.LAST_ORDER)
