import cv2.cv2 as cv2
import multiprocessing
import numpy as np
import os

###############################
frameWidth = 640
frameHeight = 480
plateCascade = cv2.CascadeClassifier(r'E:\Jarek\Python\Python38projects\LaneLines1\Lib\site-packages\cv2\data\haarcascade_russian_plate_number.xml')
minArea = 500
color = (255, 0, 255)
count = 0
i = 0
# if os.path.exists('Vid/vid_'+str(i)+'.avi'):
#    i = i + 1
######  MULTIPROCESSING  ############
e = multiprocessing.Event()
p = None
#################################
#count=count+1
#i = i + 1
def cap1(e):
   i = 0
   count = 0
   cap = cv2.VideoCapture(0)
   fourcc = cv2.VideoWriter_fourcc(*'XVID')
   fileName = 'Vid/vid_{}.avi'
   while os.path.isfile(fileName.format(i)):
      i = i + 1
   fileName = fileName.format(i)
   out = cv2.VideoWriter(fileName.format(i), fourcc, 20.0, (640,480))
   #i=i+1
   cap.set(3, frameWidth)
   cap.set(4, frameHeight)
   cap.set(10, 150)
#################################
###############################q
   while True:
      success, img = cap.read()
      imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
      plates = plateCascade.detectMultiScale(imgGray, 1.3, 4)
      images = []
      # out1 = cv2.VideoWriter('Vid/vid_' + str(i) + '.avi', fourcc, 20.0, (640, 480))
      # i = i + 1
      for (x, y, w, h) in plates:
         area = w * h
         if area > minArea:
            cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
            cv2.putText(img, "Plate Number", (x, y - 5),
                        cv2.FONT_HERSHEY_COMPLEX, 1, color, 2)
            imgRoi = img[y:y + h, x:x + w]
            cv2.imshow("ROI", imgRoi)
            cv2.waitKey(500)

            cv2.imwrite('Res/Plate_'+str(count)+'.jpg', imgRoi)
            count= count + 1

      out.write(img)

      # img = cv2.Canny(img, 20, 60)
      # cv2.imshow('res',img)
      cv2.imshow('Video',img)
      if cv2.waitKey(1) & 0xFF == ord('q'):
           break
      elif e.is_set():
         cap.release()
         out.release()
         cv2.destroyAllWindows()
         e.clear()