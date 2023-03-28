from .base import base_client as cli


class data_sources:
    def __init__(self, base_client) -> None:
        self.request_client = base_client

    def get_data_sources(self):
        res = cli.get(self.request_client, 'data_sources')
        return res.json()

    def get_data_source(self, num):
        res = cli.get(self.request_client, f'data_sources/{num}')
        return res.json()
