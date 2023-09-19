from request_builder import RequestBuilder

param = {"seconds": 10}

response = (
    RequestBuilder("GET", "https://hub.dummyapis.com/delay")
    .custom_header("Content-Type", "application/json")
    .parameters(param)
    .send()
)

print(response.status_code)
