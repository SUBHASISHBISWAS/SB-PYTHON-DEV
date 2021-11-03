import  requests

BASE = "http://127.0.0.1:5000/"


response = requests.put(BASE+"video/1",{"likes":10})
print(response.json())

#response=requests.get(BASE+"helloworld/SUBHASISH/38")
#print(response.json())

#response=requests.post(BASE+"helloworld")
#print(response)