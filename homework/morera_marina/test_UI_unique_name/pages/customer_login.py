from playwright.sync_api import Page
from playwright.sync_api import Expect

class Customerlogin:
    def __init__(self, page: Page):
        self.page = page

    def open_page(self):
        self.page.goto('https://magento.softwaretestingboard.com/customer/account/create/')

    def registration_form(self, first, last, email, password, confirm_pas):
        first_name = self.page.locator('firstname')
        last_name = self.page.locator('lastname')
        email_field = self.page.locator('email_address')
        password_field = self.page.locator('password')
        confirm_field = self.page.locator('password-confirmation')
        submit = self.page.locator('submit')
        first_name.fill(first)
        last_name.fill(last)
        email_field.fill(email)
        password_field.fill(password)
        confirm_field.fill(confirm_pas)
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

