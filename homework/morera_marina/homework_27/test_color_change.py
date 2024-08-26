from playwright.sync_api import Page


def test_check_tabs(page: Page):
    page.goto('https://demoqa.com/dynamic-properties')
    button = page.locator('#colorChange')
    page.locator(".mt-4.text-danger.btn.btn-primary").wait_for()
    button_style = button.evaluate("el => window.getComputedStyle(el)")
    assert button_style['color'] == 'rgb(220, 53, 69)'
    button.click()
