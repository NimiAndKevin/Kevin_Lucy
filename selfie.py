import cv2
import datetime
import os
import subprocess

def selfie():
    cap = cv2.VideoCapture(0)
    face_cascade = cv2.CascadeClassifier("C:\\Users\\surface\\Desktop\\Nimi's Ai\\Kevin-and-Lucy\\haarcascade_frontalface_default.xml")
    smile_cascade = cv2.CascadeClassifier("C:\\Users\\surface\\Desktop\\Nimi's Ai\\Kevin-and-Lucy\\haarcascade_smile.xml")

    selfie_taken = False  # Flag to track if a selfie has been taken

    while True:
        _, frame = cap.read()
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        face = face_cascade.detectMultiScale(gray, 1.3, 5)
        
        for x, y, w, h in face:
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 255), 2)
            face_roi = frame[y:y+h, x:x+w]
            gray_roi = gray[y:y+h, x:x+w]
            smile = smile_cascade.detectMultiScale(gray_roi, 1.3, 25)
            
            for x1, y1, w1, h1 in smile:
                cv2.rectangle(face_roi, (x1, y1), (x1+w1, y1+h1), (0, 0, 255), 2)
                
                if not selfie_taken:
                    # Take a selfie only if it hasn't been taken before
                    cv2.imwrite(f'C:\\Users\\surface\\Desktop\\selfie.png', frame)
                    os.startfile(f'C:\\Users\\surface\\Desktop\\selfie.png')
                    selfie_taken = True  # Set the flag to True after taking the selfie

        cv2.imshow('cam star', frame)

        if cv2.waitKey(10) == ord('j') or selfie_taken:
            break  # Exit the loop if 'j' is pressed or a selfie has been taken

    # Release the video capture object
    cap.release()

    # Close all windows
    cv2.destroyAllWindows()

    subprocess.run(['python', "C:\\Users\\surface\\Desktop\\gui.py"])

if __name__ == "__main__":
    selfie()

