import requests
import allure

from homework.morera_marina.test_api_marina.endpoints.endpoint import Endpoint


class CreatePost(Endpoint):
    post_id = None

    @allure.step('Create new post')
    def create_new_post(self, payload, headers=None):
        headers = headers if headers else self.headers
        self.response = requests.post(
            self.url,
            json=payload,
            headers=headers
        )
        self.json = self.response.json()
        self.post_id = self.json['id']
        return self.response
