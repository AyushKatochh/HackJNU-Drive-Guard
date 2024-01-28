import time
import face_recognition

from db import mycol

def verify(frame):
    try:
        encoding = face_recognition.face_encodings(frame)
        if(len(encoding)>1):
            print("More than one face detected")
    except Exception as e:
        print(e)

    document =  {
        'time':time.time(),
        'encoding':encoding[0].tolist()
    }
    mycol.insert_one(document)
