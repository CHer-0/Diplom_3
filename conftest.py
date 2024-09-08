import pytest

from selenium import webdriver
from selenium.webdriver import Firefox, FirefoxOptions
from selenium.webdriver.chrome.options import Options

from links import Urls

from pages.main_page import MainPage
from pages.login_page import LoginPage
from pages.reset_pass_page import ResetPassPage
from pages.forgot_pass_page import ForgotPassPage
from pages.account_page import AccountPage
from pages.feed_page import FeedPage


@pytest.fixture(params=['firefox', 'chrome'])
def driver(request):
    if request.param == 'firefox':
        options = FirefoxOptions()
        options.add_argument("--window-size=1920,1080")
        driver = Firefox(options=options)
    else:
        options = Options()
        options.add_argument('--window-size=1920,1080')
        driver = webdriver.Chrome(options=options)
    driver.get(Urls.URL_LOGIN)
    yield driver
    driver.quit()


@pytest.fixture()
def main_page(driver):
    page = MainPage(driver)
    page.driver.get(Urls.URL_MAIN)
    page.dem_overlay()
    return page


@pytest.fixture()
def login_page(driver):
    page = LoginPage(driver)
    page.dem_overlay()
    return page


@pytest.fixture()
def forgot_pass_page(driver):
    page = ForgotPassPage(driver)
    page.driver.get(Urls.URL_FORGOT_PASS)
    page.dem_overlay()
    return page


@pytest.fixture()
def reset_pass_page(driver):
    page = ResetPassPage(driver)
    page.driver.get(Urls.URL_RESET_PASS)
    page.dem_overlay()
    return page


@pytest.fixture()
def account_page(driver):
    page = AccountPage(driver)
    page.driver.get(Urls.URL_LOGIN)
    page.dem_overlay()
    return page


@pytest.fixture()
def feed_page(driver):
    page = FeedPage(driver)
    page.driver.get(Urls.URL_FEED)
    page.dem_overlay()
    return page
