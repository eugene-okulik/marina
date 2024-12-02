from playwright.sync_api import Page


class BasePage:
    base_url = 'https://magento.softwaretestingboard.com'
    page_url = None

    def __init__(self, page: Page):
        self.page = page

    def open_page(self):
        if self.page_url:
            self.page.goto(f'{self.base_url}{self.page_url}')
            popup = self.page.locator("div.fc-consent-root")
            popup.wait_for(state='visible', timeout=60000)
            self.page.locator("button.fc-button.fc-cta-consent.fc-primary-button").click()
        else:
            raise NotImplementedError('Page can not be opened by URL for this page')
