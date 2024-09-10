import pytest
from homework.morera_marina.test_UI_unique_name.pages.shop_luma import ShopLuma
from homework.morera_marina.test_UI_unique_name.pages.sales import Sales
from homework.morera_marina.test_UI_unique_name.pages.customer_login import Customerlogin


@pytest.fixture()
def shop_luma(page):
    return ShopLuma(page)


@pytest.fixture()
def sales(page):
    return Sales(page)


@pytest.fixture()
def login_page(page):
    return Customerlogin(page)
