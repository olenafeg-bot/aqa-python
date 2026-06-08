import pytest
import requests
import logging
from requests.auth import HTTPBasicAuth

logger = logging.getLogger("test_logger")
logger.setLevel(logging.INFO)

formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

console_handler = logging.StreamHandler()
console_handler.setFormatter(formatter)


file_handler = logging.FileHandler("test_search.log")
file_handler.setFormatter(formatter)

logger.addHandler(console_handler)
logger.addHandler(file_handler)


BASE_URL = "http://127.0.0.1:8080"

class TestSession:
    @pytest.fixture(scope="class")
    def session(self):
        session = requests.Session()

        response = session.post(
            f"{BASE_URL}/auth",
            auth=HTTPBasicAuth("test_user", "test_pass")
        )

        token = response.json()["access_token"]
        logger.info(f"Access token: {token}")

        session.headers.update({
            "Authorization": f"Bearer {token}"
        })

        return session
    @pytest.mark.parametrize("sort_by, limit", [("price", 10)])
    def test_cars(self, session, sort_by, limit):
        logger.info(f"Sending request to /cars ")
        response = session.get(f"{BASE_URL}/cars", params={"sort_by": sort_by, "limit": limit})

        assert response.status_code == 200
        logger.info(f"Cars status: {response.status_code}")

        data = response.json()
        logger.info(f"Response data: {data}")
        assert isinstance(data, list)
