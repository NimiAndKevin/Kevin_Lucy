import cv2
import subprocess


def count_people_in_environment():
        # Open the video capture
        cap = cv2.VideoCapture(0)  # Use 0 for default camera

        # Initialize background subtractor
        bg_subtractor = cv2.createBackgroundSubtractorMOG2()

        while True:
                # Read a frame from the video feed
                ret, frame = cap.read()

                # Apply background subtraction
                fg_mask = bg_subtractor.apply(frame)

                # Apply some morphological operations to clean up the mask
                fg_mask = cv2.erode(fg_mask, None, iterations=2)
                fg_mask = cv2.dilate(fg_mask, None, iterations=2)

                # Find contours in the mask
                contours, _ = cv2.findContours(fg_mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

                # Count the number of contours (people)
                people_count = len(contours)

                # Display the result on the frame
                result_text = f'People Count:{people_count}'
                cv2.putText(frame, result_text, (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

                cv2.imshow("Counting Detection", frame)
            # Break the loop if 'q' key is pressed
                if cv2.waitKey(1) & 0xFF == ord('q'):
                        break

        # Release the video capture object
        cap.release()

        # Close all windows
        cv2.destroyAllWindows()
        # Run another script after the detection loop
        subprocess.run(['python', "C:\\Users\\surface\\Desktop\\gui.py"])


if __name__ == "__main__":
    count_people_in_environment()