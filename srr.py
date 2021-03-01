import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes
import random

engine = pyttsx3.init()
listener=sr.Recognizer()

#def inmic()

def talk(command):
    engine.say(command)
    engine.runAndWait()

i=1
k=0
def micro():
    global i
    global k
    try:
        with sr.Microphone() as source:
            print("Listening...")
            voice=listener.listen(source)
            command=listener.recognize_google(voice)
            command=command.lower()
            if "gp" in command:
                i=i+1
                if command=="gp":
                    k=1
                
                command=command.replace("gp","")
                return(command)
            elif i>1:
                return(command)
            else:
                print(command)
                command="I am Voice Assisstant GP.Refer me as GP"
                #talk(command)
                return(command)


    except:
        pass


c=1
g=0
def td():
    global c,g,k
    command=micro()
    if 'time' in command:
        time = datetime.datetime.now().strftime("%I:%M %S %p")
        talk(datetime.datetime.now().strftime("%d of %B,20%y"))
        print(datetime.datetime.now().strftime("%d %B,20%y"))
        talk("Current time is"+time)
        print(time)
        c=0
    elif "play" in command:
        command=command.replace("play","")
        talk("Playing "+command)
        pywhatkit.playonyt(command)
        c=0
    elif "joke" in command:
        print(pyjokes.get_joke())
        talk(pyjokes.get_joke())
        c=0
    elif "why" in command:
        info=wikipedia.summary(command,2)
        print(info)
        talk(info)
        c=0
    elif "who" in command:
        info=wikipedia.summary(command,2)
        print(info)
        talk(info)
        c=0
    elif "which" in command:
        info=wikipedia.summary(command,2)
        print(info)
        talk(info)
        c=0
    elif "what" in command:
        info=wikipedia.summary(command,2)
        print(info)
        talk(info)
        c=0
    elif k==1:

            talk("Yea...I am hearing")
            c=2
            
    else: 
            #print()
            print(command)
            talk("I didn't get you ")
            g=1
            exit()   
            

d="yes"
while(d=="yes"):

    td()
    
    if g!=1 and c!=2:
        talk(random.choice(["Anything else?","anyother task to do?","Do you want me to do anything else for you?"]))
        with sr.Microphone() as source:
                voice=listener.listen(source)
                command=listener.recognize_google(voice)
                d=command.lower()
        g=0
    else:
        talk("Go on")
        td()
    
if(d!="yes"):
        talk("Have a Nice Day")
        