import cv2
import numpy as np 

image = cv2.imread('./black-background-white-font-believe-in-yourself-460x460.jpg',0)
cv2.imshow("Original",image)
cv2.waitKey(0)

kernel = np.ones((5,5),np.uint8)

# Erosion
erosion = cv2.erode(image,kernel,iterations=1)
cv2.imshow("Erosion",erosion)
cv2.waitKey(0)

# Dilation
dilation = cv2.dilate(image,kernel,iterations=1)
cv2.imshow("Dilation",dilation)
cv2.waitKey(0)

#Opening - erosion followed by dilation
opening = cv2.morphologyEx(image,cv2.MORPH_OPEN,kernel)
cv2.imshow("Opening",opening)
cv2.waitKey(0)

# Closing - dilation followed by erosion
closing = cv2.morphologyEx(image,cv2.MORPH_CLOSE,kernel)
cv2.imshow("Closing",closing)
cv2.waitKey(0)

cv2.destroyAllWindows()