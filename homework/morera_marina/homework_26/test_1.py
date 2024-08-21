from playwright.sync_api import Page


def test_first(page: Page):
    page.goto('https://the-internet.herokuapp.com/')
    page.get_by_role('link', name='Form Authentication').click()
    page.get_by_role('textbox', name='username').fill('tomsmith')
    page.get_by_role('textbox', name='password').fill('SuperSecretPassword!')
    page.get_by_role('button', name='login').click()


def test_practice(page: Page):
    page.goto('https://demoqa.com/automation-practice-form')
    page.get_by_placeholder('First Name').fill('Ivan')
    page.get_by_placeholder('Last Name').fill('Python')
    page.get_by_placeholder('name@example.com').fill('test@yandex.ru')
    page.locator('input[type="radio"][value="Male"]').click(timeout=10000, force=True)
    page.get_by_placeholder('Mobile Number').fill('4396958765')
    page.locator('#dateOfBirthInput').fill('1 Sep 1997')
    page.locator('#subjectsInput').click()
    page.locator('#subjectsInput').fill('Maths')
    page.locator('div.subjects-auto-complete__option', has_text='Maths').click()
    page.locator('#hobbies-checkbox-1').click(timeout=10000, force=True)
    page.get_by_placeholder('Current Address').fill('Current address text test')
    page.locator('#state').click()
    page.locator('text="NCR"').click()
    page.locator('#city').click()
    page.locator('text="Delhi"').click()
    page.get_by_role('button', name='Submit').click()
