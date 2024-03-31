import random
import subprocess
import numpy as np
from ultralytics import YOLO
import pyautogui
import pyttsx3
import cv2

engine = pyttsx3.init()

def speak_properly(text):
    voice = engine.getProperty('voices')[0]  
    engine.setProperty('voice', voice.id)
    engine.setProperty('rate', 150)
    engine.say(text)
    engine.runAndWait()

# opening the file in read mode
my_file = open("C:\\Users\\surface\\Desktop\\yolov8-silva\\coco.txt")
# reading the file
data = my_file.read()
# replacing end splitting the text | when newline ('\n') is seen.
class_list = data.split("\n")
my_file.close()

# print(class_list)

# Generate random colors for class list
detection_colors = []
for i in range(len(class_list)):
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    detection_colors.append((b, g, r))

# load a pretrained YOLOv8n model
model = YOLO("weights/yolov8n.pt", "v8")

# Take a screenshot using PyAutoGUI
screenshot = pyautogui.screenshot()
screenshot = np.array(screenshot)
screenshot = cv2.cvtColor(screenshot, cv2.COLOR_RGB2BGR)

# Predict on the screenshot
detect_params = model.predict(source=[screenshot], conf=0.45, save=False)

# Convert tensor array to numpy
DP = detect_params[0].numpy()

# Dictionary to store counts for each class
class_counts = {class_name: 0 for class_name in class_list}

if len(DP) != 0:
    for i in range(len(detect_params[0])):
        boxes = detect_params[0].boxes
        box = boxes[i]  # returns one box
        clsID = box.cls.numpy()[0]
        conf = box.conf.numpy()[0]
        bb = box.xyxy.numpy()[0]

        # Increment the count for the detected class
        class_counts[class_list[int(clsID)]] += 1

        speak_properly(f"I can see {class_counts[class_list[int(clsID)]]} {class_list[int(clsID)]}s")

    subprocess.run(['python', "C:\\Users\\surface\\Desktop\\gui.py"])