from cores.request_builder import RequestBuilder

response1 = RequestBuilder("GET", "https://github.com/OxR00t/HTTP_Client").send()
response2 = RequestBuilder("GET", "http://httpstat.us/404").send()
response3 = RequestBuilder("GET", "http://httpstat.us/500").send()
