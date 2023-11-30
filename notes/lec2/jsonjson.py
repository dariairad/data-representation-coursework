import json

data = {
    "name":"joe",
    "age":21,
    "student": True
    }

#print(data)

file = open("simple.json", "w")
jsonString = json.dumps(data)
print(jsonString)

############################

#importing from a file
import json
filename = "filename.json"

with open(filename, "r") as fp:
    jsonobject = json.load(fp)
for employee in jsonobject["employees"]:
    print(employee)


# importing from the cloud

import requests
url = "URL"
response = requests.get(url)
data = response.json()
print(data)



