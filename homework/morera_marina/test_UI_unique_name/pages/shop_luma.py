from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains


class ShopLuma:
    def __init__(self, driver):
        self.driver = driver

    def open_page(self):
        self.driver.get('https://magento.softwaretestingboard.com/collections/eco-friendly.html')

    def add_item_to_filter(self):
        new = self.driver.find_element(By.XPATH, '//*[@id="narrow-by-list"]/div[9]')
        new.click()
        yes = self.driver.find_element(By.XPATH, '//*[@id="narrow-by-list"]/div[9]/div[2]/ol/li[1]/a')
        yes.click()
        check_count = len(self.driver.find_elements(By.CLASS_NAME, 'product-image-container'))
        total = (self.driver.find_element(By.ID, 'toolbar-amount')).text
        number = int(total.split()[0])
        assert check_count == number

    def add_item_to_compare(self):
        item = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, 'product-image-wrapper'))
        )
        actions = ActionChains(self.driver)
        actions.move_to_element(item).perform()
        compare = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, 'tocompare'))
        )
        actions.click(compare).perform()
        item_text = self.driver.find_element(By.CLASS_NAME, 'product-item-link').text
        self.driver.execute_script("window.scrollTo(0, 500)")
        compare_text = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="compare-items"]/li/strong/a'))
        )
        assert item_text == compare_text.text

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
