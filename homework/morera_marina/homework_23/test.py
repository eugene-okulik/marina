from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import pytest
from time import sleep


@pytest.fixture()
def driver():
    chrome_driver = webdriver.Chrome()
    sleep(3)
    chrome_driver.maximize_window()
    yield chrome_driver
    sleep(3)


def test_name(driver):
    input_data = 'cat'
    driver.get('https://www.qa-practice.com/elements/input/simple')
    search_input = driver.find_element(By.NAME, 'text_string')
    search_input.send_keys(input_data)
    search_input.send_keys(Keys.ENTER)
    sleep(3)
    result_text = driver.find_element(By.ID, 'result-text')
    assert result_text.text == input_data


def test_form(driver):
    first_name = 'Marina'
    last_name = "Mar"
    email_field = 'name@test.com'
    mobile = '3243565342'
    subjects = 'python'
    address = 'russia'
    driver.get('https://demoqa.com/automation-practice-form')
    name = driver.find_element(By.ID, 'firstName')
    name.send_keys(first_name)
    last = driver.find_element(By.ID, 'lastName')
    last.send_keys(last_name)
    email = driver.find_element(By.ID, 'userEmail')
    email.send_keys(email_field)
    select = driver.find_element(By.ID, 'state')
    select.click()
    # Используем явное ожидание для видимости элемента
    select = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.ID, 'state'))
    )

    # Прокрутка до элемента
    driver.execute_script("arguments[0].scrollIntoView(true);", select)

    # Используем JavaScript для клика, если обычный клик не работает
    driver.execute_script("arguments[0].click();", select)

    state_option = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//div[@id='state']//div[text()='Haryana']"))
    )

    driver.execute_script("arguments[0].scrollIntoView(true);", state_option)
    driver.execute_script("arguments[0].click();", state_option)

    sleep(3)


def test_enabled_and_select(driver):
    driver.get('https://www.qa-practice.com/elements/button/disabled')
    button = driver.find_element(By.NAME, 'submit')
    print(button.is_enabled())
    select = driver.find_element(By.ID, 'id_select_state')
    dropdown = Select(select)
    dropdown.select_by_value('enabled')
    print(button.is_enabled())
