from playwright.sync_api import Page
from time import sleep


class ShopLuma:
    def __init__(self, page:Page):
        self.page = page

    def open_page(self):
        self.page.goto('https://magento.softwaretestingboard.com/collections/eco-friendly.html')

    def add_item_to_filter(self):
        new = self.page.locator('//div[@data-role="title" and text()="New"]')
        new.click()
        yes = self.page.locator('//div[@data-role="title" and text()="New"]/following-sibling::div[@data-role="content"]//a[contains(text(), "Yes")]')
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

        compare_text = self.page.locator('//*[@id="compare-items"]/li/strong/a').inner_text()
        print('text', compare_text, 'text 2', item_text)
        sleep(5)
        assert item_text == compare_text

    def add_item_to_wishlist(self):
        item = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, 'product-image-wrapper'))
        )
        actions = ActionChains(self.driver)
        actions.move_to_element(item).perform()
        wishlist = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, 'towishlist'))
        )
        actions.click(wishlist).perform()

    def check_wish_list_message_is(self, expected_text):
        item_text = self.driver.find_element(By.CLASS_NAME, 'messages').text
        assert item_text == expected_text
