from homework.morera_marina.test_UI_unique_name.pages.base_page import BasePage
from homework.morera_marina.test_UI_unique_name.locators.locators import Locators


class Sales(BasePage):
    page_url = '/sale.html'

    def open_women_items(self, women_url):
        shop_women = self.page.locator(Locators.TEXT_WOMEN_DEALS)
        shop_women.click()
        assert self.page.url == women_url

    def open_jackets(self):
        jackets = self.page.locator(Locators.TEXT_JACKETS).nth(2)
        text = jackets.inner_text()
        jackets.click()
        return text

    def check_jackets_title(self, expected_text):
        title_element = self.page.locator(Locators.TITLE_BASE)
        assert title_element.inner_text() == expected_text

    def add_to_compare(self):
        mens = self.page.locator(Locators.SALE_MENS)
        mens.click()
        item = self.page.locator(Locators.PRODUCT_IMAGE_WRAPPER).nth(0)
        item_text = self.page.locator(Locators.PRODUCT_ITEM_LINK).nth(0).inner_text()
        item.hover()
        compare = self.page.locator(Locators.COMPARE_BUTTON).nth(0)
        compare.click()
        return item_text

    def delete_from_compare(self, item_text):
        sale = self.page.locator(Locators.SALE).nth(0)
        sale.click()
        compare = self.page.locator(Locators.PRODUCT_ITEM_NAME).nth(0)
        compare.wait_for()
        text_compare = compare.inner_text()
        assert text_compare == item_text
