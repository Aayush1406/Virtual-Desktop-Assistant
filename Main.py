#This is main file, each files will be controlled form here
import speech
import sites
import newsreader
import audio
import wikidata
import sendmail
import osmodule
audio.speak("Hello! welcome to the world of AI. I am professor, How may i help you??") #calling audio.py file
#audio.speak("હેલો હું ચુ પ્રોફેસર મની હેઇસ્ટ થી વાત કરું છું")
audio.speak("kem chho! Artificial intellegence  nee  duniyaa ma tamaro swagat che! hu chhu professor")

while True:  # professor keeps on listening until "stop" is said.
    results=speech.take() #speech file which has take fun() which converts audio to text
    if("wikipedia") in results: 
        wikidata.wikiInfo(results) #calls wikiInfo() fun from wikidata file
    elif("news") in results:
        newsreader.readnews() #calls readnews() fun from newsreder file
    elif "youtube" in results:#opens youtube if there is youtube word included in a statement said by the user
        sites.website(results)
    elif "google" in results:
        sites.website(results)
    elif "instagram" in results:
        sites.website(results)
    elif "netflix" in results:
        sites.website(results)
    elif "amazon" in results:
        sites.website(results)
    elif "gmail" in results:
        sites.website(results)    
    elif "mail" in results:
        sendmail.emailfun()#if a user want to send a mail than from sendmail.py file emailfun() is called. 
    elif "pc" in results:#if a user want to open any file,program,application or a movie 
        osmodule.command()#calls command() fun() from osmodule file
    elif("stop") in results:# if user says stop than we will be out of the loop and program will end
        break
audio.speak("I am tired now!, Bye Bye!!!!")