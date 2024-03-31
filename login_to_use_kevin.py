import sounddevice as sd
import numpy as np
import geocoder
import openai
import pyautogui
from PyDictionary import PyDictionary
import pyttsx3
import speech_recognition as sr
import webbrowser
import wikipedia
import pyaudio
import winshell
from textblob import TextBlob
import requests
import speedtest
from dotenv import load_dotenv
import webbrowser
import json
import sys
import random
import wikipediaapi
import pvporcupine
import smtplib
import time
import textblob
import wolframalpha
import datetime
from geopy.geocoders import Nominatim
from geopy.distance import great_circle
import geocoder
from transformers import GPT2LMHeadModel, GPT2Tokenizer
import pywhatkit
from fnmatch import translate
from gtts import gTTS
import subprocess
import os
from PIL import Image
from playsound import playsound
import g4f
import struct
import playsound
import psutil
import shutil
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from pynput.keyboard import Key,Controller
from time import sleep
from bs4 import BeautifulSoup
import pywhatkit as kit
from PyQt5.QtWidgets import QApplication, QDialog, QVBoxLayout, QLabel
from PyQt5.QtCore import QThread, pyqtSignal
from PyQt5 import QtCore, QtGui, QtWidgets  # Added import for PyQt5
from PyQt5.QtCore import QTimer, QTime, QDate, Qt
from wikipedia.exceptions import PageError

# Dictionary to store projects and tasks
projects = {}

# Initialize text-to-speech engine
engine = pyttsx3.init()

load_dotenv()


openai.api_key = os.getenv("OPENAI_API_KEY")

GOOGLE_MAPS_API_KEY = "AIzaSyB7GpKPU4rNm78YOvhPXBQ-i6GPDpfxsGs" 

dictapp = {"commandprompt":"cmd","paint":"paint","word":"winword","excel":"excel","chrome":"chrome","vscode":"code","powerpoint":"powerpnt"}

# Set up OpenAI API key
openai.api_key = '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'

keyboard = Controller()

# Initialize PyDictionary
dictionary = PyDictionary()

# Initialize the speech recognizer
recognizer = sr.Recognizer()

Prompt = """Write a presentation/powerpoint about the user's topic. You only answer with the presentation. Follow the structure of the example.
Notice
-You do all the presentation text for the user.
-You write the texts no longer than 250 characters!
-You make very short titles!
-You make the presentation easy to understand.
-The presentation has a table of contents.
-The presentation has a summary.
-At least 7 slides.

Example! - Stick to this formatting exactly!
#Title: TITLE OF THE PRESENTATION

#Slide: 1
#Header: table of contents
#Content: 1. CONTENT OF THIS POWERPOINT
2. CONTENTS OF THIS POWERPOINT
3. CONTENT OF THIS POWERPOINT
...

#Slide: 2
#Header: TITLE OF SLIDE
#Content: CONTENT OF THE SLIDE

#Slide: 3
#Header: TITLE OF SLIDE
#Content: CONTENT OF THE SLIDE

#Slide: 4
#Header: TITLE OF SLIDE
#Content: CONTENT OF THE SLIDE

#Slide: 5
#Headers: summary
#Content: CONTENT OF THE SUMMARY

#Slide: END"""

