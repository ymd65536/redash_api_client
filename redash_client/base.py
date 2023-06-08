import json
import requests


class base_client:
    def __init__(self, api_key: str, host: str = "http://localhost:5000"):
        self.api_key = api_key
        self.host = host

        self.s = requests.Session()
        self.s.headers.update({"Authorization": f"Key {api_key}"})

    def get(self, uri: str, **kwargs):
        res = self.s.get(f"{self.host}/api/{uri}", **kwargs)

        if res.status_code != 200:
            raise Exception(f"[GET] /api/{uri} ({res.status_code})")

        return res

    def post(self, uri: str, payload: dict = None):
        if payload is None or not isinstance(payload, dict):
            payload = {}

        data = json.dumps(payload)

        self.s.headers.update({"Content-Type": "application/json"})
        res = self.s.post(f"{self.host}/api/{uri}", data=data)

        if res.status_code != 200:
            raise Exception(f"[POST] /api/{uri} ({res.status_code})")

        return res

    def delete(self, uri: str):
        res = self.s.delete(f"{self.host}/api/{uri}")

        if res.status_code != 200 and res.status_code != 204:
            raise Exception(f"[DELETE] /api/{uri} ({res.status_code})")

        return res
