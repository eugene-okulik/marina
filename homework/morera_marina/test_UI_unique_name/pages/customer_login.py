from playwright.sync_api import Page


class Customerlogin:
    def __init__(self, page: Page):
        self.page = page

    def open_page(self):
        self.page.goto('https://magento.softwaretestingboard.com/customer/account/create/')

    def registration_form(self, first, last, email, password, confirm_pas):
        first_name = self.page.locator('#firstname')
        last_name = self.page.locator('#lastname')
        email_field = self.page.locator('#email_address')
        password_field = self.page.locator('#password')
        confirm_field = self.page.locator('#password-confirmation')
        submit = self.page.get_by_role('button', name='Create an Account')
        first_name.fill(first)
        last_name.fill(last)
        email_field.fill(email)
        password_field.fill(password)
        confirm_field.fill(confirm_pas)

        submit.click()

    def check_success_text(self, expected_text):
        registering = self.page.locator('div.message-success')
        assert registering.inner_text() == expected_text

    def check_text(self, expected_text):
        registering = self.page.locator('div.message-error')
        assert registering.inner_text() == expected_text

    def exist_email_message_is(self, expected_text):
        email = self.page.locator('#email_address-error')
        assert email.inner_text() == expected_text
