class LogParser:

    def parse(self, log_text):

        log_text = log_text.upper()
        
        if "ATTACH COMPLETE" in log_text:
            return "SUCCESS"
        elif "AUTHENTICATION FAILURE" in log_text:
            return "AUTH_FAIL"
        elif "TIMEOUT" in log_text:
            return "TIMEOUT"
        return "UNKNOWN"


    def parse_attach_success(self, logfile="logs/gnb.log"):
        with open(logfile, "r") as f:
            logs = f.read()

        return "UE ATTACH COMPLETE" in logs
