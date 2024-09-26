import cv2
from deepface import DeepFace

face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")

video = cv2.VideoCapture(0, cv2.CAP_DSHOW)

if not video.isOpened():
    raise IOError("Cannot open webcam")

while video.isOpened():
    _, frame = video.read()

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)

    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (89, 2, 236), 1)

        # Crop the face region
        face_region = frame[y:y + h, x:x + w]

        try:
            analyze = DeepFace.analyze(face_region, actions=['emotion'], enforce_detection=False)
            cv2.putText(frame, analyze[0]['dominant_emotion'], (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 1, (224, 77, 176), 2)
            print(analyze[0]['dominant_emotion'])
        except Exception as e:
            print('no face:', e)

    cv2.imshow('video', frame)
    key = cv2.waitKey(1)
    if key == ord('q'):
        break

video.release()
cv2.destroyAllWindows()
