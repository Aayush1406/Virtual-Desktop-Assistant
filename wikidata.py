import wikipedia #it is python library that gives data from wikipedia
import speech
import audio #audio file is imported that has speak() fun
def wikiInfo(data):# data contains string with word wikipedia + "(eg. Virat kohli)"
    speechdata=data.replace("wikipedia","")  #wikipedia word is replaced  with empty string "" and data(eg. virat kohli) 
                                                #is stored in speechdata
    try:
        result=wikipedia.summary(speechdata, sentences=2) #fun summary() gives 2 line summary about speechdata(eg.Virat kohli)
        print(result)
    except Exception as e:
        audio.speak("Data does not exist")#if there arises any exception in summary() fun 
        return None #than this line will get executed and returns None
    audio.speak(result) #summary data stored in result is verbalized by audio.speak() fun