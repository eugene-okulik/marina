import re
from playwright.sync_api import Page, expect, Request, Route
from time import sleep
import json


def test(page: Page):

    def print_request(request: Request):
        print("request", request.post_data)

    page.on("request", print_request)
    page.goto("https://www.apple.com/shop/buy-iphone")
    with page.expect_response(re.compile('s68030986690955')) as response_event:
        page.locator('text="iPhone 15 Pro &"').click()
    response = response_event.value
    print(response)

    sleep(5)
def test_two(page: Page):
    def handle_route(route: Route):
        response = route.fetch()
        body = response.json()
        for item in body.get('body', {}).get('digitalMat', []):
            if item.get('productName') == 'iPhone 15 Pro':
                item['productName'] = 'айфончик'
        body = json.dumps(body)
        route.fulfill(
            response=response,
            body=body
        )

    page.route('**/digital-mat?path=library/step0_iphone/digitalmat', handle_route)
    page.goto("https://www.apple.com/shop/buy-iphone")
    page.locator('text="iPhone 15 Pro &"').click()
    sleep(5)

