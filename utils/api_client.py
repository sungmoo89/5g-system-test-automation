import requests


class APIClient:

    BASE_URL = "https://jsonplaceholder.typicode.com"

    def get_post(self, post_id):
        response = requests.get(f"{self.BASE_URL}/posts/{post_id}")
        return response

    # ✅ UE Attach simulation
    def trigger_attach(self, payload):
        """
        Simulate UE 5G attach procedure
        (Real world: call mobility / registration API)
        """

        response = requests.post(
            f"{self.BASE_URL}/posts",
            json=payload
        )

        # 실제 telecom attach 결과처럼 변환
        if response.status_code == 201:
            return {
                "status": "attached",
                "ue_id": payload.get("ue_id"),
            }
        else:
            return {
                "status": "failed"
            }
