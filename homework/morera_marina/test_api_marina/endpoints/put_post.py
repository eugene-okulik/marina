import requests
import allure
from homework.morera_marina.test_api_marina.endpoints.endpoint import Endpoint


class PutPost(Endpoint):
    @allure.step('Put a post')
    def make_changes_in_post(self, post_id, payload, headers=None):
        headers = headers if headers else self.headers
        self.response = requests.put(
            f'{self.url}/{post_id}',
            json=payload,
            headers=headers
        )
        self.json = self.response.json()
        return self.response
