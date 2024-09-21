from homework.morera_marina.test_UI_unique_name.pages.base_page import BasePage
from homework.morera_marina.test_UI_unique_name.locators.locators import Locators


class ShopLuma(BasePage):
    page_url = '/promotions/pants-all.html'

    def select_new_in_filter(self):
        new = self.page.locator(Locators.TITLE_NEW)
        new.click()
        yes = self.page.locator(Locators.TITLE_YES)
        yes.click()

    def check_total_number_in_filter(self):
        check_count = self.page.locator(Locators.PRODUCT_IMAGE_CONTAINER).count()
        total = self.page.locator(Locators.TOTAL_NUMBER).nth(1).inner_text()
        number = int(total)
        assert check_count == number

    def add_item(self):
        item = self.page.locator(Locators.PRODUCT_IMAGE_WRAPPER).nth(0)
        item.hover()
        compare = self.page.locator(Locators.COMPARE_BUTTON).nth(0)
        compare.wait_for(state='visible', timeout=60000)
        compare.click()

    def compare_item(self):
        item_text = self.page.locator(Locators.PRODUCT_ITEM_LINK).nth(0).inner_text()
        compare_link = self.page.locator(Locators.COMPARE_ITEM_LINK)
        compare_link.wait_for(state='visible', timeout=60000)
        compare_text = compare_link.inner_text()
        assert item_text == compare_text

    def add_item_to_wishlist(self):
        item = self.page.locator(Locators.PRODUCT_IMAGE_WRAPPER).nth(0)
        item.hover()
        wishlist = self.page.locator(Locators.ADD_TO_WISHLIST).nth(0)
        wishlist.click()

    def check_wish_list_message_is(self, expected_text):
        item_text = self.page.locator('.page.messages')
        item_text.wait_for(state='visible', timeout=60000)
        text = item_text.inner_text()
        print('тест найденный', text, "exp", expected_text)
        assert text == expected_text
