from homework.morera_marina.test_UI_unique_name.pages.base_page import BasePage
from homework.morera_marina.test_UI_unique_name.locators.locators import Locators


class Customerlogin(BasePage):
    page_url = '/customer/account/create/'

    def registration_form(self, first, last, email, password, confirm_pas):
        first_name = self.page.locator(Locators.FIRST_NAME)
        last_name = self.page.locator(Locators.LAST_NAME)
        email_field = self.page.locator(Locators.EMAIL)
        password_field = self.page.locator(Locators.PASSWORD)
        confirm_field = self.page.locator(Locators.PASSWORD_CONFIRM)
        submit = self.page.get_by_role('button', name='Create an Account')
        first_name.fill(first)
        last_name.fill(last)
        email_field.fill(email)
        password_field.fill(password)
        confirm_field.fill(confirm_pas)

        submit.click()

    def check_success_text(self, expected_text):
        registering = self.page.locator(Locators.MESSAGE_SUCCESS)
        assert registering.inner_text() == expected_text

    def check_text(self, expected_text):
        registering = self.page.locator(Locators.MESSAGE_ERROR)
        assert registering.inner_text() == expected_text

    def exist_email_message_is(self, expected_text):
        email = self.page.locator(Locators.EMAIL_ERROR)
        assert email.inner_text() == expected_text
