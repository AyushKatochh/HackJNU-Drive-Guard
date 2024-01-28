import face_recognition

from gaze.db import mycol

import cv2

def capture_media(decision):

    actions = {
        "image": capture_image,
        "video": capture_video,
    }

    if decision not in actions:
        raise ValueError(f"Invalid decision: {decision}")

    return actions[decision]()

def capture_image():

    cap = cv2.VideoCapture(0)  # Open default camera
    ret, frame = cap.read()
    cap.release()

    if ret:
        cv2.imwrite("captured_image.jpg", frame)
        print("Image captured successfully!")
    else:
        print("Error capturing image.")

def capture_video():

    cap = cv2.VideoCapture(0)

    fourcc = cv2.VideoWriter_fourcc(*'XVID')  # Define codec
    out = cv2.VideoWriter('captured_video.avi', fourcc, 20.0, (640, 480))  # Set output video

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        out.write(frame)
        cv2.imshow('Video Capture', frame)

        if cv2.waitKey(1) == ord('q'):  # Press 'q' to quit
            break

    cap.release()
    out.release()
    cv2.destroyAllWindows()
    print("Video captured successfully!")

# Example usage:
decision = input("Enter 'image' or 'video': ")
capture_media(decision)
