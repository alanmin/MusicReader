import cv2 

img1 = cv2.imread('test_photos/img_0001.png',cv2.IMREAD_COLOR)
img1_grey = cv2.cvtColor(img1,cv2.COLOR_BGR2GRAY)
thresh1 = cv2.adaptiveThreshold(img1_grey, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 115, 1)

img2 = cv2.imread('test_photos/img_0002.jpeg',cv2.IMREAD_COLOR)
img2_grey = cv2.cvtColor(img2,cv2.COLOR_BGR2GRAY)
thresh2 = cv2.adaptiveThreshold(img2_grey, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 115, 1)

cv2.imshow('grey', img2_grey)
cv2.imshow('thres1', thresh1)
cv2.imshow('thres2', thresh2)
cv2.waitKey(0)
cv2.destroyAllWindows()
