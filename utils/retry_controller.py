class AttachController:

    def __init__(self, simulator, parser, max_retry=3):
        self.sim = simulator
        self.parser = parser
        self.max_retry = max_retry

    def run_attach(self):

        for attempt in range(1, self.max_retry + 1):

            response = self.sim.ue_attach()

            if response["state"] == "REGISTERED":
                return {
                    "final_state": "REGISTERED",
                    "attempts": attempt
                }

        return {
            "final_state": "FAILED",
            "attempts": self.max_retry
        }
