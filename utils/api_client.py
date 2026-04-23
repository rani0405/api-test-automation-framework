import requests
from utils.config import BASE_URL

class APIClient:

    @staticmethod
    def get(endpoint, params=None, headers=None):
        return requests.get(
            BASE_URL + endpoint,
            params=params,
            headers=headers
        )

    @staticmethod
    def post(endpoint, payload=None, headers=None):
        return requests.post(
            BASE_URL + endpoint,
            json=payload,
            headers=headers
        )