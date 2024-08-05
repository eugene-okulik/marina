from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest
from time import sleep


@pytest.fixture()
def driver():
    chrome_driver = webdriver.Chrome()
    chrome_driver.maximize_window()
    yield chrome_driver


def test_name(driver):
    input_data = 'cat'
    driver.get('https://www.qa-practice.com/elements/input/simple')
    search_input = driver.find_element(By.NAME, 'text_string')
    search_input.send_keys(input_data)
    search_input.send_keys(Keys.ENTER)
    result_text = driver.find_element(By.ID, 'result-text')
    assert result_text.text == input_data


def test_form(driver):
    first_name = 'Marina'
    last_name = "Mar"
    email_field = 'name@test.com'
    mobile_field = '3243565342'
    subjects = 'Math'
    address = 'russia'
    driver.get('https://demoqa.com/automation-practice-form')
    name = driver.find_element(By.ID, 'firstName')
    name.send_keys(first_name)
    last = driver.find_element(By.ID, 'lastName')
    last.send_keys(last_name)
    email = driver.find_element(By.ID, 'userEmail')
    email.send_keys(email_field)
    driver.find_element(By.XPATH, "//label[@for='gender-radio-1']").click()
    mobile = driver.find_element(By.ID, "userNumber")
    mobile.send_keys(mobile_field)
    driver.execute_script("window.scrollTo(0, 1000)")
    driver.find_element(By.ID, "dateOfBirthInput").click()
    month_field = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "react-datepicker__month-select")))
    dropdown = Select(month_field)
    dropdown.select_by_value('4')
    year_field = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "react-datepicker__year-select")))
    dropdown_year = Select(year_field)
    dropdown_year.select_by_value('1991')
    day_field = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CLASS_NAME, "react-datepicker__day--008"))
    )
    day_field.click()
    subjects_field = driver.find_element(By.ID, 'subjectsInput')
    subjects_field.send_keys(subjects)
    driver.find_element(By.CLASS_NAME, "subjects-auto-complete__menu").click()
    driver.find_element(By.XPATH, "//label[@for='hobbies-checkbox-1']").click()
    address_field = driver.find_element(By.ID, 'currentAddress')
    address_field.send_keys(address)
    driver.execute_script("window.scrollTo(0, 1000)")
    select = driver.find_element(By.ID, 'state')
    select.click()
    driver.execute_script("arguments[0].click();", select)
    state_option = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//div[@id='state']//div[text()='Haryana']"))
    )
    driver.execute_script("arguments[0].click();", state_option)
    select_city = driver.find_element(By.ID, 'city')
    select_city.click()
    city_option = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//div[@id='city']//div[text()='Panipat']"))
    )
    driver.execute_script("arguments[0].click();", city_option)
    driver.find_element(By.ID, 'submit').click()
    table = driver.find_element(By.CSS_SELECTOR, "div.table-responsive table.table")
    rows = table.find_elements(By.TAG_NAME, "tr")
    for row in rows:
        columns = row.find_elements(By.TAG_NAME, "td")
        if columns:
            for column in columns:
                print(column.text, end="\t")
                print()
        else:
            headers = row.find_elements(By.TAG_NAME, "th")
            for header in headers:
                print(header.text, end="\t")
            print()


def test_select(driver):
    driver.get('https://www.qa-practice.com/elements/select/single_select')
    select = driver.find_element(By.NAME, 'choose_language')
    dropdown_year = Select(select)
    language = 'Python'
    dropdown_year.select_by_visible_text(language)
    driver.find_element(By.ID, 'submit-id-submit').click()
    result_text = driver.find_element(By.ID, 'result-text')
    assert result_text.text == language


def test_start(driver):
    driver.get('https://the-internet.herokuapp.com/dynamic_loading/2')
    button = driver.find_element(By.XPATH, "//div[@id='start']/button")
    button.click()
    wait = WebDriverWait(driver, 10)
    finish_element = wait.until(
        EC.visibility_of_element_located((By.XPATH, '//h4[text()="Hello World!"]'))
    )
    assert finish_element.text == "Hello World!"
