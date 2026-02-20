from utils.log_parser import LogParser

def test_5g_attach_fail():
    parser = LogParser()

    fake_log = "Attach Reject - Cause: Authentication Failure"

    result = parser.parse(fake_log)

    assert result == "AUTH_FAIL"
