import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import smtplib
import password
import gmail
import destination
import webbrowser 
import os
import pyautogui
import psutil

engine = pyttsx3.init()

p=password
g=gmail
d=destination

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def time():
    Time = datetime.datetime.now().strftime("%I:%M:%S")
    speak("the current time is:")
    speak(Time)

def date():
    year = int(datetime.datetime.now().year)
    month = int(datetime.datetime.now().month)
    date = int(datetime.datetime.now().day)
    speak(" current date is:")
    speak(date)
    speak(month)
    speak(year)

def recallme():
    #speak("wellcome Boss!")
   # time()
    #date()
    hour = datetime.datetime.now().hour
    if hour >=6 and hour<12:
        speak("Good morning !")
    elif hour >=12 and hour<16:
        speak("Good afternoon!")
    elif hour >=16 and hour<22:
        speak("Good evening!")
    else:
        speak("Good night!")
    speak("Sir!")
    speak("I'm your personal assistant Saze,how can i help you?")
    #speak("Thank you for calling me")

def takeCommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening....")
        r.pause_threshold=1
        audio=r.listen(source)
    try:
        print("Recognizing...")
        query=r.recognize_google(audio, language='en')
        print(query)
    except Exception as e:
        print(e)
        speak("Please repeat..")
        return "None"
    return query

def sendEmail(to, content):
    server=smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login(g, p)
    server.sendmail(g, to, content)
    server.close()

def screenshot():
    img = pyautogui.screenshot()
    img.save("C:\\Users\\RISHU SINGH\\Documents\\Jarvis\\file.png")

def cpu():
    usage = str(psutil.cpu_percent())
    speak('CPU ia at'+ usage)
    battery = psutil.sensors_battery()
    speak('Battery is at')
    speak(battery.percent )

if __name__ == '__main__':
    while True:
        recallme()
        query=takeCommand().lower();

        if 'time' in query:
            time()
        elif 'date' in query:
            date()
        elif 'wikipedia' in query:
            speak("Searching...")
            query=query.replace("wikipedia","")
            result=wikipedia.summary(query,sentences=4)
            print(result)
            speak(result)

        elif 'send email' in query:
            try:

                speak('what should i say sir...')
                Content=takeCommand()
                to=d
                sendEmail(to, content)
                speak('email has been sent successfully!')
            except Exception as e:
                print(e)
                speak('email has not been sent!')


        elif 'search in chrome' in query:
           speak("What should i  search ?")
           chromepath = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
           search = takeCommand().lower()
           webbrowser.get(chromepath).open_new_tab(search+'.com')

        elif 'log out from the system' in query:
            speak("do you really want to log out!")
            reply=takeCommand()
            if 'yes' in reply:
              os.system("shutdown -1")
            else:
                break

        elif 'shutdown' in query:
            os.system("shutdown /s /t 1")

        elif 'restart' in query:
            os.system("shutdown /r /t 1")

        elif 'play songs' in query:
            songs_dir='D:\\Music'
            songs=os.listdir(songs_dir)
            os.startfile(os.path.join(songs_dir, songs[0]))

        elif 'remember it' in query:
            speak("what should i remember!")
            data=takeCommand()
            speak("you asked me remember that"+data)
            remember=open('data.txt','w')
            remember.write(data)
            remember.close()

        elif 'did you remember anything' in query:
            remember=open('data.txt','r').read()
            speak("you asked me remember that" +remember.read())

        elif 'screenshot' in query:
            screenshot()
            speak("your img is saved.")

        elif 'cpu' in query:
            cpu()
        

        elif 'exit' in query:
            quit()
        else:
            speak('try again')

       # if 'open youtube' in query:
        #    speak('getting it sir')
         #   webbrowser.open('www.youtube.com')
        #elif 'open google' in query:
         #   speak("getting it sir")
          #  webbrowser.open('www.google.co.in')
        #elif 'open gmail' in query:
         #   speak("getting it sir")
          #  webbrowser.open('www.gmail.com')
        #elif 'how are in query' in query:
         #   stMsgs=['all great doing my stuff!', 'I am fine', 'Thank you']
          #  speak(random.choice(stMsgs))
        #elif 'email' in query:
         #   speak('who is the recipent? ')
          #  recipent = takeCommand()