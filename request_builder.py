from utilities.request_builder_helpers import (
    api_params_reformat,
    check_api_link,
    check_http_method,
)
from cores.requestMethods.get import Get
from cores.requestMethods.del_ import Delete
from cores.requestMethods.patch import Patch
from cores.requestMethods.put import Put
from cores.requestMethods.post import Post


class RequestBuilder:
    def __init__(self, http_method, api):
        self.__http_method = check_http_method(http_method)
        self.__api = check_api_link(api)
        self.__authentication_token = None
        self.__headers = dict()
        self.__parameters = None
        self.__body = dict()

    def bearer_token(self, token: str):
        self.__headers["Authorization"] = "Bearer " + token
        return self

    def headers(self,headers: dict):
        for key,val in headers.items():
            self.__headers[key]=val
        return self

    def custom_header(self, key, value):
        self.__headers[key] = value
        return self

    def parameters(self, parameters: dict):
        self.__api = api_params_reformat(self.__api, parameters)
        return self

    def body(self, body):
        self.__body = body
        return self

    def send(self):
        if self.__http_method == "GET":
            return Get().sendRequest(
                self.__api, json=self.__body, headers=self.__headers
            )
        elif self.__http_method == "POST":
            return Post().sendRequest(
                self.__api, json=self.__body, headers=self.__headers
            )
        elif self.__http_method == "PUT":
            return Put().sendRequest(
                self.__api, json=self.__body, headers=self.__headers
            )
        elif self.__http_method == "PATCH":
            return Patch().sendRequest(
                self.__api, json=self.__body, headers=self.__headers
            )
        elif self.__http_method == "DELETE":
            return Delete().sendRequest(
                self.__api, json=self.__body, headers=self.__headers
            )
