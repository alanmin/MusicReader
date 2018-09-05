import cv2 
import numpy as np
import matplotlib.pyplot as plt
import math

#Returns the value of the image at percent 
def get_threshold(img, percent = .9) :
	pix_vals = img.ravel()
	return(sorted(pix_vals)[math.floor(len(pix_vals) * percent)]) 


#returns the image resized with a width of width. Keeps aspect ratio
#if we need to shrink, use INTER_AREA interpolation
#if we need to enlarge, use INTER_CUBIC interpolation
def resize_img(img, width = 800) :
	img_h, img_w, junk = img.shape
	ratio = width/img_w
	if(img_w > width) :
		return(cv2.resize(img, None, fx = ratio, fy = ratio,
			interpolation=cv2.INTER_AREA))
	else :
		return(cv2.resize(img, None, fx = ratio, fy = ratio,
			interpolation = cv2.INTER_CUBIC))



img_names = ['img_0001.png', 'img_0002.jpeg', 'img_0003.jpg']
img_thresholds = [.08, .08, .08]

for i in range(len(img_names)) :
	name = img_names[i]
	thresh_val = img_thresholds[i]
	
	img = cv2.imread('test_photos/' + name, cv2.IMREAD_COLOR)
	img = resize_img(img)
	print(img.shape)
	img_grey = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
	j, thresh = cv2.threshold(img_grey, get_threshold(img_grey, img_thresholds[i]),
		255,cv2.THRESH_BINARY)
	cv2.imshow(name, thresh)

cv2.waitKey(0)
cv2.destroyAllWindows()
