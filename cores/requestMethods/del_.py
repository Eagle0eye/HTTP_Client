from ..httpclient import HttpClient
import requests


class Delete(HttpClient):
    def sendRequest(self, url, json=None, params=None, headers=None, files=None):
        return requests.delete(url, json, params, files, headers)

    def __str__(self) -> str:
        return __class__.__name__
