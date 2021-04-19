import numpy as np
import cv2
from pyzbar.pyzbar import decode

#frame = cv2.VideoCapture(0)
frame = cv2.VideoCapture(1)
frame.set(3,720)
frame.set(4,540)


with open("AuthorizedStuff.txt",'rb') as f:
    AuthorizedList = f.read().splitlines()


while True:

    success, img = frame.read()
    for code in decode(img):
        decoded = code.data.decode('utf-8')
        print(decoded)

        if decoded in AuthorizedList:
            result = "Authorized"
            color = (108, 16, 154)
        else:
            result = "Un-Authorized"
            color = (0,0,255)

        barcode = np.array([code.polygon],np.int32)
        barcode = barcode.reshape((-1,1,2))
        cv2.polylines(img,[barcode],True,color,4)
        points = code.rect
        cv2.putText(img,result,(points[0],points[1]),cv2.FONT_HERSHEY_COMPLEX,0.9,color,3)

    cv2.imshow('QR Code Reader', img)
    cv2.waitKey(10000)