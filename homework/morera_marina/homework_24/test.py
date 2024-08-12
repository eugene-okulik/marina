import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.alert import Alert


@pytest.fixture()
def driver():
    chrome_driver = webdriver.Chrome()
    chrome_driver.maximize_window()
    yield chrome_driver


def test_shop(driver):
    driver.get("https://www.demoblaze.com/index.html")
    link = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, 'card-img-top'))
    )
    ActionChains(driver).key_down(Keys.CONTROL).click(link).key_up(Keys.CONTROL).perform()
    WebDriverWait(driver, 10).until(lambda d: len(d.window_handles) == 2)
    tabs = driver.window_handles
    driver.switch_to.window(tabs[1])
    save = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CLASS_NAME, 'btn-success'))
    )
    save.click()
    text_item = driver.find_element(By.CLASS_NAME, 'name').text
    WebDriverWait(driver, 10).until(EC.alert_is_present())
    alert = Alert(driver)
    alert.accept()
    driver.close()
    driver.switch_to.window(tabs[0])
    driver.find_element(By.ID, 'cartur').click()
    cart_item = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="tbodyid"]/tr/td[2]'))
    )
    assert cart_item.text == text_item


def test_luma(driver):
    driver.get("https://magento.softwaretestingboard.com/gear/bags.html")
    item = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, 'product-image-wrapper'))
    )
    actions = ActionChains(driver)
    actions.move_to_element(item).perform()
    compare = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, 'tocompare'))
    )
    actions.click(compare).perform()
    item_text = driver.find_element(By.CLASS_NAME, 'product-item-link').text
    driver.execute_script("window.scrollTo(0, 500)")
    compare_text = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="compare-items"]/li/strong/a'))
    )
    assert item_text == compare_text.text
