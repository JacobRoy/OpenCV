import cv2
import numpy as np 

image = cv2.imread('./../images/road.jpg',0)

Gaussian = cv2.GaussianBlur(image,(7,7),0)
cv2.imshow("Gaussian Blurring",Gaussian)
cv2.waitKey(0)

cv2.destroyAllWindows()