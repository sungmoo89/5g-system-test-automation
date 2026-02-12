from core.base_test import BaseTest
from utils.api_client import APIClient
from utils.log_parser import LogParser

def test_5g_attach():
    base = BaseTest()
    base.setup()

    api = APIClient()
    response = api.trigger_attach()

    parser = LogParser()
    result = parser.parse("Attach Success")

    assert response["status"] == "success"
    assert result is True

    base.teardown()
