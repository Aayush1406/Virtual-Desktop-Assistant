import json
f=open("example_1.json")
data=json.load(f)# load read file and convert string format into dict
print(type(data))
data=json.dumps(data)# dumps converts dict format to string format
print(type(data))