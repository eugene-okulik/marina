import pytest

TEST_DATA = [
    {"name": "Apple MacBook Pro 16", "price": 1839.00, "CPU model": "Intel Core i9",
     "Hard disk size": "1 TB"},
    {"name": "Apple MacBook Pro 18", "price": 2000, "CPU model": "Intel Core i99",
     "Hard disk size": "2 TB"}
]


@pytest.mark.parametrize('data', TEST_DATA)
def test_post_a_post(create_post_endpoint, data):
    create_post_endpoint.create_new_post(payload=data)


def test_put_post(put_post_endpoint, post_id):
    payload = {
        "name": "Apple MacBook Pro 16 (Updated Name)",
        "price": 1232,
    }
    put_post_endpoint.make_changes_in_post(post_id, payload)
    put_post_endpoint.check_that_status_is_200()


def test_delete_post(delete_post_endpoint, post_id):
    delete_post_endpoint.delete_post(post_id)
    delete_post_endpoint.check_that_status_is_200()
