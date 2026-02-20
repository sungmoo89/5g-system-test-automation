from utils.network_simulator import NetworkSimulator
from utils.log_parser import LogParser
from utils.retry_controller import AttachController

def test_attach_retry():

    sim = NetworkSimulator()
    parser = LogParser()

    controller = AttachController(sim, parser)

    result = controller.run_attach()

    assert result["attempts"] <= 3
