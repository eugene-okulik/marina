from playwright.sync_api import Page, Route
import json


def test_two(page: Page):
    def handle_route(route: Route):
        response = route.fetch()
        body = response.json()

        for item in body.get('body', {}).get('digitalMat', []):
            if item.get('productName') == 'iPhone 15 Pro':
                item['productName'] = 'айфончик'
                for familyType in item.get('familyTypes', []):
                    familyType['productName'] = 'айфончик'
        body = json.dumps(body)
        route.fulfill(
            response=response,
            body=body
        )

    page.route('**/digital-mat?path=library/step0_iphone/digitalmat', handle_route)
    page.goto("https://www.apple.com/shop/buy-iphone")
    page.locator('text="iPhone 15 Pro &"').click()
    page.wait_for_selector('text="айфончик"')
    assert page.locator('text="айфончик"').count() > 0
