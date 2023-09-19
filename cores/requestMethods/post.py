from ..httpclient import HttpClient
import requests


class Post(HttpClient):
    def sendRequest(self, url, json=None, headers=None, files=None):
        return requests.post(url, json=json, headers=headers, files=files)

    def __str__(self) -> str:
        return __class__.__name__
