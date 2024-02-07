import json
import requests
import audio
import speech
import filterwords
def readnews():
    apidata=requests.get("https://newsapi.org/v2/top-headlines?country=us&apiKey=adffb7a838634ba4a02b7c5bb4195387")

    apidata=apidata.json()
    apidata=apidata["articles"]
    #print(data[0]["source"]["name"])
    for item in apidata :
        print(item["source"]["name"])
        #choice=input("Enter your choice")
    while True:
        str=speech.take()
        print(str)
        str=filterwords.filter_txt(str)
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
        print("flag value=",flag)
        if(flag==False):
            audio.speak("News type does not exist")        
if __name__=="__main__":
    readnews()
