import smtplib as s #it is a protocol that allows you to send email
import audio
import speech
def emailfun():
    obj=s.SMTP("smtp.gmail.com",587) #it creates a session  and establishes connection 
    obj.starttls()#transport layer security it is used to encrypt for security purpose
    obj.login("sergioprofessor.1406@gmail.com","sergio@123") #login(email,pass)
    while True: #works until stop is said
        audio.speak("Whom do you want to send the email?")
        recepient=speech.take() #it takes the imput and returned data is stored in recepient. here we say
        #the name of a person
        if("stop" in recepient):
            return "stop"
        if recepient in email_dict: #if email_dict contains recepient name than 
            recepient=email_dict[recepient] #gives the value of recepeint i.e email id 
            pass
        else:
            continue
        break
    while True:
        audio.speak("what is the subject of your email")
        subject=speech.take()
        print(subject)
        if(subject==None):
            continue
        audio.speak("say yes if message typed over here is correct else say no")
        response=speech.take()
        
        if("yes" in response):
            break
        else:
            continue
    while True:    
        audio.speak("what is body of your email")
        body=speech.take()
        print(body)
        if(body==None):
            continue
        audio.speak("say yes if message typed over here is correct else say no")
        response=speech.take()
        if("yes" in response):
            break
        else:
            continue
    message="subject:{}\n\n{}".format(subject,body)
    obj.sendmail("sergioprofessor.1406@gmail.com",recepient,message) #(sender,receiver,msg)
    print("sent successfully")
    obj.quit()#close the established session
    


email_dict={ "aayush":"aayushbhavsar.ab@gmail.com",
"chinmayi":"cmpatel1412@gmail.com",
"shrey":"shreygajjar1998@gmail.com",
"rajesh":"rajeshbhavar1967@yahoo.com",
"aatman":"aatmanpathak@gmail.com",
"nita":"bhavsarnita1969@gmail.com",
"avish":"avishshah18@gmail.com",
"trusha":"trushashah1971@gmail.com",
"richa":"bhavsarricha1995@gmail.com",
"anil":"a.desai@aegisinfoware.com",
"jameen":"mmp1981p@gmail.com"
}