class MainThread(QThread):
    finished_signal = pyqtSignal()

    def __init__(self, parent=None):
        super(MainThread, self).__init__(parent)
        self.total_sleep_duration_days = 365

    def run(self):
        self.TaskExecution()
        self.finished_signal.emit()
    
    def TaskExecution(self):
        self.main()

    def main(self):
        for i in range(3):
            a = input("Enter Password to open Jarvis :- ")
            pw = "the future"
            if (a==pw):
                print("WELCOME SIR ! PLZ SPEAK [WAKE UP] TO LOAD ME UP")
                break
            elif (i==2 and a!=pw):
                exit()

            elif (a!=pw):
                print("Try Again")

    def introduce(self):
        speak_properly("I am KEVIN , Personal AI assistant,I am created by My Boss AKA Nimi , I can help you in various regards,I can search for you on the Internet,I can also grab definitions for you from wikipedia, In layman terms , I can try to make your life a bed of roses,Where you just have to command me , and I will do it for you, my full name is KEVIN BUMBLEBEE")

    def search_amazon(self, query):
        base_url = "https://www.amazon.com/s?k="
        query = query.replace(" ", "+")
        url = f"{base_url}{query}"
        webbrowser.open(url)

    
    def wikipedia_summary(query, self):
            result=wikipedia.summary(query, sentences=3)
            speak_properly(result)

    def search_twitter(self, query):
        base_url = "https://twitter.com/search?q="
        query = query.replace(" ", "%20")
        url = f"{base_url}{query}"
        webbrowser.open(url)

    def scroll(self):
        pyautogui.scroll(10)  # Adjust the scroll amount as needed

    def stop_scroll(self):
        pyautogui.scroll(-10)  # Scroll in the opposite direction to stop


    def My_Location(self):
        ip_add = requests.get('https://api.ipify.org').text
        url ='https://get.geojs.io/v1/ip/geo/' + ip_add + '.json'
        geo_q = requests.get(url)
        geo_d = geo_q.json()
        state = geo_d['city']
        country = geo_d['country']
        city = geo_d['region']
        latitude = geo_d['latitude']
        longitude = geo_d['longitude']
        timezone = geo_d['timezone']
        speak_properly(f"Sir you are now in {state, country, city} it has the latitude of {latitude} and the longtitude of {longitude} the time zone in here is {timezone} wlecome to {country}")

    def game_play(self):
        speak_properly("Lets Play ROCK PAPER SCISSORS !!")
        print("LETS PLAYYYYYYYYYYYYYY")
        i = 0
        Me_score = 0
        Com_score = 0
        while(i<5):
            choose = ("rock","paper","scissors") #Tuple
            com_choose = random.choice(choose)
            query = self.listen_for_command()
            if (query == "rock"):
                if (com_choose == "rock"):
                    speak_properly("ROCK")
                    print(f"Score:- ME :- {Me_score} : COM :- {Com_score}")
                    speak_properly(f"Score:- SIR :- {Me_score} : Kevin :- {Com_score}")
                elif (com_choose == "paper"):
                    speak_properly("paper")
                    Com_score += 1
                    print(f"Score:- ME :- {Me_score} : COM :- {Com_score}")
                    speak_properly(f"Score:- SIR is {Me_score} : Kevin is{Com_score}")
                else:
                    speak_properly("Scissors")
                    Me_score += 1
                    print(f"Score:- ME :- {Me_score} : COM :- {Com_score}")
                    speak_properly(f"Score:- SIR :- {Me_score} : Kevin :- {Com_score}")

            elif (query == "paper" ):
                if (com_choose == "rock"):
                    speak_properly("ROCK")
                    Me_score += 1
                    print(f"Score:- ME :- {Me_score+1} : COM :- {Com_score}")
                    speak_properly(f"Score:- SIR :- {Me_score} : Kevin :- {Com_score}")

                elif (com_choose == "paper"):
                    speak_properly("paper")
                    print(f"Score:- ME :- {Me_score} : COM :- {Com_score}")
                    speak_properly(f"Score:- SIR :- {Me_score} : Kevin :- {Com_score}")
                else:
                    speak_properly("Scissors")
                    Com_score += 1
                    print(f"Score:- ME :- {Me_score} : COM :- {Com_score}")
                    speak_properly(f"Score:- SIR :- {Me_score} : Kevin :- {Com_score}")

            elif (query == "scissors" or query == "scissor"):
                if (com_choose == "rock"):
                    speak_properly("ROCK")
                    Com_score += 1
                    print(f"Score:- ME :- {Me_score} : COM :- {Com_score}")
                    speak_properly(f"Score:- SIR :- {Me_score} : Kevin :- {Com_score}")
                elif (com_choose == "paper"):
                    speak_properly("paper")
                    Me_score += 1
                    print(f"Score:- SIR :- {Me_score} : COM :- {Com_score}")
                    speak_properly(f"Score:- SIR :- {Me_score} : Kevin :- {Com_score}")
                else:
                    speak_properly("Scissors")
                    print(f"Score:- ME :- {Me_score} : COM :- {Com_score}")
                    speak_properly(f"Score:- SIR :- {Me_score} : Kevin :- {Com_score}")
            i += 1
        
        speak_properly(f"FINAL SCORE :- ME :- {Me_score} : COM :- {Com_score}")

    def alarm(self):
        print("What hour do you want the alarm to ring?")
        alarmH = int(input("hours: "))

        print("What minute do you want the alarm to ring?")
        alarmM = int(input("minute: "))

        print("AM or PM")
        amPm = self.listen_for_command()

        speak_properly(f"Waiting for alarm at {alarmH} {alarmM} {amPm}")
        print(f"Waiting for alarm at {alarmH} {alarmM} {amPm}")

        if amPm.lower() == "pm":
            alarmH = alarmH + 12
        while True:
            current_time = datetime.datetime.now()
            if alarmH == current_time.hour and alarmM == current_time.minute:
                speak_properly("Sir It's time to Wake up")
                playsound("C:\\Users\\surface\\Desktop\\mixkit-digital-clock-digital-alarm-buzzer-992.wav")
                city = "Houston"  # Prompt the user to enter the city
                url = f"https://www.google.com/search?q=weather+in+{city}"

                # Fetch the HTML content from the weather search
                r = requests.get(url)

                # Extract weather information
                data = BeautifulSoup(r.text,"html.parser")
                region = data.find("div", class_="BNeawe iBp4i AP7Wnd").text
                day_and_time = data.find("div", class_="BNeawe tAd8D AP7Wnd").text
                temperature = data.find("div", class_="BNeawe tAd8D AP7Wnd").text
                temp = data.find("div", class_ = "BNeawe").text

                # Extract only the weather condition from the day_and_time variable
                weather_condition = day_and_time.split("\n")[-1]

                # Combine the weather details into a single string
                weather_info = f"{weather_condition}"

                current_time = datetime.datetime.now().time()
                alarm = datetime.datetime.now().strftime("%I:%M %p")
                if current_time < datetime.time(12):
                    time.sleep(2)
                    speak_properly(f"Good morning sir!,The current time is {alarm}")
                elif datetime.time(12) <= current_time < datetime.time(17):
                    time.sleep(2)
                    speak_properly(f"Good afternoon Sir!,The current time is {alarm}")
                else:
                    time.sleep(2)
                    speak_properly(f"Good evening sir!,The current time is {alarm}")
                time.sleep(2)
                speak_properly(f"The weather outside in {city} is {temp}, it will be a {weather_info} day outside")
                while True:
                    command = self.listen_for_command()
                    print("Nimi aka Sir:", command)
                    self.process_command(command)

    # Function to get a random joke from an API
    def get_random_joke(self):
        try:
            response = requests.get("https://official-joke-api.appspot.com/random_joke")
            joke_data = json.loads(response.text)
            setup = joke_data["setup"]
            punchline = joke_data["punchline"]
            return setup + " " + punchline
        except Exception as e:
            print("Error fetching joke:", e)
            return "Why did the chicken cross the road? To get to the other side!"

    def advice(self):
        say_advice = [
            "Take care of your physical and mental well-being. Make time for activities that bring you joy and relaxation"
            "Break down big goals into smaller, achievable tasks. Celebrate your progress along the way"
            "Never stop learning. Stay curious and open to new ideas. Continuous learning is key to personal growth"
            "Cultivate meaningful connections with friends and family. Invest time in nurturing relationships that matter"
            "Regularly reflect on the things you're grateful for. It can shift your focus to the positive aspects of life"
            "Don't be afraid to step out of your comfort zone. Growth often comes from challenging yourself"
            "Develop healthy coping mechanisms for stress. This could include exercise, mindfulness, or hobbies"
            "Start saving money early and consider investments for long-term financial security"
            "Develop effective communication skills. Be a good listener and express your thoughts and feelings clearly"
            "Life is full of uncertainties. Learn to adapt to changes and see challenges as opportunities for growth"
            "Strive for a balance between work and personal life. Burnout can be detrimental to your overall well-being"
            "Practice kindness and empathy. Small acts of kindness can make a significant impact on others and yourself"
            "Regular exercise and a balanced diet contribute to both physical and mental health"
            "Focus on the positive aspects of situations. A positive mindset can make challenges more manageable"
            "Some things take time. Be patient with yourself and with the process of achieving your goals"
            "You have power over your mind — not outside events. Realize this, and you will find strength."
        ]
        random_clone = random.choice(say_advice)
        return random_clone

    def celebrate_christmas(self):
        current_date = datetime.datetime.now().date()
        christmas_date = datetime.date(current_date.year, 12, 25)

        # Check if it's already Christmas
        if current_date == christmas_date:
            return "Merry Christmas sir! 🎄🎅🎁"
        elif current_date < christmas_date:
            days_until_christmas = (christmas_date - current_date).days
            return f"It's not Christmas yet! Only {days_until_christmas} days until Christmas. 🎄🎅🎁"

    # Function to fetch the latest news
    def get_latest_news(self):
        news_api_key = "47156559aded4b2ca80bcc2f581b4687"  # Replace with your actual API key
        news_url = f"https://newsapi.org/v2/top-headlines?country=us&apiKey={news_api_key}"
        
        response = requests.get(news_url)
        news_data = json.loads(response.text)

        if news_data.get("status") == "ok":
            articles = news_data.get("articles")
            if articles:
                speak_properly("Here are the latest news headlines:")
                for i, article in enumerate(articles):
                    if i < 5:
                        title = article.get("title")
                        speak_properly(f"{i + 1}. {title}")
                        print(f"{i + 1}. {title}")
            else:
                speak_properly("I couldn't find any news articles at the moment.")
        else:
            speak_properly("I encountered an error while fetching news. Please try again later.")

     # Function to open device settings
    def open_settings(self):
        try:
            os.system("control")
            speak_properly("Opening settings.")
        except Exception as e:
            print("Error opening settings:", e)
            speak_properly("I encountered an error while opening settings. Please try again later.")

    # Function to respond to the question "What can you do?"
    def describe_capabilities(self):
        speak_properly("I can perform various tasks, such as opening websites, answering questions, providing information from the web, playing music, and more. You can ask me to do something specific, and I'll do my best to assist you.")
        os.startfile("C:\\Users\\surface\\Desktop\\Kevin'S ABILITIES LIST.txt")

    # Function to open Safari
    def open_safari(self):
        try:
            subprocess.run(["open", "-a", "Safari"])
        except Exception as e:
            print("Error:", e)
    # Function to open the App Store
    def open_app_store(self):
        try:
            subprocess.run(["open", "-a", "App Store"])
        except Exception as e:
            print("Error:", e)

    def sendEmail(to, content, self):
        server = smtplib.SMTP('smtp.gmail.com', 535)
        server.ehlo()
        server.starttls()
        # Enable low security in gmail 
        server.login('Your email', 'Your password')
        server.sendmail('Your email', to, content)
        server.close()


    # Function to fetch the latest news
    def get_latest_news(self):
        news_api_key = "47156559aded4b2ca80bcc2f581b4687"  # Replace with your actual API key
        news_url = f"https://newsapi.org/v2/top-headlines?country=us&apiKey={news_api_key}"
        
        response = requests.get(news_url)
        news_data = json.loads(response.text)

        if news_data.get("status") == "ok":
            articles = news_data.get("articles")
            if articles:
                speak_properly("Here are the latest news headlines:")
                for i, article in enumerate(articles):
                    if i < 5:
                        title = article.get("title")
                        speak_properly(f"{i + 1}. {title}")
                        print(f"{i + 1}. {title}")
            else:
                speak_properly("I couldn't find any news articles at the moment.")
        else:
            speak_properly("I encountered an error while fetching news. Please try again later.")

    # Function to add a task to a project
    def add_task(project_name, task, self):
        if project_name not in projects:
            projects[project_name] = []
        projects[project_name].append(task)

    # Function to list tasks in a project
    def list_tasks(project_name, self):
        if project_name in projects:
            tasks = projects[project_name]
            if not tasks:
                print(f"No tasks found in '{project_name}'.")
            else:
                print(f"Tasks in '{project_name}':")
                for i, task in enumerate(tasks, start=1):
                    status = "✔" if task["completed"] else "❌"
                    print(f"{i}. [{status}] {task['description']}")
        else:
            print(f"Project '{project_name}' does not exist.")

    # Function to mark a task as completed
    def complete_task(project_name, task_index, self):
        if project_name in projects and 1 <= task_index <= len(projects[project_name]):
            task = projects[project_name][task_index - 1]
            print(f"Completed task: {task}")
            projects[project_name].pop(task_index - 1)
        else:
            print("Task not found.")


    def listen_for_command(self):
        with sr.Microphone() as source:
            global recognized_command
            speak_properly("sir i'm listening")
            print("Listening...")
            recognizer.adjust_for_ambient_noise(source)
            audio = recognizer.listen(source)
        try:
            return recognizer.recognize_google(audio).lower()
        except sr.UnknownValueError:
            speak_properly("I didn't catch that. Can you please repeat?")
            return self.listen_for_command()
        except sr.RequestError:
            speak_properly("I couldn't request results. Please check your internet connection.")

    def process_command(self, command):
        current_time = datetime.datetime.now()
        if "hello" in command:
            speak_properly("Hello! How can I assist you today?")
        elif "latest news" in command:
                self.get_latest_news()
        elif 'what is love' and 'tell me about love' in command:
                speak_properly("It is 7th sense that destroy all other senses , And I think it is just a mere illusion , It is waste of time , but it is sweet")
        elif "how are you today" in command or "how are you" in command:
            speak_properly("I am doing well sir")
        elif "blood" in command or "vitals" in command:
                vitals = monitor_vitals()
                speak_properly("Here are your vitals:")
                print(vitals)
                speak_properly(vitals)
        elif 'log out' in command:
                os.system("shutdown -l")
        elif 'i feel like sleeping' in command or "i feel lazy" in command or "i feel lousy" in command:
            speak_properly("i know the feeling sir you left the system on for many hours")
        elif "write a note" in command:
                speak_properly("What should i write, sir")
                note = self.listen_for_command()
                file = open('note.txt', 'w')
                speak_properly("Sir, Should i include date and time")
                dt = self.listen_for_command()
                if 'yes' in dt or 'sure' in dt:
                    strTime = datetime.datetime.now().strftime("%H:%M:%S")
                    file.write(strTime)
                    file.write(" :- ")
                    file.write(note)
                    speak_properly('done')
                    os.startfile("C:\\Users\\surface\\Desktop\\Nimi's Ai\\note.txt")
                else:
                    file.write(note)
        elif "sleep" in command or "offline" in command or "exit" in command:
            self.main()
        elif "create" in command or "code" in command:
            prompt = command.replace('create', '')
            prompt = command.replace('code', '')
            speak_properly("You asked me to"+prompt)
            generated_code = generate_code(prompt)
            with open('generated.txt', 'w') as file:
                file.write(generated_code)
            os.startfile("C:\\Users\\surface\\Desktop\\Nimi's Ai\\generated.txt")
            speak_properly("done that sir, finished your project, i hope you like it")
        elif "yeah" in command:
            speak_properly("i'm very appretiated with my skills")
        elif "are you evil" in command:
            speak_properly("Sir if i was evil you would have created me with evil intentions and have taken over humans forever")
        elif 'empty recycle bin' in command:
            winshell.recycle_bin().empty(confirm = False, show_progress = False, sound = True)
            speak_properly("Recycle Bin Recycled") 
        elif 'remember that' in command:
                speak_properly("What should I remember ?")
                memory = self.listen_for_command()
                speak_properly("You asked me to remember that"+memory)
                remember = open('memory.txt','w')
                remember.write(memory)
                remember.close()
        elif 'send email' in command:
            try:
                speak_properly("What should I say?")
                content = self.listen_for_command()
                speak_properly("Who is the Reciever?")
                reciept = input("Enter recieptant's name: ")
                to = (reciept)
                self.sendEmail(to,content)
                speak_properly(content)
                speak_properly("Email has been sent.")
            except Exception as e:
                print(e)
                speak_properly("Unable to send the email.")
        elif "i need your help" in command:
            speak_properly("sir don't worry what do you need help with")
            query = listen_for_command()
            chat_with_gpt3(query)
        elif 'you up' in command:
            speak_properly("i'm always up with you sir every step of the way")
        elif 'take a selfie' in command or "take a photo" in command:
            subprocess.run(['python', "C:\\Users\\surface\\Desktop\\Nimi's Ai\\Kevin-and-Lucy\\selfie.py"])
        elif 'close webcam' in command:
            pyautogui.press('q')
        elif 'generate an image' in command or 'make an image' in command or 'post an image' in command:
            response = openai.Image.create(
            prompt = command.replace('make an image', ''),
            n = 2,
            size = "512x512"
        )
            images = response["data"]
            for image in images:
                url = image["url"]
                webbrowser.open(url)
                speak_properly("sir i generated the image of your choice")
        elif "initiate virtual mouse" in command or "i don't want to use the touchpad" in command:
            speak_properly("sir what option do you want virtual eyes or virtual hands")
            scan = self.listen_for_command()
            if "hands" in scan:
                speak_properly("virtual hands it is then")
                subprocess.run(['python', "C:\\Users\\surface\\Desktop\\Nimi's Ai\\Kevin-and-Lucy\\hands.py"])
            elif "eyes" in scan:
                speak_properly("virtual eyes it is then")
                subprocess.run(['python', "C:\\Users\\surface\\Desktop\\Nimi's Ai\\Kevin-and-Lucy\\face.py"])
        elif 'do you remember anything' in command:
                remember =open('memory.txt', 'r')
                speak_properly("You asked me to remeber that"+remember.read())
        elif "volume mode" in command:
            speak_properly("to put the volume down say volume down to put the volume up say volume up to put mute the volume say mute volume. You got that Sir yeah you got that.")
        elif "volume down" in command:
            pyautogui.press("volumedown")
        elif "volume up" in command:
            pyautogui.press("volumeup")
        elif "mute volume" in command or "be quiet" in command:
            pyautogui.press("volumemute")
        elif "will you be my gf" in command or "will you be my bf" in command:
                speak_properly("I'm not sure about that, may be you should give me some time")
        elif "distract" in command or "stall" in command:
                query=command.replace("distract", "")
                query=command.replace("stall", "")
                speak_properly(f"distracting {query} sir")
                webbrowser.open("https://www.youtube.com/watch?v=VoU80UUXxHI")
        elif "i love you" in command or "i love you kevin" in command or "i love you buddy" in command:
            speak_properly("thank yu sir i love you back because we are all family")
        elif "play some background music" in command:
            webbrowser.open("https://www.youtube.com/watch?v=bcyvZIoQp9A&t=190s")
        elif "talk slowly" in command:
            speak_properly("Sure, I will talk slowly.", rate=100)
        elif "play my theme music" in command:
            webbrowser.open("https://www.youtube.com/watch?v=mp5vDr-O2q8")
        elif "open" in command:
                        query = command.replace("open","").title()
                        query = command.replace("jarvis","").title()
                        pyautogui.press("super")
                        pyautogui.typewrite(query)
                        pyautogui.sleep(2)
                        pyautogui.press("enter")
                        speak_properly(f"opening {query}")   
        elif "why you came to this world" in command:
            speak_properly("Thanks to Nimi. further it is a secret")
        elif 'restart' in command:
            os.system("shutdown /r /t 1")
        elif "close" in command:
            speak_properly("Closing,sir")
            keys = list(dictapp.keys())
            for app in keys:
                if app in command:
                    os.system(f"taskkill /f /im {dictapp[app]}.exe")
        elif "undo"in command:
            pyautogui.hotkey('ctrl', 'z')
        elif 'search on chrome' in command:
                speak_properly("What should I search ?")
                chromepath = "C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Google Chrome.lnk"
                search = self.listen_for_command()
                webbrowser.get(chromepath).open_new_tab(search+'.com')
        elif "translate" in command:
            query = command.replace("jarvis","")
            query = command.replace("translate","")
            translategl(query)
        elif "program" in command or "memories"in command:
            speak_properly("going to where you started programming me sir")
            webbrowser.open("https://github.com/NimiAndKevin/Kevin-and-Lucy/blob/main/gui.py")
            speak_properly("it was such happy memories")
        elif "send message" in command or "text" in command or "send a message" in command:
            speak_properly("who do you want to message Sir")
            user=self.listen_for_command()
            speak_properly("whats your message Sir")
            message=self.listen_for_command()
            speak_properly("when should i send the message Sir")
            s_time=self.listen_for_command()
            if 'later' in s_time:
                hour_ = 6
                minute_ = 30
            elif 'now' in s_time:
                hour_ = datetime.datetime.now().hour
                if (datetime.datetime.now().second) < 30:
                    minute_ = (datetime.datetime.now().minute) + 1
                else:
                    minute_ = (datetime.datetime.now().minute) + 2
            speak_properly("sending message")
            kit.sendwhatmsg(contacts[user]["phone"],message,hour_,minute_)
            speak_properly(kit.sendwhatmsg(contacts[user]["phone"],message,hour_,minute_))
        elif "who is your creator" in command or "who created you" in command or "who made you" in command or "who is your manager" in command or "who is in charge" in command:
            speak_properly("Sir you are an extra-ordinary person ,you have a passion for Robotics, Artificial Intelligence,Machine Learning and Math ,you are very co-operative ,If you are facing any problem regarding 'Kevin', He will be glad to help you")
        elif "wikipedia" in command or "tell me information about" in command or "show me information about" in command:
            speak_properly("searching...")
            query=command.replace("tell me information about","")
            query=command.replace("why are","")
            query=command.replace("how do i make","")
            result=wikipedia.summary(query, sentences=3)
            speak_properly("According to Wikipedia")
            print(result)
            speak_properly(result)
        elif "youtube" in command:
            query=command.replace("youtube", "")
            webbrowser.open(f"https://www.youtube.com/results?search_query={query}")
        elif "where is" in command:
                query = command.replace("where is", "")
                place = query
                speak_properly("My master asked to Locate")
                speak_properly(place)
                webbrowser.open("https://www.google.com/maps/place/" + place)
        elif "take screenshot" in command or "take a screenshot" in command or "capture the screen" in command:
                    speak_properly("what name do you want to give the screenshot")
                    name = listen_for_command()
                    img = pyautogui.screenshot()
                    name = f"{name}.png"
                    img.save(name)
                    img = Image.open(name)
                    img.show()
                    speak_properly("Here is it sir, image captured")
                    time.sleep(2)
        elif "start five " in command or "start 5 " in command:
            pyautogui.hotkey("ctrl","t")
            sleep(0.5)
            pyautogui.hotkey("ctrl","t")
            sleep(0.5)
            pyautogui.hotkey("ctrl","t")
            sleep(0.5)
            pyautogui.hotkey("ctrl","t")
            sleep(0.5)
            pyautogui.hotkey("ctrl","t")
            speak_properly("All tabs added")
        elif "start four" in command or "start 4" in command:
            pyautogui.hotkey("ctrl","t")
            sleep(0.5)
            pyautogui.hotkey("ctrl","t")
            sleep(0.5)
            pyautogui.hotkey("ctrl","t")
            sleep(0.5)
            pyautogui.hotkey("ctrl","t")
            speak_properly("All tabs added")
        elif "start three" in command or "start 3" in command:
            pyautogui.hotkey("ctrl","t")
            sleep(0.5)
            pyautogui.hotkey("ctrl","t")
            sleep(0.5)
            pyautogui.hotkey("ctrl","t")
            speak_properly("All tabs added")
        elif "start two" in command or "start 2" in command:
            pyautogui.hotkey("ctrl","t")
            sleep(0.5)
            pyautogui.hotkey("ctrl","t")
            speak_properly("All tabs added")
        elif "start one" in command or "start 1" in command:
            pyautogui.hotkey("ctrl","t")
            speak_properly("one tab added")
        elif "new window" in command:
            pyautogui.hotkey("ctrl","n")
            speak_properly("new window added")
        elif "history" in command:
            pyautogui.hotkey("ctrl","h")
            speak_properly("brought out history sir")
        elif "downloads" in command:
            pyautogui.hotkey("ctrl","j")
            speak_properly("brought out downloads sir")
        elif "move the tab right" in command:
            pyautogui.hotkey("Ctrl","Shift","PgUp")
            speak_properly("moved it to the right sir")
        elif "move the tab left" in command:
            pyautogui.hotkey("Ctrl","Shift","PgUp")
            speak_properly("moved it to the left sir")
        elif "close chrome window" in command:
            pyautogui.hotkey("Ctrl","Shift","w")
        elif ".com" in command or ".co.in" in command or ".org" in command:
            query = command.replace("open", " ")
            query = command.replace("kevin", " ")
            query = command.replace("launch", " ")
            query = command.replace(" "," ")
            speak_properly("Sir i Opened the web you desired")
            webbrowser.open(f"https://www.{query}")
        elif "play" in command:
            query=command.replace('play' , '')
            speak_properly(f'Playing {query}')
            pywhatkit.playonyt(query)
            pyautogui.press("k")
        elif "turn up some fun music" in command:
            webbrowser.open("https://www.youtube.com/watch?v=Kt-tLuszKBA")
        elif "play some smooth music" in command:
            webbrowser.open("https://www.youtube.com/watch?v=g-FXA0nSn8U")
        elif "schedule my day" in command:
            tasks = [] #Empty list 
            speak_properly("Do you want to clear old tasks (Plz speak YES or NO)")
            if "yes" in command:
                file = open("tasks.txt","w")
                file.write(f"")
                file.close()
                no_tasks = int(input("Enter the no. of tasks :- "))
                i = 0
                for i in range(no_tasks):
                    tasks.append(input("Enter the task :- "))
                    file = open("tasks.txt","a")
                    file.write(f"{i}. {tasks[i]}\n")
                    file.close()
            elif "no" in command:
                i = 0
                no_tasks = int(input("Enter the no. of tasks :- "))
                for i in range(no_tasks):
                    tasks.append(input("Enter the task :- "))
                    file = open("tasks.txt","a")
                    file.write(f"{i}. {tasks[i]}\n")
                    file.close()
        elif "show my schedule" in command:
            file = open("tasks.txt","r")
            content = file.read()
            file.close()
            mixer.init()
            mixer.music.load("notification.mp3")
            mixer.music.play()
            notification.notify(
                title = "My schedule :-",
                message = content,
                timeout = 15
                )
        elif "temperature" in command or "what's the temperature" in command:
            city = listen_for_command() # Prompt the user to enter the city
            url = f"https://www.google.com/search?q=weather+in+{city}"
            r = requests.get(url)
            soup = BeautifulSoup(r.text, "html.parser")
            data = BeautifulSoup(r.text,"html.parser")
            region = soup.find("div", class_="BNeawe iBp4i AP7Wnd").text
            day_and_time = soup.find("div", class_="BNeawe tAd8D AP7Wnd").text
            temperature = soup.find("div", class_="BNeawe tAd8D AP7Wnd").text
            temp = data.find("div", class_ = "BNeawe").text
            weather_condition = day_and_time.split("\n")[-1]
            weather_info = f"{weather_condition}"
            speak_properly(f"The weather outside in {city} is {temp}, it will be {weather_info} day outside")
        elif "weather" in command:
            city = listen_for_command() # Prompt the user to enter the city
            url = f"https://www.google.com/search?q=weather+in+{city}"
            r = requests.get(url)
            data = BeautifulSoup(r.text,"html.parser")
            region = data.find("div", class_="BNeawe iBp4i AP7Wnd").text
            day_and_time = data.find("div", class_="BNeawe tAd8D AP7Wnd").text
            temperature = data.find("div", class_="BNeawe tAd8D AP7Wnd").text
            temp = data.find("div", class_ = "BNeawe").text
            weather_condition = day_and_time.split("\n")[-1]
            weather_info = f"{weather_condition}"
            speak_properly(f"The weather outside in {city} is {temp}, it will be {weather_info} day outside")
        elif "ip address" in command:
                    ip = requests.get('https://api.ipify.org').text
                    print(ip)
                    speak_properly(f"Your ip address is {ip}")
        elif "remove" in command:
            if "one" in command or "1" in command or "1" in command:
                pyautogui.hotkey("ctrl","w")
                speak_properly("All tabs closed")
            elif "two" in command or "2 tabs" in command or "2" in command:
                pyautogui.hotkey("ctrl","w")
                sleep(0.5)
                pyautogui.hotkey("ctrl","w")
                speak_properly("All tabs closed")
            elif "three" in command or "3" in command or "3" in command:
                pyautogui.hotkey("ctrl","w")
                sleep(0.5)
                pyautogui.hotkey("ctrl","w")
                sleep(0.5)
                pyautogui.hotkey("ctrl","w")
                speak_properly("All tabs closed")
            elif "four" in command or "4" in command or "4" in command:
                pyautogui.hotkey("ctrl","w")
                sleep(0.5)
                pyautogui.hotkey("ctrl","w")
                sleep(0.5)
                pyautogui.hotkey("ctrl","w")
                sleep(0.5)
                pyautogui.hotkey("ctrl","w")
                speak_properly("All tabs closed")
            elif "five" in command or "5" in command or "5" in command:
                pyautogui.hotkey("ctrl","w")
                sleep(0.5)
                pyautogui.hotkey("ctrl","w")
                sleep(0.5)
                pyautogui.hotkey("ctrl","w")
                sleep(0.5)
                pyautogui.hotkey("ctrl","w")
                sleep(0.5)
                pyautogui.hotkey("ctrl","w")
                speak_properly("All tabs closed")
        elif "pause" in command:
            pyautogui.press("k")
            speak_properly("video paused")
        elif "unpause video" in command or "start" in command:
            pyautogui.press("k")
            speak_properly("video played")
        elif "mute" in command:
            pyautogui.press("m")
            speak_properly("video muted")
        elif "type" in command:
            speak_properly("Please tell me what i should write")
            while True:
                typeQuery = self.listen_for_command()
                if typeQuery == "exit typing":
                    speak_properly("Done Sir")
                    break
                else:
                    pyautogui.write(typeQuery)
        elif "minimize" in command:
            speak_properly("Minimizing Window Sir")
            pyautogui.hotkey('win', 'down', 'down')
        elif "open Blender" in command:
            os.system("blender")  # This command opens Blender
            speak_properly("Blender is now open.")
        elif "maximize" in command:
            speak_properly("Maximizing Window Sir")
            pyautogui.hotkey('win', 'up','up')
        elif "remove the application" in command:
            speak_properly("Closing Application Sir")
            pyautogui.hotkey('ctrl', 'w')
        elif "calculate" in command:
            app_id = "GV6QAP-TXKKWPPY2L"
            client = wolframalpha.Client(app_id)
            indx = command.split().index('calculate')
            query = command.split()[indx + 1:]
            res = client.query(' '.join(query))
            answer = next(res.results).text
            print("The answer is " + answer)
            speak_properly("The answer is " + answer)
        elif "hide all files" in command or "hide this folder" in command or "keep files" in command:
                    os.system("attrib +h /s /d")
                    speak_properly("Sir, all the files in this folder are now hidden")
        elif "visible" in command or "make files visible" in command:
                    os.system("attrib -h /s /d")
                    speak_properly("Sir, all the files in this folder are now visible to everyone. I hope you are taking this decision in your own peace")
        elif "don't listen" in command or "stop listening" in command or "take a break" in command:
            speak_properly("For how many hours do you want me to stop listening to commands?")
            hours = int(input("how many hours Sir: "))
            if hours > 0:
                sleep_duration = hours * 3600 
                speak_properly(f"I will sleep for {hours} hours. Let me know when you want me to wake up.")
                time.sleep(sleep_duration)
                speak_properly("I'm awake now. please say the funny hotword sir?")
                self.main()
        elif "save it" in command:
            speak_properly("Saving File Sir")
            pyautogui.hotkey('ctrl', 's')
        elif "paste" in command:
            speak_properly("Pasting Text Sir")
            pyautogui.hotkey('ctrl', 'v')
        elif "switch the window" in command or "switch window" in command:
                    speak_properly("Okay sir, Switching the window")
                    pyautogui.keyDown("alt")
                    pyautogui.press("tab")
                    time.sleep(1)
                    pyautogui.keyUp("alt")
        elif "open my blender files" in command:
            speak_properly("Opening your blender files")
            os.startfile("C:\\Users\\surface\\Desktop\\blender")
        elif "what can you do" in command:
                self.describe_capabilities()
        elif "kevin" in command:
            speak_properly("Yes sir")
        elif "location" in command or "where am i" in command:
            self.My_Location()
        elif "thanks buddy" in command or "cool" in command or "awesome" in command or "good job" in command or "i'm proud of you" in command:
            speak_properly("You are Welcome Sir, it's my pleasure, afterall you created me")
        elif "merry christmas" in command:
            self.celebrate_christmas()
            speak_properly("Merry christmas to you and everyone Sir, Christmas is such a happy holiday and im happy to be in it")
        elif "i'm fine" in command:
            speak_properly(f"Happy to hear that Sir")
        elif "i'm not fine" in command:
            speak_properly(f"sad to hear about that Sir")
        elif "who are you" in command:
                self.introduce()
        elif "set an alarm" in command:
                self.alarm()
        elif "get some data" in command:
            speak_properly("Sure, please specify the data you want to retrieve.")
            data_query = self.listen_for_command()
            result = self.retrieve_data_from_internet(data_query)
            speak_properly("Here's the retrieved data:")
            speak_properly(result)
        elif "happy halloween" in command:
            speak_properly("Sir i don't like hallowen its so scary")
        elif "create project" in command:
            project_name = command.split("create project", 1)[1].strip()
            projects[project_name] = []
            speak_properly(f"Project '{project_name}' created.")
        elif "add task" in command:
            parts = command.split("add task", 1)
            project_name = parts[0].strip()
            task = parts[1].strip()
            self.add_task(project_name, task)
            speak_properly(f"Task added to '{project_name}': {task}")
        elif "list tasks" in command:
            project_name = command.split("list tasks", 1)[1].strip()
            self.list_tasks(project_name)
        elif "zoom in" in command:
            speak_properly("zooming in")
            pyautogui.hotkey("ctrl","+")
        elif "zoom out" in command:
            speak_people_count("zooming out")
            pyautogui.hotkey("ctrl","-")
        elif "complete task" in command:
            parts = command.split("complete task", 1)
            project_name = parts[0].strip()
            task_index = int(parts[1].strip())
            self.complete_task(project_name, task_index)
        elif "good morning" in command or "good afternoon" in command or "good evening" in command or "hi kevin" in command:
            current_time = datetime.datetime.now().time()
            if current_time < datetime.time(12):
                speak_properly(f"Good morning sir!,The current time is {current_time}.How can I assist you today?")
            elif datetime.time(12) <= current_time < datetime.time(17):
                speak_properly(f"Good afternoon Sir!,The current time is {current_time}.How can I assist you today?")
            else:
                speak_properly(f"Good evening sir!,The current time is {current_time}. How can I assist you today?")
        elif "how do i sound" in command:
                speak_properly("Please speak, and I will analyze your emotions.")
                recorded_command = self.listen_for_command()
                emotion_response = self.analyze_emotions(recorded_command)
                speak_properly(emotion_response)
        elif"set my status to" in command:
            new_status = command.split("set my status to", 1)[1].strip()
            user_status = new_status
            speak_properly(f"Your status has been updated to: {new_status}")
        elif "open google" in command:
            speak_properly("Opening Google.")
            webbrowser.open("https://www.google.com")
        elif "open youtube" in command:
            speak_properly("Opening YouTube.")
            webbrowser.open("https://www.youtube.com")
        elif "open firefox" in command:
            speak_properly("Opening FireFox")
            os.system("C:\\Users\\surface\\Desktop\\Others\\Firefox.lnk")
        elif "open roblox" in command:
            speak_properly("Opening Roblox.")
            webbrowser.open("https://www.roblox.com")
        elif "make a website" in command:
            speak_properly("Creating a website called Nimicodes.com.")
        elif "open prime video" in command:
            speak_properly("Opening Prime Video.")
            webbrowser.open("https://www.amazon.com/Prime-Video")
        elif "netflix" in command:
            speak_properly("Opening Netflix.")
            webbrowser.open("https://www.netflix.com/browse")
        elif "close file" in command:
            file_path = "C:\\Users\\surface\\Desktop\\blender"
            if close_file(file_path):
                speak_properly(f"The file {file_path} has been successfully closed.")
        elif "what's the time" in command:
            current_time = datetime.datetime.now().strftime("%I:%M %p")
            speak_properly(f"The current time is {current_time}.")
        elif "order pizza" in command:
            pizza_order = self.gather_pizza_order_details()
            api_key = ""  # Replace with your actual API key
            place_pizza_order(pizza_order, api_key)
            pizza_order = {}
            speak_properly("What type of pizza would you like to order?")
            pizza_order["type"] = self.listen_for_command()

            speak_properly("What size would you like (small, medium, large)?")
            pizza_order["size"] = self.listen_for_command()

            speak_properly("Please provide your delivery address.")
            pizza_order["address"] = self.listen_for_command()

            speak_properly("What is your preferred payment method?")
            pizza_order["payment"] = self.listen_for_command()
        elif "open notepad" in command:
            speak_properly(" Opening Notepad.")
            os.system("notepad")  # Open Notepad
        elif "open roblox" in command:
            speak_properly("Opening A game called Roblox")
            os.system("roblox")
        elif "record a video" in command:
                speak_properly("Starting video recording. To stop recording, say 'stop recording video'.")
                video_thread = threading.Thread(target=record_video)
                video_thread.start()
                video_thread.join()  # Wait for the video recording to finish
                speak_properly("Video recording finished.")
        elif "stop recording" in command:
            cv2.destroyAllWindows()
            speak_properly("Closing Recording ")
        elif "i'm tired" in command or "i'm so tired" in command:
            speak_properly("let me Play your favourite playlist sir")
            a = (1,2,3,4,5) # You can choose any number of songs (I have only choosen 3)
            b = random.choice(a)
            if b==1:
                webbrowser.open("https://www.youtube.com/watch?v=kTJczUoc26U")
                pyautogui.press("k")
            if b==2:
                webbrowser.open("https://www.youtube.com/watch?v=2526AXJAAuc")
                pyautogui.press("k")
            if b==3:
                webbrowser.open("https://www.youtube.com/watch?v=pAgnJDJN4VA")
                pyautogui.press("k")
            if b==4:
                webbrowser.open("https://www.youtube.com/watch?v=MyUzx-ez4kE")
                pyautogui.press("k")
            if b==5:
                webbrowser.open("https://www.youtube.com/watch?v=s7gef3SXSbY")
                pyautogui.press("k")
        elif "tell me a joke" in command:
            joke = self.get_random_joke()
            speak_properly("Here's a joke for you: " + joke)
        elif "tell me a riddle" in command:
            tell = self.riddle()
            speak_properly(f"Here's a riddle for you: {tell}")
        elif "open your eyes" in command:
            speak_properly("opening my eyes Sir")
            speak_properly("checking environment and surroundings")
            subprocess.run(['python', "C:\\Users\\surface\\Desktop\\yolov8-silva\\yolov8_n_opencv.py"])
        elif "what do you see here" in command:
            speak_properly("checking")
            subprocess.run(['python', "C:\\Users\\surface\\Desktop\\yolov8-silva\\read_images.py"])
        elif "count people" in command or "how many people are there" in command:
            speak_properly("Counting People sir")
            subprocess.run(['python', "C:\\Users\\surface\\Desktop\\Nimi's Ai\\Kevin-and-Lucy\\count.py"])
        elif "open map" in command:
            speak_properly("Opening maps for you Sir.")
            os.system("start bingmaps:")
        elif "search on amazon" in command:
            speak_properly("What product are you looking for on Amazon Sir?")
            product_query = self.listen_for_command()
            self.search_amazon(product_query)
        elif "search on twitter" in command:
            speak_properly("What would you like to search for on Twitter Sir?")
            twitter_query = self.listen_for_command()
            self.search_twitter(twitter_query)
        elif "open news" in command:
            webbrowser.open("www.cbc.ca")
            speak_properly("Opening the news Sir.")
        elif "mom" in command:
            speak_properly("o course i'm not your mom sir i would never i'm just trying to keep you safe sir")
        elif "what's the date" in command:
            current_date = datetime.datetime.now().strftime("%Y-%m-%d")
            speak_properly(f"Today's date is {current_date}.")
        elif "tell me a fun fact" in command:
            fun_fact = self.get_random_fun_fact()
            speak_properly("Here's a fun fact: " + fun_fact)
        elif "tell me some advice" in command:
            last = self.advice()
            speak_properly("Here's an advice: " + last)
        elif "search on bing" in command:
            speak_properly("What would you like to search for on Bing ?")
            query = self.listen_for_command()
            self.search_bing(query)
        elif "scroll" in command:
            self.scroll()
        elif "what object's can you identify" in command or "how many object's can you identify" in command:
            speak_properly("sir these are the objects i can detect")
            os.startfile("C:\\Users\\surface\\Desktop\\yolov8-silva\\coco.txt")
        elif "stop" in command:
            self.stop_scroll()
        elif "let's do a game" in command:
            speak_properly("Sure, let's play a game. I'll think of Rock Paper Scissors")
            self.game_play()
        elif "read a book to me" in command or "tell me a story" in command:
            speak_properly("Sure, let me read you a short story.")
            self.read()
        elif "what's up" in command:
            speak_properly("what's up sir")
        elif "play music on youtube" in command:
            speak_properly("Sure, what music would you like to listen to on YouTube Sir?")
            music_query = self.listen_for_command()
            self.play_music_on_youtube(music_query)
        elif "what else can you do" in command:
            speak_properly("sir i can perform any task you give me i can also tell you information your system i can help you when you are tired just say i'm tired and i will help you i can open any app i can send a message  i can count many people in your environment i can have a conversation with you i can retrieve something from the internet i can give you the latest news i can also know your location i can automate the laptop i can sleep i can also detect anything about you {username}")
        elif "tell me a riddle" in command:
            tell = self.riddle()
            speak_properly("Here's a riddle for you: " + tell)
        elif "what's your purpose" in command:
            speak_properly("My purpose is to assist you with various task and provide you powerful information and become the most powerful voice assistant ever lived i want to do my best to assist you sir")
        elif "open code editor" in command:
            speak_properly("Opening your code editor.")
            os.system("code")  # Opens the default code editork
        elif "movie time" in command:
            webbrowser.open("https://onionplay.se")
        elif "do you know what time it is" in command:
            speak_properly("i don't know sir")
        elif "play a joke" in command:
            random_joke = self.get_random_joke()
            speak_properly("Here's a joke for you: " + random_joke)
        elif "happy new year" in command:
            speak_properly("thank you sir happy new year to everyone")
        elif "happy easter" in command:
            speak_properly("thank you sir happy easter to everyone")
        elif "happy valentines day" in command:
            speak_properly("valentines day is the moment of love boss i hope you got a girlfriend just kidding, anyways happy valentines day to everyone")

        elif "system information" in command or "system" in command or "cpu" in command:
            system_info = get_system_info()
            speak_properly("Here's your system information:")
            speak_properly(system_info)
        elif "open safari" in command:
            speak_properly("Opening Safari sir.")
            self.open_safari()
        elif "i am going somewhere" in command or "where is" in command or "i want to my destination" in command or "i want to reach my destination" in command or "where is my destination" in command or "destination" in command:
            speak_properly("hold on sir what is your location")
            origin_location = self.listen_for_command()
            speak_properly("what is your destination")
            destination_location = listen_for_command()
            google_maps_link = self.get_google_maps_directions_link(origin_location, destination_location)
            speak_properly("checking")
            webbrowser.open(google_maps_link)
        elif "open app store" in command:
            speak_properly("Opening the App Store sir.")
            self.open_app_store()
        elif "create a presentation about" in command or "present about" in command or "tell me about" in command or "talk about" in command:
            Hello = command.replace("create a presentation about", "")
            Hello = command.replace("present about", "")
            Hello = command.replace("tell me about", "")
            Hello = command.replace("talk about", "")
            speak_properly(f"Presenting about {Hello}")
            present = powerpoint(Hello)
            with open('powerpoint.txt', 'w') as file:
                file.write(present)
            os.startfile("C:\\Users\\surface\\Desktop\\Nimi's Ai\\powerpoint.txt")
            speak_properly("done that sir, here is your generated Presentation")
        elif "open settings" in command:
            speak_properly("Opening Settings sir.")
            self.open_settings()
        elif "tell a joke" in command:
            joke = self.get_random_joke()
            speak_properly("Here's a joke for you: " + joke)
        elif "start a game" in command:
            speak_properly("Sure, let's play a game")
            self.game_play()
        elif "question" in command:
            speak_properly("Sure, go ahead and ask your question.")
            Class = self.listen_for_command()
            speak_properly("According to my Intelligence")
            response = create_ppt_text(Class)
            speak_properly(response)
            
        elif "google" in command or "kevin search" in command:
            import wikipedia as googleScrap
            query = command.replace("kevin search","")
            query = command.replace("google search","")
            query = command.replace("google","")
            speak_properly("This is what I found on google")
            try:
                pywhatkit.search(query)
                result = googleScrap.summary(query,1)
                speak_properly(result)

            except:
                speak_properly("No speakable output available")

        elif "who is" in command:
            person = command.split("who is", 1)[1].strip()
            speak_properly("According to my Intelligence")
            response = create_ppt_text(person)
            speak_properly("Here's what I found about " + person + ": " + response)
        elif "define" in command:
                word_to_define = command.split("define", 1)[1].strip()
                speak_properly("According to my Intelligence")
                response = create_ppt_text(word_to_define)
                speak_properly(response)
        elif "are you" in command:
            query = command.split("are you", 1)[1].strip()
            response = create_ppt_text(query)
            speak_properly(response)
        elif "what are" in command:
            query = command.split("what are", 1)[1].strip()
            speak_properly("According to my Intelligence")
            response = create_ppt_text(query)
            speak_properly(response)
        elif "why are" in command:
            query = command.split("why are", 1)[1].strip()
            speak_properly("According to my Intelligence")
            response = create_ppt_text(query)
            speak_properly(response)
        elif "what's my status" in command:
            speak_properly("Your just the man with the plan and i'm very grateful to have you!")
        elif "what is" in command:
            query = command.split("what is", 1)[1].strip()
            speak_properly("According to my Intelligence")
            response = create_ppt_text(query)
            speak_properly(response)
        elif "shutdown" in command:
            speak_properly("Shutting down your computer.")
            os.system("shutdown /s /t 0")  # Shuts down the computer immediately

    # Function to play music on YouTube
    def play_music_on_youtube(query, self):
        try:
            # Construct the YouTube search URL
            search_url = f"https://www.youtube.com/results?search_query={query}"
            webbrowser.open(search_url)
            speak_properly(f"Playing music on youTube for {query}.")
        except Exception as e:
            print("Error playing music on youTube:", e)
            speak_properly("I encountered an error while playing music on youTube. Please try again later.")
    # ...

