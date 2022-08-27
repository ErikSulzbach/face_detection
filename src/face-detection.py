import cv2

capture = cv2.VideoCapture(0)
cascade = cv2.CascadeClassifier("data/haarcascade_frontalface_default.xml")

while True:
    _, img = capture.read()
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = cascade.detectMultiScale(img_gray) #[(0,0,500,500), (200,300,650,650), ...]
    
    for x, y, width, height in faces:
        cv2.rectangle(img, (x, y), (x + width, y + height), color=(0, 0, 255), thickness=2)
    cv2.imshow("Kamera", img)
    
    if cv2.waitKey(1) == ord("q"):
        break


capture.release()
cv2.destroyAllWindows