import cv2
import numpy as np 

image = cv2.imread('./vertical-black-to-white-gradient.jpg')
cv2.imshow("Original",image)

ret,thresh1 = cv2.threshold(image,127,255,cv2.THRESH_BINARY)
cv2.imshow("Threshold Binary",thresh1)
cv2.waitKey(0)

ret,thresh2 = cv2.threshold(image,127,255,cv2.THRESH_BINARY_INV)
cv2.imshow("Threshold Binary Inverse",thresh2)
cv2.waitKey(0)

ret,thresh3 = cv2.threshold(image,127,255,cv2.THRESH_TRUNC)
cv2.imshow("Threshold Trunc",thresh3)
cv2.waitKey(0)

ret,thresh4 = cv2.threshold(image,127,255,cv2.THRESH_TOZERO)
cv2.imshow("Threshold ToZero",thresh4)
cv2.waitKey(0)

ret,thresh5 = cv2.threshold(image,127,255,cv2.THRESH_TOZERO_INV)
cv2.imshow("Threshold ToZeroInv",thresh5)
cv2.waitKey(0)

cv2.destroyAllWindows()