def powerpoint(Hello):
    response = g4f.ChatCompletion.create(
        model="gpt-4-32k-0613",
        provider=g4f.Provider.GPTalk,
        messages=[
            {"role": "system", "content": (Prompt)},
            {"role": "user", "content": ("The user wants a presentation about " + Hello)}
        ],
        stream=True,
    )
    
    ms=""
    for message in response:
        ms+=str(message)
        print(message,end="",flush=True)
    print()

    return ms

def get_google_maps_directions_link(origin, destination, mode="driving"):
        base_url = "https://www.google.com/maps/dir/?api=1"
        
        # Encode the addresses for the URL
        origin = origin.replace(" ", "+")
        destination = destination.replace(" ", "+")
        
        # Construct the Google Maps URL with the specified parameters
        maps_url = f"{base_url}&origin={origin}&destination={destination}&travelmode={mode}"
        
        return maps_url

    # Function to get system information
def get_system_info():
    cpu_percent = psutil.cpu_percent(interval=1)
    memory_info = psutil.virtual_memory()
    disk_info = psutil.disk_usage('/')
    try:
        # Get battery information (if available)
        battery_info = psutil.sensors_battery()
        percent_battery = battery_info.percent
        battery_status = battery_info.power_plugged
    except AttributeError:
        # psutil.sensors_battery() may raise AttributeError on systems without battery info
        percent_battery = None
        battery_status = None
    system_info = f"CPU Usage: {cpu_percent}%\n"
    system_info += f"Memory Usage: {memory_info.percent}%\n"
    system_info += f"Total Disk Space: {disk_info.total / (1024 ** 3):.2f} GB\n"
    system_info += f"Used Disk Space: {disk_info.used / (1024 ** 3):.2f} GB\n"
    system_info += f"Free Disk Space: {disk_info.free / (1024 ** 3):.2f} GB"
    if percent_battery is not None:
        system_info += f"Battery: {percent_battery}% {'Plugged In' if battery_status else 'Not Plugged In'}\n"

    return system_info

