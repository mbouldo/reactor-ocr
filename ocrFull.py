import cv2
import pytesseract
import numpy as np
 

pytesseract.pytesseract.tesseract_cmd = r'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'

image = cv2.imread('img/r2.jpg')
image = cv2.resize(image, None, fx=1.2, fy=1.2, interpolation=cv2.INTER_CUBIC)

kernel = np.ones((1, 1), np.uint8)
image = cv2.dilate(image, kernel, iterations=1)
image = cv2.erode(image, kernel, iterations=1)


gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
thresh = cv2.threshold(gray, 200, 255, cv2.THRESH_BINARY)[1]
thresh = cv2.bitwise_not(thresh)

custom_config = r'-l eng -c tessedit_char_whitelist="1234567890." '
pressureText = pytesseract.image_to_string(image,config=custom_config)

h, w, c = image.shape
boxes = pytesseract.image_to_boxes(image,config=custom_config) 
for b in boxes.splitlines():
    b = b.split(' ')
    image = cv2.rectangle(image, (int(b[1]), h - int(b[2])), (int(b[3]), h - int(b[4])), (0, 255, 0), 2)

cv2.imshow('image', image)
cv2.waitKey(0)


print(pressureText)