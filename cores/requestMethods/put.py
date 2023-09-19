from ..httpclient import HttpClient
import requests


class Put(HttpClient):
    def sendRequest(self, url, json=None, headers=None, files=None):
        return requests.patch(url, json=json, headers=headers, files=files)

    def __str__(self) -> str:
        return __class__.__name__