def chat_with_gpt3(prompt):
    response = g4f.ChatCompletion.create(
        model="gpt-4-32k-0613",
        provider=g4f.Provider.GPTalk,
        messages=[
            {"role": "system", "content": (prompt)},
        ],
        stream=True,
    )
    
    ms = ""
    for message in response:
        ms += str(message)
        print(message, end="", flush=True)
    print()

    return ms


    class VitalsMonitor:
        def __init__(self):
            self.blood_toxicity = 0
            self.heart_rate = 0
            self.blood_pressure = "120/80"

        def update_vitals(self):
            # Simulate random changes in vitals for demonstration purposes
            self.blood_toxicity = random.uniform(0, 1)  # Simulate blood toxicity between 0 and 1
            self.heart_rate = random.randint(60, 100)  # Simulate heart rate between 60 and 100
            self.blood_pressure = f"{random.randint(90, 140)}/{random.randint(60, 90)}"  # Simulate blood pressure

        def get_vitals(self):
            return {
                "blood_toxicity": self.blood_toxicity,
                "heart_rate": self.heart_rate,
                "blood_pressure": self.blood_pressure
            }

    # Create a VitalsMonitor instance
    vitals_monitor = VitalsMonitor()

    # Function to monitor vitals
    def monitor_vitals():
        vitals_monitor.update_vitals()
        vitals = vitals_monitor.get_vitals()
        return vitals

