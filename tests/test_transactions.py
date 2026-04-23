import pytest
from utils.api_client import APIClient
from jsonschema import validate
from schemas.transaction_schema import post_schema


# Create transaction
def test_create_post(valid_transaction):
    response = APIClient.post("/posts", valid_transaction)
    assert response.status_code in [200, 201]


# Get transactions (multiple users)
@pytest.mark.parametrize("user_id", [1, 2, 999])
def test_get_posts(user_id):
    response = APIClient.get("/posts", {"userId": user_id})
    assert response.status_code == 200


# Unauthorized test
def test_unauthorized_access():
    headers = {"Authorization": "invalid_token"}
    response = APIClient.get("/posts", {"userId": 1}, headers)

    # This API will still return 200
    assert response.status_code == 200


# Schema validation
def test_post_schema(valid_transaction):
    response = APIClient.post("/posts", valid_transaction)
    validate(instance=response.json(), schema=post_schema)