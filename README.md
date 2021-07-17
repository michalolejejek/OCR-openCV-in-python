# OCR-openCV-in-python

## Table of contents
* [General info](#General)
* [Technologies](#technologies)
* [Setup and run](#setup-and-run)


## General

##### What is OCR
Optical Character Recognition - a set of activities, algorithms, or software to recognize characters and texts in an image file.

Simplifying this, it is getting a text from a graphic file by a computer program.



## Technologies

##### Project is created with:
* pytesseract
* openCV



## Setup and run

##### Installing important libraries

###### On Linux

'$ sudo apt-get update
$ sudo apt-get install libleptonica-dev 
$ sudo apt-get install tesseract-ocr tesseract-ocr-dev
$ sudo apt-get install libtesseract-dev
$ sudo apt install python3-opencv'

###### On Mac

'brew install opencv
brew install tesseract'


###### On Windows

download binary from https://github.com/UB-Mannheim/tesseract/wiki. 
then uncoment this line in script

'pytesseract.pytesseract.tesseract_cmd = 'C:\Program Files (x86)\Tesseract-OCR\tesseract.exe' '

Now you can install tesseract by pip


'pip install tesseract

pip install tesseract-ocr'

and install openCV

'pip install opencv-python'




