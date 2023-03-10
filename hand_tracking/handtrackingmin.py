import cv2
import mediapipe as mp
import time
cap=cv2.VideoCapture(0)

mphands=mp.solutions.hands
hands=mphands.Hands()
mpdraw=mp.solutions.drawing_utils

pTime=0
cTime=0

print("hello")
while True:

    sucess,img=cap.read()

    imgRGB=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
    results=hands.process(imgRGB)
    if results.multi_hand_landmarks:
        for handlans in results.multi_hand_landmarks:
            for id,lm in enumerate(handlans.landmark):

                h,w,c=img.shape
                cx,cy=int(lm.x *w),int(lm.y *h)
                print(id,cx,cy)
                if id ==0:
                    cv2.circle(img,(cx,cy),25,(255,0,255),cv2.FILLED)
            mpdraw.draw_landmarks(img,handlans,mphands.HAND_CONNECTIONS)


    #Calcul fps
    cTime=time.time()
    fps=1/(cTime-pTime)
    pTime=cTime

    #Afficher
    cv2.putText(img,f"{int(fps)}",(10,70),cv2.FONT_HERSHEY_PLAIN,3,(255,0,255),3)


    cv2.imshow('img',img)
    cv2.waitKey(1)