import cv2
import mediapipe as mp
import pyautogui

# Initialize Mediapipe Hands
mp_hands = mp.solutions.hands
hands = mp_hands.Hands()

# Set up video capture
cap = cv2.VideoCapture(0)
cap.set(3, 640)
cap.set(4, 480)

# Scroll speed factor
scroll_speed_factor = 90

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    # Flip the frame horizontally for a later selfie-view display
    frame = cv2.flip(frame, 1)

    # Convert the BGR image to RGB
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Process the frame with Mediapipe Hands
    results = hands.process(rgb_frame)

    # Check if hand landmarks are detected
    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            # Extract the x and y coordinates of the index finger
            index_finger = hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP]
            index_x = int(index_finger.x * frame.shape[1])
            index_y = int(index_finger.y * frame.shape[0])

            # Scroll up, down, or horizontally based on index finger position and adjust speed
            if index_y < frame.shape[0] // 3:
                pyautogui.scroll(scroll_speed_factor)
            elif index_y > 2 * frame.shape[0] // 3:
                pyautogui.scroll(-scroll_speed_factor)
            elif index_x < frame.shape[1] // 3:
                pyautogui.hscroll(scroll_speed_factor)
            elif index_x > 2 * frame.shape[1] // 3:
                pyautogui.hscroll(-scroll_speed_factor)

            # Draw a circle at the index finger position
            cv2.circle(frame, (index_x, index_y), 10, (0, 255, 0), -1)

    # Display the frame
    cv2.imshow('Hand Scroll', frame)

    # Break the loop when 'Esc' key is pressed
    if cv2.waitKey(1) == 27:
        break
