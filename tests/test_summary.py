import pytest
from utils.api_client import APIClient   # IMPORTANT import

@pytest.mark.smoke
def test_get_summary_valid():
    response = APIClient.get("/posts/1")

    assert response.status_code == 200
    assert "id" in response.json()