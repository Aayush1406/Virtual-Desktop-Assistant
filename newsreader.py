import json
import requests #with the help of this module we can sent http request
import audio # audio file contains speak() fun
import speech# speech file contains take() fun
import filterwords #filterwords contains filter_txt() fun
def readnews(): 
    apidata=requests.get("https://newsapi.org/v2/top-headlines?country=us&apiKey=adffb7a838634ba4a02b7c5bb4195387")
#since we are sending get request we use "requests.get()" fun
    apidata=apidata.json() #it returns a python dictionary and stores it in apidata
    apidata=apidata["articles"] #here articles is list so we go inside list 
    #print(data[0]["source"]["name"])
    for item in apidata : #here we iterate list 
        print(item["source"]["name"]) #here source is a dictionary inside list and 
                                        #it has key value name whose value will be news type(eg. BBC news)
    
    while True: #here until user says "stop" it will keep on telling news 
        str=speech.take()  #user will tell his news choice and stored in str 
        print(str)
        str=filterwords.filter_txt(str) #here the fun() tokenize the string, removes stopwords and returns a list 
        print(str)
        flag=False
        if("stop" in str):
            break
        if("None" in str):
            continue
        for item in apidata:
            for item2 in str:
                if(item2 in item["source"]["name"].lower()):
                    print(item["content"])
                    audio.speak(item["content"])
                    flag=True
                    break
            if(flag==True):
                break
        '''for item in apidata: #iterating list articles
            if (str  in item["source"]["name"].lower() ): #here if name contains whatever is in str
                print(item["content"])# than print the content of that particular news name
                audio.speak(item["content"])#speaks the content
                flag=True
                break'''
        print("flag value=",flag)
        if(flag==False):
            audio.speak("News type does not exist")        
if __name__=="__main__":
    readnews()
