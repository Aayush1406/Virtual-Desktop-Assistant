import json
f=open("example_1.json","r")
data=f.read()
data=json.loads(data)#loads does not read file but convert string to dictionary
print(data["color"])