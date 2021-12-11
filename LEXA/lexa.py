import pywhatkit
import os
import webbrowser
import speech_recognition as sr
import pyttsx3
import pyaudio
import datetime
import wikipedia
from wikipedia.wikipedia import summary


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
# print(voices[1].id)



def speak (audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
      hour = int(datetime.datetime.now().hour)
      if hour>=0 and hour<12:
        speak("Good Morning!")

      elif hour>=12 and hour<18:
        speak("Good Afternoon!")   

      else:
        speak("Good Evening!")      

      speak('I am Lexa sir. Please tell me how may i help you')

def take_command():
    
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('Listening...')
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print('Recognizing...')
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        print(e)
        print('Say that again please..')
        return 'None'
    return query


if __name__ == "__main__":
    # speak("Aditya is good boy")
    wishMe()
    while True:
         query = take_command().lower()
          

         if 'time' in query:
             time = datetime.datetime().strftime('%H:%M:')
            #  print(time)
             speak('current time is' + time)


         elif 'wikipedia' in query:
             speak('Searching wikipedia..')
             query= query.replace("wikipedia", "")
             results = wikipedia.summary(query, sentences=3)
             print(results)
             speak(results)

         elif "play" in query:
             song = query.replace('play', '')
             engine.say('playing..' + song)
             pywhatkit.playonyt(song)
    

         elif 'open youtube' in query:
             webbrowser.open("youtube.com")    

         elif 'open google' in query:
             webbrowser.open("google.com")    

         elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com") 

         elif 'open github' in query:
            webbrowser.open("github.com")     

         elif 'music' in query:
            music_dir = 'A:\\Songs'
            songs = os.listdir(music_dir)
            # print(songs)    
            os.startfile(os.path.join(music_dir, songs[0]))

         elif 'open code' in query:
            codePath = "C:\\Users\\Aditya Malviya\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)  

         elif 'open pycharm' in query:
            pyPath = "C:\\Program Files\\JetBrains\\PyCharm Community Edition 2018.1.6\\bin\\pycharm.exe"
            os.startfile(pyPath) 

         elif 'open telegram' in query:
            telePath = "C:\\Users\\Aditya Malviya\\AppData\\Roaming\\Telegram Desktop\\Telegram.exe"
            os.startfile(telePath)  
         else:
             print('Please say it again..')    