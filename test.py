import cv2
import numpy as np

# Load the pre-trained face detection model
face_cascade = cv2.CascadeClassifier("C:\\Users\\surface\\Desktop\\Nimi's Ai\\Kevin-and-Lucy\haarcascade_frontalface_default.xml")

# Load the pre-trained face recognition model
recognizer = cv2.face.LBPHFaceRecognizer_create()

# Load the training data
recognizer.read("C:\\Users\\surface\\Desktop\\Nimi's Ai\\trained_data.yml")

# Initialize the video capture
cap = cv2.VideoCapture(0)

# Flag to track if the message has been printed
hello_printed = False

while True:
    # Read the current frame
    ret, frame = cap.read()
    
    # Convert the frame to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    # Detect faces in the frame
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))
    
    for (x, y, w, h) in faces:
        # Draw a rectangle around the face
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
        
        # Extract the face region of interest
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = frame[y:y+h, x:x+w]
        
        # Perform face recognition
        label, confidence = recognizer.predict(roi_gray)

        # Display the name of the recognized person
        if confidence < 100:
            name = "Nimi " + str(label)
            
            # Print "hello sir" if not already printed
            if not hello_printed:
                print("hello sir")
                hello_printed = True
                
                # Break out of the loop if "hello sir" is printed
                break
        else:
            name = "Unknown"

    # Display the resulting frame
    cv2.imshow('Face Recognition', frame)
    
    # Break the loop if 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    
    # Break out of the loop if "hello sir" is printed
    if hello_printed:
        break
    
    

# Release the video capture and close all windows
cap.release()
cv2.destroyAllWindows()
