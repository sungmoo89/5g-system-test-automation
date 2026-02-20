import random
import time
import os
from datetime import datetime

LOG_FILE = "logs/gnb.log"

class NetworkSimulator:

    def ue_attach(self, ue_id="UE001", force_result=None):

        os.makedirs("logs", exist_ok=True)
        outcomes = ["REGISTERED", "TIMEOUT", "AUTH_FAIL"]

        if force_result:
            result = force_result
        else:
            result = random.choice(outcomes)
            result = result.upper()

        with open(LOG_FILE, "a") as f:
            f.write(f"{datetime.now()} UE {ue_id} RRC SETUP\n")

            if result == "REGISTERED":
                f.write("UE ATTACH COMPLETE\n")
            elif result == "TIMEOUT":
                f.write("RRC TIMEOUT\n")
            else:
                f.write("AUTHENTICATION FAILURE\n")

        return {"state": result}
