from abc import ABC, abstractmethod


class HttpClient(ABC):
    @abstractmethod
    def sendRequest(self, url, json=None, params=None, headers=None, files=None):
        pass
