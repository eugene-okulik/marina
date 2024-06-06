from locust import HttpUser, task, between
import random


class CreatePost:
    url = 'https://api.restful-api.dev'
    headers = {'Content-type': 'application/json'}

    def create_new_post(self, client, payload):
        response = client.post(
            self.url,
            json=payload,
            headers=self.headers
        )
        post_id = response.json().get('id')
        return post_id


class ApiLocust(HttpUser):
    host = "https://api.restful-api.dev"

    TEST_DATA = [
        {"name": "Apple MacBook Pro 16", "price": "1839", "CPU model": "Intel Core i9", "Hard disk size": "1 TB"},
        {"name": "Apple MacBook Pro 18", "price": "2000", "CPU model": "Intel Core i99", "Hard disk size": "2 TB"}
    ]

    def on_start(self):
        self.create_post_endpoint = CreatePost()
        self.created_post_ids = []

    @task(1)
    def create_post_task(self):
        data = random.choice(self.TEST_DATA)
        post_id = self.create_post_endpoint.create_new_post(self.client, data)
        if post_id:
            self.created_post_ids.append(post_id)

    @task(2)
    def get_posts_task(self):
        self.client.get("/objects")
