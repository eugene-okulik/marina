import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from homework.morera_marina.test_UI_unique_name.pages.shop_luma import ShopLuma
from homework.morera_marina.test_UI_unique_name.pages.sales import Sales
from homework.morera_marina.test_UI_unique_name.pages.customer_login import Customerlogin
from playwright.sync_api import sync_playwright
from time import sleep


@pytest.fixture()
def selenium_driver():
    options = Options()
    options.add_argument('--headless')
    chrome_driver = webdriver.Chrome(options=options)
    sleep(3)
    chrome_driver.implicitly_wait(5)
    return chrome_driver


@pytest.fixture()
def playwright_context_and_page():
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=True)
        context = browser.new_context()
        page = context.new_page()
        page.set_viewport_size({'width': 1920, 'height': 1080})
        yield page
        browser.close()


@pytest.fixture()
def shop_luma(playwright_context_and_page):
    return ShopLuma(playwright_context_and_page)


@pytest.fixture()
def sales(playwright_context_and_page):
    return Sales(playwright_context_and_page)


@pytest.fixture()
def login_page(playwright_context_and_page):
    return Customerlogin(playwright_context_and_page)
