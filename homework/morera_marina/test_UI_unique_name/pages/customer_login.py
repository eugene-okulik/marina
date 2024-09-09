from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Customerlogin:
    def __init__(self, driver):
        self.driver = driver

    def open_page(self):
        self.driver.get('https://magento.softwaretestingboard.com/customer/account/create/')

    def registration_form(self, first, last, email, password, confirm_pas):
        first_name = self.driver.find_element(By.ID, 'firstname')
        last_name = self.driver.find_element(By.ID, 'lastname')
        email_field = self.driver.find_element(By.ID, 'email_address')
        password_field = self.driver.find_element(By.ID, 'password')
        confirm_field = self.driver.find_element(By.ID, 'password-confirmation')
        submit = self.driver.find_element(By.CLASS_NAME, 'submit')
        first_name.send_keys(first)
        last_name.send_keys(last)
        email_field.send_keys(email)
        password_field.send_keys(password)
        confirm_field.send_keys(confirm_pas)
        submit.click()

    def check_success_text(self, expected_text):
        registering = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="maincontent"]/div[1]/div[2]/div/div/div'))

        )
        assert registering.text == expected_text

    def check_text(self, expected_text):
        registering = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="maincontent"]/div[2]'))

        )
        assert registering.text == expected_text

    def exist_email_message_is(self, expected_text):
        email = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="email_address-error"]'))
        )
        assert email.text == expected_text

