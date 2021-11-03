import  requests

BASE = "http://127.0.0.1:5000/"

response=requests.get(BASE+"helloworld/SUBHASISH/38")
print(response.json())

response=requests.post(BASE+"helloworld")
print(response)