import requests


def create_object():
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
    assert response.json()['id']


def new_post():
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
    return response.json()['id']


def put_object():
    post_id = new_post()
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
    response = requests.put(f'https://api.restful-api.dev/objects/{post_id}',
                            json=body,
                            headers=headers).json()
    assert response['name'] == 'Apple MacBook Pro 16 PUT'
    print(response)
    clear(post_id)


def clear(post_id):
    requests.delete(f'https://api.restful-api.dev/objects/{post_id}')


def patch_object():
    post_id = new_post()
    body = {
        "name": "Apple MacBook Pro 16 (Updated Name)"
    }
    headers = {'Content-Type': 'application/json'}
    response = requests.patch(f'https://api.restful-api.dev/objects/{post_id}',
                              json=body,
                              headers=headers).json()
    print(response)
    clear(post_id)


def delete_object():
    post_id = new_post()
    response = requests.delete(f'https://api.restful-api.dev/objects/{post_id}')
    print(response.json())
    assert response.status_code == 200, 'Status code is incorrect'


create_object()
put_object()
patch_object()
delete_object()
