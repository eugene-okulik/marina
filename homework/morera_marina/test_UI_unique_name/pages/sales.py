from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC


class Sales:
    def __init__(self, driver):
        self.driver = driver

    def open_page(self):
        self.driver.get('https://magento.softwaretestingboard.com/sale.html')

    def open_women_items(self, women_url):
        shop_women = self.driver.find_element(By.CLASS_NAME, 'more')
        shop_women.click()
        assert self.driver.current_url == women_url

    def open_jackets(self):
        jackets = self.driver.find_element(By.XPATH, '//*[@id="maincontent"]/div[4]/div[2]/div/div/ul[1]/li[2]/a')
        text = jackets.text
        jackets.click()
        title_page = self.driver.find_element(By.CLASS_NAME, 'base')
        assert title_page.text == text

    def add_to_compare_and_delete(self):
        mens = self.driver.find_element(By.CLASS_NAME, 'sale-mens')
        mens.click()
        item = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, 'product-image-wrapper'))
        )
        text = self.driver.find_element(By.CLASS_NAME, 'product-item-link').text
        actions = ActionChains(self.driver)
        actions.move_to_element(item).perform()
        compare = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, 'tocompare'))
        )
        actions.click(compare).perform()
        sale = self.driver.find_element(By.XPATH, '//*[@id="ui-id-8"]/span')
        sale.click()
        compare = self.driver.find_element(By.CLASS_NAME, 'product-item-name')
        text_compare = compare.text

        assert text_compare == text
