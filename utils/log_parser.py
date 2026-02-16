class LogParser:

    def parse(self, log_data):
        if "Attach Success" in log_data:
            return True
        elif "Reject" in log_data:
            return False
        return None
