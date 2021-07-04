import cv2
import numpy as np
from pyzbar.pyzbar import decode

cap = cv2.VideoCapture(0)
cap.set(3,420) #width of frames in video feed
cap.set(4,640) #height of frames in video feed

while True:
	ret,img = cap.read()
	for barcode in decode(img):
		my_data = barcode.data.decode('utf-8')
		print (my_data)
		pts = np.array([barcode.polygon],np.int32) #boundary of barcode
		pts.reshape((-1,1,2))
		cv2.polylines(img,[pts],True,(0,0,255),4) #5 is thickness
		pts2 = barcode.rect      #rectangle boundary
		cv2.putText(img,my_data,(pts2[1],pts2[3]),cv2.FONT_HERSHEY_PLAIN,1.2,(255,128,0),2)

	cv2.imshow('answer',img)
	cv2.waitKey(1)

cv2.destroyAllWindows()

