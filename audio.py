import pyttsx3 #python text to speech module
engine=pyttsx3.init("sapi5") #microsoft speech api helps in speech recognition and syntheis
voices=engine.getProperty("voices") #get details of current voice
#print(voices[1].id)
engine.setProperty("rate",125)
engine.setProperty("voice",voices[0].id) #voices[0].id==Male && voices[1].id==female
def speak(audio): #speak fun() converts txt to audio
    
    engine.say(audio)
    engine.runAndWait()#Without this command, speech will not be audible to us


if __name__=="__main__":
    speak("Hi, i am smarti, what can i do for you?")