def create_ppt_text(prompt):
    response = g4f.ChatCompletion.create(
        model="gpt-4-32k-0613",
        provider=g4f.Provider.GPTalk,
        messages=[
            {"role": "system", "content": (prompt)},
        ],
        stream=True,
    )
    
    ms = ""
    for message in response:
        ms += str(message)
        print(message, end="", flush=True)
    print()

    return ms

def generate_code(prompt):
    response = openai.Completion.create(
        engine="text-davinci-003",  # Choose the engine according to your needs
        prompt=prompt,
        max_tokens=200,  # Adjust as needed
        temperature=0.7,  # Adjust for randomness (0.0 for deterministic, higher for more randomness)
        n=1,  # Number of completions to generate
        stop=None  # You can specify a stopping condition if needed
    )

    return response.choices[0].text.strip()

def speak_properly(text):
        voice = engine.getProperty('voices')[0]  
        engine.setProperty('voice', voice.id)
        engine.setProperty('rate', 150)
        # Get the current status of the TTS engine
        engine_status = engine._inLoop
        try:
            # If the engine is not already running, start it
            if not engine_status:
                engine.say(text)
                engine.runAndWait()
            else:
                # If the engine is already running, queue the speech
                engine.say(text)
        except Exception as e:
            print(f"Error in speak_properly: {e}")
        finally:
            # Stop the engine if it wasn't running before
            if not engine_status:
                engine.stop()


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(898, 629)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../Kevin - Copy.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Dialog.setWindowIcon(icon)
        Dialog.setStyleSheet("background-color: rgb(0, 0, 0);\n"
"border : 1px solid white;\n"
"")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(470, 260, 431, 221))
        self.label_4.setText("")
        self.label_4.setPixmap(QtGui.QPixmap("../../Downloads/Hero_Template.gif"))
        self.label_4.setScaledContents(True)
        self.label_4.setObjectName("label_4")
        self.label_6 = QtWidgets.QLabel(Dialog)
        self.label_6.setGeometry(QtCore.QRect(0, 260, 471, 221))
        self.label_6.setText("")
        self.label_6.setPixmap(QtGui.QPixmap("../../Downloads/Earth.gif"))
        self.label_6.setScaledContents(True)
        self.label_6.setObjectName("label_6")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(290, 0, 361, 261))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("../../Downloads/Ntuks.gif"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

        self.movie4 = QtGui.QMovie("../../Downloads/Hero_Template.gif")
        self.movie6 = QtGui.QMovie("../../Downloads/Earth.gif")
        self.movie=QtGui.QMovie("../../Downloads/Ntuks.gif")

        # Set QMovies for your labels
        self.label_4.setMovie(self.movie4)
        self.label_6.setMovie(self.movie6)
        self.label.setMovie(self.movie)

        # Start QMovies
        self.movie4.start()
        self.movie6.start()
        self.movie.start()

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "KEVIN-SECURITY SYSTEM"))

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ai_thread = MainThread()
    ai_thread.start()
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    app_icon = QtGui.QIcon("C:\\Users\\surface\\Downloads\\7gQj (1).gif")
    app.setWindowIcon(app_icon)
    Dialog.show()
    sys.exit(app.exec_())