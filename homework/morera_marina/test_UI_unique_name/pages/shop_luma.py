from homework.morera_marina.test_UI_unique_name.pages.base_page import BasePage


class ShopLuma(BasePage):
    page_url = '/eco-friendly.html'

    def add_item_to_filter(self):
        new = self.page.locator('//div[@data-role="title" and text()="New"]')
        new.click()
        yes = self.page.locator('//div[@data-role="title" and text()="New"]/following-sibling::'
                                'div[@data-role="content"]//a[contains(text(), "Yes")]')
        yes.click()
        check_count = self.page.locator('.product-image-container').count()
        total = self.page.locator('xpath=//p[@id="toolbar-amount"]/span[@class="toolbar-number"]').nth(1).inner_text()
        number = int(total)

        assert check_count == number

    def add_item_to_compare(self):
        item = self.page.locator('.product-image-wrapper').nth(0)
        item.hover()
        compare = self.page.locator('.tocompare').nth(0)
        compare.wait_for(state='visible', timeout=60000)
        compare.click()
        item_text = self.page.locator('.product-item-link').nth(0).inner_text()
        compare_link = self.page.locator('//ol[@id="compare-items"]//li//strong/a')
        compare_link.wait_for(state='visible', timeout=60000)
        compare_text = compare_link.inner_text()
        assert item_text == compare_text

    def add_item_to_wishlist(self):
        item = self.page.locator('.product-image-wrapper').nth(0)
        item.hover()
        wishlist = self.page.locator('.action.towishlist').nth(0)
        wishlist.click()

    def check_wish_list_message_is(self, expected_text):
        item_text = self.page.locator('.page.messages')
        item_text.wait_for(state='visible', timeout=60000)
        text = item_text.inner_text()
        print('тест найденный', text, "exp", expected_text)
        assert text == expected_text
