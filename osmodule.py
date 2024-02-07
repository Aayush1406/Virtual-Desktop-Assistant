import audio
import speech
import os
import filterwords
def command():
    while True:
        audio.speak("what do you want to open?")
        flag=False
        desktop=False
        downloads=False
        response=speech.take()
        response=filterwords.filter_txt(response)
#        response=["bhavsar"]       
        print("user said=",response)
        if("stop" in response):
            break
        if(response=="None"):
            continue
        files_desktop=os.listdir("C:/Users/Aayush/Desktop")
#        files_desktop=["aayush","bhavsar aayush","ict","shershah"]
        #print(files_desktop)
        for i in (files_desktop):
           # print("items1 desktop",files_desktop[i])
            for j in (response):
            #    print("items2 desktop",response[j])
                if j in i.lower():
                    print("desktop success")
                    result=i
                    print("desktop",result)
#                    print(type(result))
                    desktop=True
                    flag=True
                    break
            if (flag==True):
                break
            
        files_downloads=os.listdir("C:/Users/Aayush/Downloads")
#        files_downloads=["how","goat","leo","hello"]
        #print(files_downloads)
        for i in files_downloads:
            for j in response:
                if j in i.lower():
                    print("downloads success")
                    result=i
                    print("downloads",result)
#                    print(type(result))
                    flag=True
                    downloads=True
                    break
            if(flag==True):
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
#command()
'''def command():
    while True:
        audio.speak("what do you want to open?")
        flag=False
        desktop=False
        downloads=False
        response=speech.take()
        print(response)
        #response=test.filter_txt(response)
        if("stop" in response):
            break
        if(response=="None"):
            continue
        files_desktop=os.listdir("C:/Users/Aayush/Desktop")
        #print(files_desktop)
        for items in files_desktop:
            if response in items.lower():
                print("success")
                result=items
                desktop=True
                flag=True
                break
        files_downloads=os.listdir("C:/Users/Aayush/Downloads")
        #print(files_downloads)
        for items in files_downloads:
            if response in items.lower():
                print("success")
                result=items
                flag=True
                downloads=True
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
command()'''
