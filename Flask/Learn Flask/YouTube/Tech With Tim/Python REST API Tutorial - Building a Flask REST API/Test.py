import requests

BASE = "http://127.0.0.1:5000/"

data = [{"likes": 78, "name": "Joe", "views": 100000},
        {"likes": 10000, "name": "HOW to make REST API", "views": 80000},
        {"likes": 35, "name": "Tim", "views": 2000}]

for i in range(len(data)):
    response=requests.put(BASE+"video/"+str(i),data[i])
    print(response.json())

input()
response = requests.put(BASE + "video/1", {"likes": 10000, "name": "SUBHASISH", "views": 100000})
print(response.json())
input()
response = requests.get(BASE + "video/1")
print(response.json())

# response=requests.post(BASE+"helloworld")
# print(response)
