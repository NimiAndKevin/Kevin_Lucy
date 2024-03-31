import random
import subprocess
import cv2
import numpy as np
from ultralytics import YOLO
from clarifai import ClarifaiApp

# opening the file in read mode
my_file = open("C:\\Users\\surface\\Desktop\\Nimi's Ai\\yolov8-silva\\coco.txt")
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

# Set up Clarifai API client
clarifai_api_key = "2f167cf2396d467d84600769d2986716"  # Replace with your Clarifai API key
app = RESTClient(api_key=clarifai_api_key)
model = app.public_models.general_model

# Vals to resize video frames | small frame optimise the run
frame_wid = 640
frame_hyt = 480

cap = cv2.VideoCapture(0)

while True:
    # Capture frame-by-frame
    ret, frame = cap.read()
    # if frame is read correctly ret is True

    if not ret:
        print("Can't receive frame (stream end?). Exiting ...")
        break

    # Predict on image
    detect_params = model.predict(source=[frame], conf=0.45, save=False)

    # Convert tensor array to numpy
    DP = detect_params[0].numpy()

    if len(DP) != 0:
        for i in range(len(detect_params[0])):
            boxes = detect_params[0].boxes
            box = boxes[i]  # returns one box
            clsID = box.cls.numpy()[0]
            conf = box.conf.numpy()[0]
            bb = box.xyxy.numpy()[0]

            cv2.rectangle(
                frame,
                (int(bb[0]), int(bb[1])),
                (int(bb[2]), int(bb[3])),
                detection_colors[int(clsID)],
                3,
            )

            # Display class name and confidence
            font = cv2.FONT_HERSHEY_COMPLEX
            cv2.putText(
                frame,
                class_list[int(clsID)] + " " + str(round(conf, 3)) + "%",
                (int(bb[0]), int(bb[1]) - 10),
                font,
                1,
                (255, 255, 255),
                2,
            )

            # Use Clarifai API to get information about the object
            response = model.predict_by_filename(frame)  # Assuming Clarifai supports image file input
            concepts = response['outputs'][0]['data']['concepts']
            
            # Extract relevant information
            object_info = ', '.join([concept['name'] for concept in concepts])
            print(f"Detected object: {class_list[int(clsID)]}, Clarifai info: {object_info}")

            # Say information about the object
            subprocess.run(['python', "C:\\Users\\surface\\Desktop\\gui.py"])
            
    # Display the resulting frame
    cv2.imshow("ObjectDetection", frame)

    # Terminate run when "Q" pressed
    if cv2.waitKey(1) == ord("q"):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()