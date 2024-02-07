import json
f=open("example_1.json","r")#the data in json is in string format

data=json.load(f)# load function reads the json file and converts string to dictionary
print("loadddd=",data)
print(type(data))