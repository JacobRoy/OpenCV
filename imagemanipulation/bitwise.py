import cv2
import numpy as np 

square = cv2.imread('./Square.jpg')
ellipse = cv2.imread('./Ellipse.jpg')

And = cv2.bitwise_and(square,ellipse)
cv2.imshow("And",And)
cv2.waitKey(0)

Or = cv2.bitwise_or(square,ellipse)
cv2.imshow("Or",Or)
cv2.waitKey(0)

xor = cv2.bitwise_xor(square,ellipse)
cv2.imshow("Xor",xor)
cv2.waitKey(0)

bitwise_not_img = cv2.bitwise_not(square,ellipse)
cv2.imshow("Not",bitwise_not_img)
cv2.waitKey(0)

cv2.destroyAllWindows()