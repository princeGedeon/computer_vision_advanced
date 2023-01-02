import cv2
import mediapipe as mp
import time










class handDetector():
    def __init__(self,mode=False,maxHands=2,model_complexy=1,detectionCon=0.5,trackingCon=0.5):
        self.mode=mode
        self.maxHands=maxHands
        self.detectionCon=detectionCon
        self.model_complexy=model_complexy
        self.trackCon=trackingCon

        self.mphands = mp.solutions.hands
        self.hands = self.mphands.Hands(self.mode,self.maxHands,self.model_complexy,self.detectionCon,self.trackCon)
        self.mpdraw = mp.solutions.drawing_utils


    def findHands(self,img,draw=True):
        imgRGB=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
        self.results=self.hands.process(imgRGB)
        if self.results.multi_hand_landmarks:
            for handlans in self.results.multi_hand_landmarks:
                if draw:
                    self.mpdraw.draw_landmarks(img,handlans,self.mphands.HAND_CONNECTIONS)
        return img

    def findPosition(self,img,handNo=0,draw=True):
        lmList=[]
        #if self.results.

                
             #   for id,lm in enumerate(handlans.landmark):

              #      h,w,c=img.shape
               #     cx,cy=int(lm.x *w),int(lm.y *h)
                #    print(id,cx,cy)
                  #  if id ==0:
                   #     cv2.circle(img,(cx,cy),25,(255,0,255),cv2.FILLED)

pTime=0
cTime=0

print("hello")





def main():
    pTime = 0
    cTime = 0
    cap = cv2.VideoCapture(0)
    dectector=handDetector()
    print("hello")
    while True:

        sucess, img = cap.read()
        dectector.findHands(img)
        # Calcul fps
        cTime = time.time()
        fps = 1 / (cTime - pTime)
        pTime = cTime

        # Afficher
        cv2.putText(img, f"{int(fps)}", (10, 70), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 255), 3)

        cv2.imshow('img', img)
        cv2.waitKey(1)


main()