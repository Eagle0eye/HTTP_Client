from cores.request_builder import RequestBuilder
import time

token="eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjk3OTI3NTMwLCJpYXQiOjE2OTUzMzU1MzAsImp0aSI6ImI3YzFmNGYzMjM5MzQxOGI4MGFlMmExODFkN2VhZDE0IiwidXNlcl9pZCI6NDMsImZ1bGxfbmFtZSI6Ik5ldyB0ZXN0Iiwicm9sZSI6ImNvbXBhbnkiLCJhdmF0YXIiOiJ1c2Vycy9OZXcgdGVzdC84NTE1OWY3OC0zMWQ2LTQ4ZDMtYWQ4OS00NzkxZWEzMjNmZjEucG5nIn0.UGjL9dJmNLVraSig2AjRSlq6AhGEwD72o6t4oGhCSrc"
response = (
    RequestBuilder("GET", "https://api.dev.mdawm.com/api/company/v1/user/")
    .bearer_token(token)
    .send()
)

file =open("response.json",'w+')
file.write(response.text)
file.close()