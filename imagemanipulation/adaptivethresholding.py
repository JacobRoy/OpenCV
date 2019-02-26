import cv2
import numpy as np 

image = cv2.imread('./vertical-black-to-white-gradient.jpg')
cv2.imshow("Original",image)
cv2.waitKey(0)

image = cv2.GaussianBlur(image,(3,3),0)

thresh = cv2.adaptiveThreshold(image,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,3,5)
cv2.imshow("Adaptive Mean_C thresholding",thresh)
cv2.waitKey(0)

_, th2 = cv2.threshold(image,0,255,cv2.THRESH_BINARY + cv2.THRESH_OTSU)
cv2.imshow("Otsu's Thresholding",thresh)
cv2.waitKey(0)

blur = cv2.GaussianBlur(image,(5,5),0)
_, th3 = cv2.threshold(blur,0,255,cv2.THRESH_BINARY + cv2.THRESH_OTSU)
cv2.imshow("Gaussian Otsu's Thresholding",thresh)
cv2.waitKey(0)

cv2.destroyAllWindows()
