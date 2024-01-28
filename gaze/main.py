import cv2
import time

from gaze_tracking import GazeTracking
from utils import verify

new_frame_time = 0
prev_frame_time = 0
curr_frame = 0
counter = 0

IMG_SIZE = (640, 480)

gaze:GazeTracking = GazeTracking()
cap = cv2.VideoCapture('E:/code/projects/hackathon_project/input/vdo_eyes.mp4')
# result = cv2.VideoWriter('output.avi',
#                         cv2.VideoWriter_fourcc(*'MJPG'), 
#                          8, (640,480))

while True:
    if counter==1:
        verify(frame)

    ret, frame = cap.read()
    if not ret:
        print('---------------------------------Stream Ended---------------------------------')
        break
    
    frame = cv2.resize(frame, IMG_SIZE)
    gaze.refresh(frame)
    text:str = ""

    new_frame_time = time.time()
    fps = 1/(new_frame_time-prev_frame_time) 
    prev_frame_time = new_frame_time
    fps = str(int(fps))
    cv2.putText(frame, f'FPS: {fps}', (10, 20), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)


    if gaze.is_blinking():
        counter+=1
        if(counter<=7):
            text = "Blinking"
        else: text = "Drowsy"

    elif gaze.is_right() or gaze.is_left() or gaze.is_center():
        text = "Attentive"
        counter=0
    else: text = "Not Attentive"
    curr_frame+=1
    if(curr_frame%13500==0):
        verify(frame)
    
        
    cv2.putText(frame, text, (2, 50), cv2.FONT_HERSHEY_DUPLEX, 0.8, (147, 58, 31), 2)

    cv2.imshow("Demo", frame)
    # result.write(frame)

    if cv2.waitKey(1) == 27:
        break
   
cap.release()
# result.release()
cv2.destroyAllWindows()