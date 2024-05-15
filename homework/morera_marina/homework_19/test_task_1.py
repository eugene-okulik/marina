import requests
import pytest


@pytest.fixture(scope='session')
def hello():
    print('Start testing')
    yield
    print('Testing completed')


@pytest.fixture(scope='function')
def repeat():
    print('before test')
    yield
    print('after test')


@pytest.fixture()
def new_object_id():
    body = {
        "name": "Apple MacBook Pro 16",
        "data": {
            "year": 2019,
            "price": 1849.99,
            "CPU model": "Intel Core i9",
            "Hard disk size": "1 TB"
        }
    }
    headers = {'Content-Type': 'application/json'}
    response = requests.post('https://api.restful-api.dev/objects',
                             json=body,
                             headers=headers)
    post_id = response.json()['id']
    yield post_id
    requests.delete(f'https://api.restful-api.dev/objects/{post_id}')


@pytest.mark.parametrize("name, price", [("Apple MacBook Pro 16", 1839.00), ("Apple MacBook Pro 18", 2000),
                                         ("Apple MacBook Pro 20", 3233)])
def test_create_object(hello, name, price, repeat):
    body = {
        "name": name,
        "data": {
            "year": 2019,
            "price": price,
            "CPU model": "Intel Core i9",
            "Hard disk size": "1 TB"
        }
    }
    headers = {'Content-Type': 'application/json'}
    response = requests.post('https://api.restful-api.dev/objects',
                             json=body,
                             headers=headers)
    assert response.status_code == 200


@pytest.mark.critical
def test_put_object(new_object_id, hello, repeat):
    body = {
        "name": "Apple MacBook Pro 16 PUT",
        "data": {
            "year": 2019,
            "price": 1849.99,
            "CPU model": "Intel Core i9",
            "Hard disk size": "1 TB"
        }
    }
    headers = {'Content-Type': 'application/json'}
    response = requests.put(f'https://api.restful-api.dev/objects/{new_object_id}',
                            json=body,
                            headers=headers).json()
    assert response['name'] == 'Apple MacBook Pro 16 PUT'
    assert response['id'] == new_object_id


@pytest.mark.medium
def test_patch_object(new_object_id, hello, repeat):
    body = {
        "name": "Apple MacBook Pro 16 (Updated Name)"
    }
    headers = {'Content-Type': 'application/json'}
    response = requests.patch(f'https://api.restful-api.dev/objects/{new_object_id}',
                              json=body,
                              headers=headers).json()
    assert response['id'] == new_object_id


def test_delete_object(new_object_id, hello, repeat):
    response = requests.delete(f'https://api.restful-api.dev/objects/{new_object_id}')
    assert response.status_code == 200, 'Status code is incorrect'
