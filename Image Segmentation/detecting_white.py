import cv2
import numpy as np 

image = cv2.imread('./../images/lane.jpeg')
cv2.imshow("Original",image)
cv2.waitKey(0)

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
mask_white = cv2.inRange(gray,200, 255)
mask = cv2.bitwise_and(gray,mask_white)

cv2.imshow("Masked",mask)
cv2.waitKey(0)

blur = cv2.GaussianBlur(gray,(5,5),0)
ret,thresh1 = cv2.threshold(blur,225,255,cv2.THRESH_BINARY)

cv2.imshow("Threshold",thresh1)
cv2.waitKey(0)

cv2.destroyAllWindows()