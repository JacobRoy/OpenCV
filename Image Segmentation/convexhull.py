import cv2
import numpy as np 

image = cv2.imread('./../images/jr.jpg')
orig_image = image.copy()
cv2.imshow('Original Image',orig_image)
cv2.waitKey(0)

gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
ret,thresh = cv2.threshold(gray,127,255,cv2.THRESH_BINARY_INV)

_, contours, _ =   cv2.findContours(thresh.copy(),cv2.RETR_LIST,cv2.CHAIN_APPROX_NONE)

n = len(contours)-1
contours = sorted(contours,key=cv2.contourArea,reverse=False)[:n]

for c in contours:
    hull = cv2.convexHull(c)
    cv2.drawContours(image,[hull],0,(0,255,0),2)
    cv2.imshow('Convex hull',image)

cv2.waitKey(0)
cv2.destroyAllWindows()