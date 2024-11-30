import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from homework.morera_marina.test_UI_unique_name.pages.shop_luma import ShopLuma
from homework.morera_marina.test_UI_unique_name.pages.sales import Sales
from homework.morera_marina.test_UI_unique_name.pages.customer_login import Customerlogin
from playwright.sync_api import BrowserContext
from time import sleep


@pytest.fixture()
def driver():
    options = Options()
    options.add_argument('--headless')
    chrome_driver = webdriver.Chrome(options=options)
    sleep(3)
    chrome_driver.implicitly_wait(5)
    return chrome_driver


@pytest.fixture()
def page(context: BrowserContext, playwright):
    playwright.selectors.set_test_id_attribute("id")
    page = context.new_page()
    page.set_viewport_size({'width': 1920, 'height': 1080})
    return page


@pytest.fixture()
def shop_luma(page):
    return ShopLuma(page)


@pytest.fixture()
def sales(page):
    return Sales(page)


@pytest.fixture()
def login_page(page):
    return Customerlogin(page)
