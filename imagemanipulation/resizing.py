import cv2
import numpy as np 

image = cv2.imread('./../images/jr.jpg')
cv2.imshow("Original",image)
cv2.waitKey(0)

image_scaled = cv2.resize(image,None,fx=0.75,fy=0.75)
cv2.imshow('Scaled',image_scaled)
cv2.waitKey(0)

image_scaled = cv2.resize(image,None,fx=2,fy=2,interpolation=cv2.INTER_CUBIC)
cv2.imshow('Scaling-Cubic Interpolation',image_scaled)
cv2.waitKey(0)

image_scaled = cv2.resize(image,(900,400),interpolation = cv2.INTER_AREA)
cv2.imshow('Scaling - skewed size',image_scaled)
cv2.waitKey(0)

cv2.destroyAllWindows()