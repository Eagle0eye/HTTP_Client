from ..httpclient import HttpClient
import requests


class Get(HttpClient):
    def sendRequest(self, url, json=None, headers=None):
        return requests.get(url, json=json, headers=headers)

    def __str__(self) -> str:
        return __class__.__name__
