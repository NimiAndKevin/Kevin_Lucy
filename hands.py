import cv2
import mediapipe as mp
import pyautogui
import subprocess



def virtual():
        cap = cv2.VideoCapture(0)
        hand_detector = mp.solutions.hands.Hands()
        drawing_utils = mp.solutions.drawing_utils

        # Set the desired frame width and height
        frame_width = 640
        frame_height = 480

        # Set the frame width and height for the capture
        cap.set(3, frame_width)
        cap.set(4, frame_height)

        screen_width, screen_height = pyautogui.size()
        index_y = 0

        while True:
            _, frame = cap.read()
            frame = cv2.flip(frame, 1)

            rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            output = hand_detector.process(rgb_frame)
            hands = output.multi_hand_landmarks

            if hands:
                for hand in hands:
                    drawing_utils.draw_landmarks(frame, hand)
                    landmarks = hand.landmark
                    for id, landmark in enumerate(landmarks):
                        x = int(landmark.x * frame_width)
                        y = int(landmark.y * frame_height)
                        if id == 8:
                            cv2.circle(img=frame, center=(x, y), radius=10, color=(0, 255, 255))
                            index_x = screen_width / frame_width * x
                            index_y = screen_height / frame_height * y

                        if id == 4:
                            cv2.circle(img=frame, center=(x, y), radius=10, color=(0, 255, 255))
                            thumb_x = screen_width / frame_width * x
                            thumb_y = screen_height / frame_height * y
                            if abs(index_y - thumb_y) < 20:
                                pyautogui.click()
                                pyautogui.sleep(1)
                            elif abs(index_y - thumb_y) < 100:
                                pyautogui.moveTo(index_x, index_y)

            # Resize the frame for display
            enlarged_frame = cv2.resize(frame, (2 * frame_width, 2 * frame_height))
            cv2.imshow("Kevin's Virtual Mouse", enlarged_frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):    
                break

        cap.release()
        cv2.destroyAllWindows()
        # Run another script after the detection loop
        subprocess.run(['python', "C:\\Users\\surface\\Desktop\\gui.py"])

if __name__ == "__main__":
    virtual()