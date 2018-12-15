import cv2
import numpy as np

file = open('data.txt')
poly = file.readlines()
poly.remove("\n")

car_cascade = cv2.CascadeClassifier('cars.xml')
cap = cv2.VideoCapture('test.mp4')
font = cv2.FONT_HERSHEY_COMPLEX_SMALL

while True:
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    cars = car_cascade.detectMultiScale(gray,1.2,5)

    for i in range(0,15):
        res = [int(s) for s in poly[i].split() if s.isdigit()]
        res.pop(0)
        print("log res: ", res)
        res = np.array(res)
        pts = np.array([[res[0],res[1]],[res[2],res[3]],[res[4],res[5]],[res[6],res[7]]])
        pts = pts.reshape((-1,1,2))
        print("log pts: ",pts)
        font = cv2.FONT_HERSHEY_SIMPLEX
        cv2.putText(frame,str(i),(pts[0][0][0],pts[0][0][1]), font, 1,(0,0,0),2,cv2.LINE_AA)
        x=pts[2][0][0]
        y=pts[2][0][1]
        print("x: ",x)
        print("y: ",y)

        w = pts[3][0][0]  - x
        h = pts[1][0][1] - y
        roi = frame[y:y+h, x:x+w]
        gray_roi = cv2.cvtColor(roi,cv2.COLOR_BGR2GRAY)
        avg_color_per_row = np.average(gray_roi, axis=0)
        avg_color = np.average(avg_color_per_row, axis=0)
        cv2.polylines(frame,[pts],True,(0,255,0))
        cv2.polylines(frame,[pts],True,(0,0,255))



    for (x,y,w,h) in cars:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,255),5)


    cv2.imshow("car_detection",frame)
    k = cv2.waitKey(1)
    if k == ord('q'):
        break