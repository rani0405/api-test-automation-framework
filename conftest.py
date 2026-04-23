import pytest
from utils.helpers import load_test_data

data = load_test_data()

@pytest.fixture
def valid_transaction():
    return data["valid_transaction"]

@pytest.fixture
def invalid_transaction():
    return data["invalid_transaction"]

@pytest.fixture
def missing_field_transaction():
    return data["missing_field_transaction"]

@pytest.fixture
def large_transaction():
    return data["large_transaction"]