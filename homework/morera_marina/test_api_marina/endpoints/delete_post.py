import requests
import allure
from homework.morera_marina.test_api_marina.endpoints.endpoint import Endpoint


class DeletePost(Endpoint):
    @allure.step('Delete a post')
    def delete_post(self, post_id):
        self.response = requests.delete(
            f'{self.url}/{post_id}'
        )
