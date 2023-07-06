import pyttsx3 #text to speach using python
import datetime
import speech_recognition as sr  #pip install SpeechRecognition
import smtplib
from Mysecrets import senderemail, epwd, to
from email.message import EmailMessage
import pyautogui
import webbrowser as wb
from time import sleep
import wikipedia
import pywhatkit
import clipboard
import os
import pyjokes
import time as tt
import string
import random
from nltk.tokenize import word_tokenize

engine =pyttsx3.init()

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def getvoices(voice):
    voices = engine.getProperty('voices')
    #print(voices[1].id)
    if voice == 1:
        engine.setProperty('voice', voices[0].id)
        speak("Hello this is cortana")
    
    if voice == 2:
        engine.setProperty('voice', voices[1].id)
        speak("Hello this is Cortana")
    
def time():
    Time = datetime.datetime.now().strftime("%I:%M:%S")# hour = I minutes 
    speak("the current time is:")
    speak(Time)

def date():
    year = int(datetime.datetime.now().year)
    month = int(datetime.datetime.now().month)
    date = int(datetime.datetime.now().day)
    speak("The current date is:")
    speak(date)
    speak(month)
    speak(year)

def greeting():
    hour = datetime.datetime.now().hour
    if hour >=6 and hour <12:
        speak("Good morning sir!")
    elif hour >=12 and hour <18:
        speak("Good Afternoon sir!")
    elif hour >=18 and hour <24:
        speak("Good Evening sir!")
    else:
        speak("Good NIght sir!")
def wishme():
    speak("Welcome back sir!")
    time()
    date()
    greeting()
    speak("Cortana is here to give you a great service, please tellme how can i help you?")
#while True:
#    voice = int(input("Press 1 for male voice \npress 2 for female voice \n"))
#   #speak(audio) 
#   getvoices()
#wishme()

def takeCommandCMD():
    query = input("Please tell me how can i help you!\n")
    return query

def takeCommandMic():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening....")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizeing...")
        query = r.recognize_google(audio , language="hi-IN")
        query = r.recognize_google(audio , language="en-IN")
        print(query)
    except Exception as e:
        print(e)
        speak("Could you please say it again....")
        return "None"
    return query
def sendEmail(receiver, subject, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()   # TRANSPORT LAYER SECURITY (TLS)
    server.login(senderemail, epwd)
    email = EmailMessage()
    email['From'] = senderemail
    email['TO'] = receiver
    email['Subject'] = subject
    email.set_content(content)
    server.send_message(email)
    server.close()
    
def sendwhatsmsg(phone_no, message):
    Message = message
    wb.open('https://web.whatsapp.com/send?phone='+phone_no+'&text='+Message)
    sleep(10)
    pyautogui.press('enter')
    
def Perplexity():
    speak('What kind of information you want?')
    search = takeCommandMic()
    wb.open('https://www.perplexity.ai/search?q='+search)   
    
def google():
    speak('What should i search for?')
    on = takeCommandMic()
    wb.open('https://www.google.com/search?q='+on)    
    
def text2speech():
    text = clipboard.paste()
    print(text)
    speak(text)
    
def screenshot():
    name_img = tt.time()
    name_img = 'C:\\Users\\HP\\OneDrive\\Desktop\\Cortana Ai\\Cortana Ai\\screenshot\\{name_img}.png'
    img = pyautogui.screenshot(name_img)
    img.show()

def passwordgen():
    s1 = string.ascii_uppercase
    s2 = string.ascii_lowercase
    s3 = string.digits
    s4 = string.punctuation
    
    passlen = 8
    s =[]
    s.extend(list(s1))
    s.extend(list(s2))
    s.extend(list(s3))
    s.extend(list(s4))
    
    random.shuffle(s)
    newpass = ("".join(s[0:passlen]))
    print(newpass)
    speak(newpass)
    
def flip():
    speak("okay sir, fliping a coin")
    coin = ['heads', 'tails']
    toss =[]
    toss.extend(coin)
    random.shuffle(toss)
    toss = ("".join(toss[0])) 
    speak("i flipped the coin and you got"+toss)   
    
if __name__=="__main__":
     getvoices(2)
     #wishme()
     wakeword = "cortana"
     while True:
         query = takeCommandMic().lower()
         query = word_tokenize(query)
         print(query)
         if wakeword in query:
          
            if 'time' in query:
                time()
                
            elif 'date' in query:
                date()

            elif 'email' in query:
                email_list = {
                    'Bob':'raxas0502@gmail.com'
                }
                try:
                    speak("To who you want to send an email?")
                    name = takeCommandMic()
                    receiver = email_list[name]
                    speak("What is the subject of the mail?")
                    subject = takeCommandMic()
                    speak('what should i say?')
                    content = takeCommandMic()
                    sendEmail(receiver, subject, content)
                    speak("Email has been send")
                except Exception as e:
                    print(e)
                    speak("unable to end the email")
                    
            elif 'message' in query:
                user_name = {
                    'Joy': '+91 90331 12363'#add number main 
                }
                user_name = {
                    'Sahil': '+91 8735555174'#add manually number for sending messages
                }
                try:
                    speak("To who you want to send the whats app message?")
                    name = takeCommandMic()
                    phone_no = user_name[name]
                    speak("What is the message?")
                    message = takeCommandMic()
                    sendwhatsmsg(phone_no,message)
                    speak("message has been send")
                except Exception as e:
                    print(e)
                    speak("unable to end the message")
                    
            elif 'wikipedia' in query:
                speak('serching for wikipedia....')
                query = ' '.join(query)
                query = query.replace("wikipedia", " ")
                result = wikipedia.summary(query, sentences = 2)
                print(result)
                speak(result)                  
                    
            elif 'search' in query:
                Perplexity()       
                            
            elif 'on' in query:
                google()
                             
            elif 'youtube' in query:
                speak("What should i search for on youtube?")
                topic = takeCommandMic()
                pywhatkit.playonyt(topic)  
                        
            elif 'read' in query:
                text2speech()
                                
            elif 'opencode' in query:
                codepath = 'E:\\Sublime text\\Sublime Text\\sublime_text.exe'    
                os.startfile(codepath) 
                
            elif 'openbrave' in query:
                codepath = 'C:\\Program Files\\BraveSoftware\\Brave-Browser\\Application\\brave.exe' 
                os.startfile(codepath)
                
            elif 'joke' in query:
                speak(pyjokes.get_joke())
                    
            elif 'screenshot' in query:
                screenshot()
                
            elif 'remember that' in query:
                speak("What should i remember?")
                data = takeCommandMic()
                speak("You said me to remember that"+data)
                remember = open('data.txt','w')
                remember.write(data)
                remember.close()
                
            elif 'do you know anything' in query:
                remember = open('data.txt', 'r')
                speak("You told me to remember that" +remember.read())   
                
            elif 'password' in query:
                passwordgen() 
                
            elif 'flip' in query:
                flip()
                
            elif 'offline' in query:
                quit()