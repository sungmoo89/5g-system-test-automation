import pytest
from utils.log_parser import LogParser
from utils.logger import get_logger
from core.base_test import BaseTest
# from utils.api_client import APIClient
from utils.network_simulator import NetworkSimulator
from utils.log_parser import LogParser
from utils.config_loader import load_config

scenarios = ["REGISTERED", "TIMEOUT", "AUTH_FAIL"]

@pytest.mark.parametrize(
    "network_state",
    scenarios,
    ids=scenarios
)


def test_5g_attach(network_state):
    config = load_config("config/test_config.yaml")
    print("Network:", config["network"]["name"])    
    
    base = BaseTest()
    base.setup()

    sim = NetworkSimulator()

    response = sim.ue_attach(force_result=network_state)

    parser = LogParser()
    result = parser.parse_attach_success()

    if network_state == "REGISTERED":
        assert response["state"] == "REGISTERED"
        assert result is True

    else:
        assert response["state"] != "REGISTERED"

    base.teardown()
