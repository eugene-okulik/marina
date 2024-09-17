from homework.morera_marina.test_UI_unique_name.pages.base_page import BasePage


class Sales(BasePage):
    page_url = '/sale.html'

    def open_women_items(self, women_url):
        shop_women = self.page.locator('text="Shop Women’s Deals"')
        shop_women.click()
        assert self.page.url == women_url

    def open_jackets(self):
        jackets = self.page.locator('text="Jackets"').nth(2)
        text = jackets.inner_text()
        jackets.click()
        title_element = self.page.locator('.base')
        assert title_element.inner_text() == text

    def add_to_compare_and_delete(self):
        mens = self.page.locator('.sale-mens')
        mens.click()
        item = self.page.locator('.product-image-wrapper').nth(0)
        text = self.page.locator('.product-item-link').nth(0).inner_text()
        item.hover()
        compare = self.page.locator('.tocompare').nth(0)
        compare.click()
        sale = self.page.locator('#ui-id-8 span').nth(0)
        sale.click()
        compare = self.page.locator('.product-item-name').nth(0)
        compare.wait_for()
        text_compare = compare.inner_text()
        assert text_compare == text
