import cv2 as cv
import mediapipe as mp
import time
import pose_estimation_module as pem
import numpy as np

cap = cv.VideoCapture(0)

if not cap.isOpened():
    print("Error: Could not open video file")
    exit()

detector = pem.PoseDetector()
pTime =0
count = -0.5
dir = 1 # 0 - up, 1 - down

while True:
    success, img = cap.read()
    img = detector.findPose(img, draw=False)

    cTime = time.time()
    fps = 1/(cTime-pTime)
    pTime = cTime
    cv.putText(img, str(int(fps)), (70,50), cv.FONT_HERSHEY_PLAIN, 3, (255,0,0), 3)
    lmList = detector.findPosition(img, draw=False)
    
    if len(lmList) != 0:
        knee = detector.findAngle(img, 12, 24, 26)
        back = detector.findAngle(img, 24, 26, 28)
        elbow = detector.findAngle(img, 12, 14, 16)

        k = 0
        b = 0
        
        if knee > 170 and knee < 190:
            k = 1
        if back > 170 and back < 190:
            b = 1
        if k == 1 and b == 1:
            cv.putText(img, "Good Posture", (70, 150), cv.FONT_HERSHEY_PLAIN, 5, (0, 255, 0), 3)
        else:
            cv.putText(img, "Bad Posture", (70, 150), cv.FONT_HERSHEY_PLAIN, 5, (0, 0, 255), 3)

        per = np.interp(elbow, (75, 160), (0, 100))
        print(elbow, per)

        #Check elbow curl
        if per == 100:
            if dir == 1:
                count += 0.5
                dir = 0
        if per == 0:
            if dir == 0:
                count += 0.5
                dir = 1
        cv.putText(img, f'Count: {int(count)}', (70, 300), cv.FONT_HERSHEY_PLAIN, 10, (255, 0, 0), 3)
    
    print(count)
    cv.imshow("Push Up", img)
    cv.waitKey(1)
