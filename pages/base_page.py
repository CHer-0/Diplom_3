from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from locators.login_page_locators import LoginLocators


class BasePage:
    timeout = 30

    def __init__(self, driver):
        self.driver = driver

    def find_element_and_wait(self, locator):
        WebDriverWait(self.driver, self.timeout).until(expected_conditions.visibility_of_element_located(locator))
        return self.driver.find_element(*locator)

    def find_element_wait(self, locator):
        WebDriverWait(self.driver, self.timeout).until(expected_conditions.element_to_be_clickable(locator))
        return self.driver.find_element(*locator)

    def find_no_element_text_wait(self, locator, text):
        WebDriverWait(self.driver, self.timeout).until_not(
            expected_conditions.text_to_be_present_in_element(locator, text))

    def find_element_text_wait(self, locator, text):
        WebDriverWait(self.driver, self.timeout).until(expected_conditions.text_to_be_present_in_element(locator, text))

    def click_on_element(self, locator):
        self.find_element_wait(locator).click()

    def get_text_from_element(self, locator):
        elt = self.find_element_and_wait(locator)
        return elt.text

    def set_text_to_element(self, locator, text):
        elt = self.find_element_and_wait(locator)
        elt.send_keys(text)

    @staticmethod
    def format_locator(locator, n):
        method, locator1 = locator
        locator2 = locator1.format(n)
        return method, locator2

    def get_url_wait(self, url):
        WebDriverWait(self.driver, self.timeout).until(expected_conditions.url_to_be(url))
        return self.driver.current_url

    def get_attribute(self, locator, attribute):
        elt = self.find_element_and_wait(locator)
        return elt.get_attribute(attribute)

    def drag_drop_element(self, elt_from, elt_to):
        from_elt = self.find_element_wait(elt_from)
        to_elt = self.find_element_wait(elt_to)
        f = open("scripts/drag_and_drop.js", "r")
        javascript = f.read()
        f.close()
        self.driver.execute_script(javascript, from_elt, to_elt)

    def dem_overlay(self):
        if self.driver.name == 'firefox':
            locator = LoginLocators.OVERLAY
            list_overlay = self.driver.find_elements(*locator)
            for elt in list_overlay:
                WebDriverWait(self.driver, self.timeout).until_not(expected_conditions.visibility_of(elt))

    def dem_overlay_1(self):
        if self.driver.name == 'firefox':
            locator = LoginLocators.OVERLAY_1
            elt = self.driver.find_element(*locator)
            WebDriverWait(self.driver, self.timeout).until_not(expected_conditions.visibility_of(elt))

    def scroll_to(self, locator):
        elt = self.find_element_and_wait(locator)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", elt)
