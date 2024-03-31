import sys
from PyQt5.QtWidgets import QApplication, QDialog, QVBoxLayout, QLabel
from PyQt5.QtCore import QThread, pyqtSignal
import sounddevice as sd
import numpy as np
import openai
import speech_recognition as sr
import pyttsx3
import requests
import json
from bs4 import BeautifulSoup
import time as time
from datetime import datetime
from PyQt5 import QtCore, QtGui, QtWidgets  # Added import for PyQt5
import webbrowser
#pip install selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
import colorama
from colorama import Fore, Back, Style
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from os import getcwd
import colorama
from colorama import Fore, Back, Style
import g4f

class MainThread(QThread):
    finished_signal = pyqtSignal()

    def __init__(self, parent=None):
        super(MainThread, self).__init__(parent)
        self.total_sleep_duration_days = 365

    def run(self):
        self.TaskExecution()
        self.finished_signal.emit()

    def TaskExecution(self):
        text_to_speech("Please Snap to Use Me")
        self.lucy_sleep()
        text_to_speech("Hello Captain, I'm Lucy, your Female ChatGPT Voice Assistant! Ask me any question, and I will answer it")

        while True:
            user_input = self.listen_for_voice()
            self.process_user_input(user_input)

    def listen_for_voice(self):
        colorama.init(autoreset=True)
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument("--use-fake-ui-for-media-stream")
        chrome_options.add_argument("--headless=new")
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()),options=chrome_options)
        website = f"file:///C:/Users/surface/Desktop/Destop/Nimi's%20Ai/Kevin-and-Lucy/voice.html"
        driver.get(website)
        print(Fore.MAGENTA + "LISTENING ... ")
        print()
        driver.get(website)
        driver.find_element(by=By.ID, value='start').click()
        while 1:
            text=driver.find_element(by=By.ID, value='output').text
            if text != "":
                print(Fore.YELLOW+"YOU SAID : " + text.lower())
                print()

                driver.find_element(by=By.ID, value='end').click()
                return text.lower()

    def process_user_input(self, user_input):
        if "sleep" in user_input:
            text_to_speech("Please Snap to Use Me")
            self.lucy_sleep()
            text_to_speech("Hello Captain, I'm Lucy, your Female ChatGPT Voice Assistant! Ask me any question, and I will answer it")
        elif "the weather" in user_input:
            text_to_speech("where")
            city = self.listen_for_voice() # Prompt the user to enter the city
            url = f"https://www.google.com/search?q=weather+in+{city}"
            r = requests.get(url)
            data = BeautifulSoup(r.text,"html.parser")
            region = data.find("div", class_="BNeawe iBp4i AP7Wnd").text
            day_and_time = data.find("div", class_="BNeawe tAd8D AP7Wnd").text
            temperature = data.find("div", class_="BNeawe tAd8D AP7Wnd").text
            temp = data.find("div", class_ = "BNeawe").text
            weather_condition = day_and_time.split("\n")[-1]
            weather_info = f"{weather_condition}"
            text_to_speech(f"The weather outside in {city} is {temp}, it will be {weather_info} day outside")
        elif "location" in user_input or "where am i" in user_input:
            My_Location()
        elif "the time in" in user_input:
            try:
                # Get the time zone for the specified location
                timezone = pytz.timezone(location)

                # Get the current time and convert it to the specified time zone
                current_time = datetime.datetime.now()
                time_in_location = current_time.astimezone(timezone)

                return time_in_location.strftime("%Y-%m-%d %H:%M:%S")
            except Exception as e:
                return f"Error: {str(e)}"
            location = user_input.replace("the time in", "")  # Replace with the desired time zone (city, state, or country)
            current_time = get_current_time(location)
            text_to_speech(f"The current time in {location} is: {current_time}")
        elif "lucy" in user_input:
            query=user_input.replace("lucy", "")
            response = self.chat_with_gpt3(query)
            text_to_speech(response)
        elif "go back to kevin" in user_input or "call kevin" in user_input:
            text_to_speech("calling my friend kevin")
            subprocess.run(["python", "C:\\Users\\surface\\Desktop\\Nimi's Ai\\gui.py"])
        elif "i am going somewhere" in user_input or "where is" in user_input or "i want to my destination" in user_input or "i want to reach my destination" in user_input or "where is my destination" in user_input or "destination mode" in user_input:
            destination_location = user_input.replace("where is", "")
            text_to_speech("hold on captain what is your location")
            origin_location = self.listen_for_voice()
            google_maps_link = get_google_maps_directions_link(origin_location, destination_location)
            text_to_speech("checking")
            webbrowser.open(google_maps_link)
            text_to_speech("here is your destination, i wish you safe travels")
        elif "i need help" in user_input or "i need your help" in user_input:
            text_to_speech("sir what do you need help with")
            query = self.listen_for_voice()
            text_to_speech("Certainly captain let me look into it an see what is going on")
            response=self.chat_with_gpt3(query)
            text_to_speech(response)
        elif "don't listen" in user_input or "stop listening" in user_input or "take a break" in user_input:
            text_to_speech("For how many hours do you want me to stop listening to commands?")
            hours = int(input("how many hours Sir: "))
            if hours > 0:
                sleep_duration = hours * 3600 
                text_to_speech(f"I will sleep for {hours} hours. Let me know when you want me to wake up.")
                time.sleep(sleep_duration)
                while True:
                    user_input = self.listen_for_voice()
                    self.process_user_input(user_input)

    def lucy_sleep(self):
        total_sleep_duration_seconds = self.total_sleep_duration_days * 24 * 60 * 60
        print(f"Lucy is sleeping...")

        # Set the duration for each sleep check
        sleep_check_duration = 5  # in seconds (adjust as needed)
        sampling_rate = 44100

        start_time = time.time()
        current_time = start_time

        while current_time - start_time < total_sleep_duration_seconds:
            # Record audio to detect a snap
            recording_duration = int(sleep_check_duration * sampling_rate)
            recording = sd.rec(recording_duration, samplerate=sampling_rate, channels=2, dtype=np.int16)
            sd.wait()

            # Check for a snap sound (sudden change in amplitude)
            snap_threshold = 3000  # Adjust this threshold based on your environment
            amplitude_changes = np.diff(np.abs(recording[:, 0]))  # Use the left channel for simplicity
            snap_detected = any(amplitude_changes > snap_threshold)

            if snap_detected:
                print("Snap detected")
                text_to_speech("Lucy heard a snap! Waking up...")
                current_time = datetime.now().strftime("%I:%M %p")
                text_to_speech("Welcome back, Captain")
                text_to_speech(f"The current time is {current_time}")
                break

            print(f"Lucy didn't hear a clap. Still sleeping. Time elapsed: {current_time - start_time} seconds")

            # Sleep for the check duration
            time.sleep(sleep_check_duration)
    def chat_with_gpt3(self,prompt):
        response = g4f.ChatCompletion.create(
            model="gpt-4-32k-0613",
            provider=g4f.Provider.Bing,
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
def text_to_speech(text):
    tts_engine = pyttsx3.init()
    voice = tts_engine.getProperty('voices')[2]
    tts_engine.setProperty('voice', voice.id)
    tts_engine.setProperty('rate', 150)
    tts_engine.say(text)
    tts_engine.runAndWait()

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.setStyleSheet("background-color: rgb(0, 0, 0);\n"
                            "")
        
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(240, 80, 421, 421))
        self.label.setText("")
        
        # Create a QMovie and set it to the QLabel for animation
        self.movie = QtGui.QMovie("C:\\Users\\surface\\Downloads\\fxVE.gif")
        self.label.setMovie(self.movie)
        self.movie.start()  
        
        self.label.setScaledContents(True)
        self.label.setObjectName("label")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "LUCY"))

def My_Location():
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
    text_to_speech(f"Sir you are now in {state, country, city} it has the latitude of {latitude} and the longtitude of {longitude} the time zone in here is {timezone} wlecome to {country}")
def get_google_maps_directions_link(origin, destination, mode="driving"):
    base_url = "https://www.google.com/maps/dir/?api=1"
    
    # Encode the addresses for the URL
    origin = origin.replace(" ", "+")
    destination = destination.replace(" ", "+")
    
    # Construct the Google Maps URL with the specified parameters
    maps_url = f"{base_url}&origin={origin}&destination={destination}&travelmode={mode}"
    
    return maps_url

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ai_thread = MainThread()
    ai_thread.start()
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    app_icon = QtGui.QIcon("C:\\Users\\surface\\Desktop\\Destop\\icon-5887113_1280.webp")
    app.setWindowIcon(app_icon)
    Dialog.show()
    sys.exit(app.exec_())