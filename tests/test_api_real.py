from utils.api_client import APIClient
from utils.logger import get_logger

logger = get_logger(__name__)

def test_real_api_call():

    api = APIClient()
    response = api.get_post(1)

    logger.info(f"Status Code: {response.status_code}")

    assert response.status_code == 200

    data = response.json()

    logger.info(f"User ID: {data['userId']}")

    assert "userId" in data
    assert "title" in data
