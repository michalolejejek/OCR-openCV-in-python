import cv2
import pytesseract as ptc
import argparse


#Reading image from your drive
#You can read give path to image or have image in the same folder with code
#path = input('input path:')
image = cv2.imread("test.jpeg")

#Making Copy of image
image2 = image.copy()


#Convert all colors to gray scale using openCV2
img_to_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

#programing treshhold
ret, thresh_hold1 = cv2.threshold(img_to_gray, 0, 255, cv2.THRESH_OTSU | cv2.THRESH_BINARY_INV)
rect_kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (18, 18))

#dilation on the threshold image
dilation = cv2.dilate(thresh_hold1, rect_kernel, iterations = 1)

#Finding contours 
cntr, hierarchy = cv2.findContours(dilation, cv2.RETR_EXTERNAL,
												cv2.CHAIN_APPROX_NONE)


#creating text file where we save our result
file = open("output.txt", "w+")
file.write("")
file.close()

for cnt in cntr:
	x, y, w, h = cv2.boundingRect(cnt)
#Making rectangle image
	rect = cv2.rectangle(image2, (x, y), (x + w, y + h), (0, 255, 0), 2)
	
#Making cropbox 
	cpd = image2[y:y + h, x:x + w]
	
#Opening file with output
	file = open("output.txt", "a")
	text = ptc.image_to_string(cpd)
	
#saving output
	file.write(text)
	file.write("\n")
	file.close
