import cv2
import numpy as np 

red = int(input("R:"))
green = int(input("G:"))
blue = int(input("B:"))
color = np.uint8([[[blue,green,red]]])
hsv_color = cv2.cvtColor(color,cv2.COLOR_BGR2HSV)
print(hsv_color)