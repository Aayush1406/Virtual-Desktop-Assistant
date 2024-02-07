import json
import requests
import audio
import speech
import os
import test
def command():
    while True:
        audio.speak("what do you want to open?")
        flag=False
        desktop=False
        downloads=False
#        response=speech.take()
#        response=test.filter_txt(response)
        response=["shershah"]       
        print(response)
        if("stop" in response):
            break
        if(response=="None"):
            continue
        files_desktop=os.listdir("C:/Users/Aayush/Desktop")
        print(files_desktop)
        for items1 in files_desktop:
            for items2 in response:
                if items2 in items1.lower():
                    print("success")
                    result=items1
                    print(result)
                    desktop=True
                    flag=True
                    break
            break
        files_downloads=os.listdir("C:/Users/Aayush/Downloads")
        #print(files_downloads)
        for items1 in files_downloads:
            for items2 in items1.lower():
                if items2 in items1.lower():
                    print("success")
                    result=items1
                    print(result)
                    flag=True
                    downloads=True
                    break
            break
        if(flag==False):
            audio.speak("does not exist!")
            continue      
        if(desktop==True):      
            path="C:/Users/Aayush/Desktop/"+result
            os.startfile(path)
        if(downloads==True):
            path="C:/Users/Aayush/Downloads/"+result
            os.startfile(path)
command()