import cv2
import numpy as np
import sys

grey = cv2.imread(sys.argv[1], cv2.CV_LOAD_IMAGE_GRAYSCALE)

h, w = grey.shape
if h > 600:
	grey = cv2.resize(grey, (w/4, h/4))
else:
	grey = cv2.resize(grey, (w*2, h*2))	

h, w = grey.shape

rangeImg = cv2.inRange(grey, 200, 255)

cv2.imshow("grey", grey)
cv2.imshow("range", rangeImg)

# blur = cv2.blur(rangeImg, (3,3))
# rangeImg = cv2.addWeighted(rangeImg, 1.5, blur, -0.5, 0)
# cv2.imshow("blur", rangeImg)
print rangeImg.dtype
contours, _ = cv2.findContours(rangeImg, cv2.RETR_CCOMP, cv2.CHAIN_APPROX_NONE)
# print contours
print len(contours)
print type(contours)

maxArea = w * h * 0.00018
finalContours = []

for contour in contours:
	area = cv2.contourArea(contour)
	permieter = cv2.arcLength(contour, True)
	moments = cv2.moments(contour)

	if area < 200 and area > 0:
		finalContours.append(contour)
		print area, permieter
		print moments

print "Final contours", len(finalContours)

origContours = np.copy(grey)
cv2.drawContours(origContours, contours, -1, 255, 2)

cv2.drawContours(grey, finalContours, -1, 255, 2)

cv2.imshow("origContours", origContours)
cv2.imshow("contours", grey)

cv2.waitKey(0)


