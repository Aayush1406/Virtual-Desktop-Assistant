import webbrowser
import speech
def website(order):
    #url=speech.take()
    #url=url.lower()
    url=order #url is passed from final.py and stored in url
    print("you said",url)
    chromedir="C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s" #here we are using google chrome
    if "youtube" in url :
        webbrowser.get(chromedir).open("youtube.com")
    elif "google" in url:
        webbrowser.get(chromedir).open("google.com")
    elif "facebook" in url:
        webbrowser.get(chromedir).open("facebook.com")
    elif "instagram" in url:
        webbrowser.get(chromedir).open("instagram.com")
    elif "1337x" in url:
        webbrowser.get(chromedir).open("1337x.com")
    elif "gmail" in url:
        webbrowser.get(chromedir).open("gmail.com")
    elif "gtu" in url:
        webbrowser.get(chromedir).open("student.gtu.ac.in")
    elif "netflix" in url:
        webbrowser.get(chromedir).open("netflix.com")
    elif "amazon" in url:
        webbrowser.get(chromedir).open("amazonprime.com")
    else:
        print("Does not exist")