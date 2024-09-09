import pytest
from pages.shop_luma import ShopLuma
from pages.sales import Sales
from pages.customer_login import Customerlogin


@pytest.fixture()
def shop_luma(driver):
    return ShopLuma(driver)


@pytest.fixture()
def sales(driver):
    return Sales(driver)


@pytest.fixture()
def login_page(driver):
    return Customerlogin(driver)
