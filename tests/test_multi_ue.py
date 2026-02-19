import pytest
from utils.api_client import APIClient
from utils.logger import get_logger

logger = get_logger(__name__)

@pytest.mark.parametrize("ue_id", [1,2,3,4,5])
def test_multiple_ue_attach(ue_id):

    api = APIClient()
    response = api.get_post(ue_id)

    logger.info(f"UE {ue_id} status: {response.status_code}")

    assert response.status_code == 200
