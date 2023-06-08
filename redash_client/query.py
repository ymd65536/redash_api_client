from .base import base_client as cli


class queries:
    def __init__(self, base_client) -> None:
        self.request_client = base_client

    def get_queries(self):
        """_summary_

        Returns:
            List: query list
        """
        res = cli.get(self.request_client, 'queries')
        return res.json()
