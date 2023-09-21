from utilities.request_builder_helpers import (
    api_params_reformat,
    check_api_link,
    check_http_method,
    encode_excel_base_x64
)


from cores.requestMethods.get import Get
from cores.requestMethods.del_ import Delete
from cores.requestMethods.patch import Patch
from cores.requestMethods.put import Put
from cores.requestMethods.post import Post


class RequestBuilder:
    def __init__(self, http_method, api):
        self.__http_method:str = check_http_method(http_method)
        self.__api :str= check_api_link(api)
        self.__authentication_token: str= None
        self.__headers = dict()
        self.__parameters = dict()
        self.__body = dict()
        self.__file:str = None

    def bearer_token(self, token: str):
        self.__authentication_token= token
        self.__headers["Authorization"] = "Bearer " + self.__authentication_token.strip()
        return self

    def headers(self,headers: dict):
        for key,val in headers.items():
            if type(key) is str :
                key=key.strip()
            if type(val) is str:   
                val=val.strip() 
            self.__headers[key]=val
        return self

    def files(self,path):
        self.__file[path]=encode_excel_base_x64(path)
        return self
    
    def custom_header(self, key, value):
        if type(key) is str :
            key=key.strip()
        if type(value) is str:   
            value=value.strip() 
        self.__headers[key] = value
        return self

    def parameters(self, parameters: dict):
        self.__parameters=parameters
        self.__api = api_params_reformat(self.__api, self.__parameters)
        return self

    def body(self, body):
        self.__body = body
        return self

    def send(self):
        self.__http_method=self.__http_method.upper()
        if self.__http_method == "GET":
            return Get().sendRequest(
                self.__api, json=self.__body, headers=self.__headers
            )
        elif self.__http_method == "POST":
            return Post().sendRequest(
                self.__api, json=self.__body, headers=self.__headers,files=self.__file
            )
        elif self.__http_method == "PUT":
            return Put().sendRequest(
                self.__api, json=self.__body, headers=self.__headers,files=self.__file
            )
        elif self.__http_method == "PATCH":
            return Patch().sendRequest(
                self.__api, json=self.__body, headers=self.__headers,files=self.__file
            )
        elif self.__http_method == "DELETE":
            return Delete().sendRequest(
                self.__api, json=self.__body, headers=self.__headers
            )
