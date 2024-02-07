import speech_recognition as sr #speech recognition is a module used for converting an audio to txt 
import audio #audio file imported which has speak fun() that converts text to speech
def take(): #it takes microphone input from user and returns string as an output
    r=sr.Recognizer() 
    with sr.Microphone() as source:
        print("Listening......")
        r.energy_threshold = 40
        r.pause_threshold=1.0
        audio_data=r.listen(source)
    try:
        print("Recognizing....") 
        text=r.recognize_google(audio_data,language="en-in")#using google for speech recognition and returned data is stored in text
        text=text.lower() 
        print("user said",text)# whatever said by user is printed here.
    except Exception as e:
        audio.speak("plz say that again")#if there is an error in "recognize_google" than interpreter will jump to this statement
        return "None"#and returns none is it is not recognized by "recognize_google" fun()
    return text#else whatever is said by user is return by "return text" in string format

if __name__=="__main__":# works as a main fun() it will not get executed when called into another file.

    speech=take()
    print((speech))
