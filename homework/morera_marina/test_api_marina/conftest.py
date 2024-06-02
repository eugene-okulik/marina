import pytest
from endpoints.create_post import CreatePost
from endpoints.put_post import PutPost
from endpoints.delete_post import DeletePost


@pytest.fixture()
def create_post_endpoint():
    return CreatePost()


@pytest.fixture()
def put_post_endpoint():
    return PutPost()


@pytest.fixture()
def delete_post_endpoint():
    return DeletePost()


@pytest.fixture()
def post_id(create_post_endpoint):
    payload = {"name": "Apple MacBook Pro 16", "year": 2019,
               "price": 1849.99,
               "CPU model": "Intel Core i9",
               "Hard disk size": "1 TB"}
    create_post_endpoint.create_new_post(payload)
    yield create_post_endpoint.post_id
