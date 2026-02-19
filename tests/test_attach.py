from utils.logger import get_logger
from core.base_test import BaseTest
from utils.api_client import APIClient
from utils.log_parser import LogParser
from utils.config_loader import load_config

logger = get_logger(__name__)

def test_5g_attach():
    config = load_config("config/test_config.yaml")
    print("Network:", config["network"]["name"])    
    
    base = BaseTest()
    base.setup()

    api = APIClient()
    payload = {
        "ue_id": "test_ue_01",
        "network": config["network"]["name"]
    }
    response = api.trigger_attach(payload)

    parser = LogParser()
    result = parser.parse("Attach Success")

    assert response["status"] == "attached"
    assert result is True

    base.teardown()
