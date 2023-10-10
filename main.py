from cores.request_builder import RequestBuilder
import time

token="Token_API"
response = (
    RequestBuilder("GET", "https://www.youtube.com/")
    .bearer_token(token)
    .send()
)

file =open("response.json",'w+')
file.write(response.text)
file.close()