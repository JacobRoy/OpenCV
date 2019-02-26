import cv2
import numpy as np

image = ('./../images/Sunflower Field Painting.jpg',cv2.IMREAD_GRAYSCALE)

detector = cv2.SimpleBlobDetector_create()
image_data = np.asarray(image)
keypoints = detector.detect(image_data)

blank = np.zeros((1,1))
blobs = cv2.drawKeypoints(image,keypoints,blank,(0,255,255),cv2.DRAW_MATCHES_FLAGS_DEFAULT)

cv2.imshow('Blobs',blobs)
cv2.waitKey(0)
cv2.destroyAllWindows()
