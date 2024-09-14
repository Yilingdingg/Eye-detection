import cv2

eye_xml="haarcascade_eye.xml"

eye_detection=cv2.CascadeClassifier(eye_xml)

path="datasets/Elise"
#open camera
webcam=cv2.VideoCapture(0)
count=1
while count<40:
    ret, img=webcam.read()
    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    eye=eye_detection.detectMultiScale(gray, 1.5, 1)
    print(eye)
    for (x,y,w,h) in eye:
        cv2.rectangle(img, (x,y),(x+w,y+h),(186,198,240),3)
        eye=gray[y:y+h,x:x+h]
        eye_resize=cv2.resize(eye,(110,90))
    count+=1

    
    cv2.imshow("Webcam", img)
    key=cv2.waitKey(10)
    if key==27:
        break