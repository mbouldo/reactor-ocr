import cv2
import pytesseract
import numpy as np
 

pytesseract.pytesseract.tesseract_cmd = r'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'

image = cv2.imread('img/r2.jpg')

dimensions = image.shape
# height, width, number of channels in image
height = image.shape[0]
width = image.shape[1]

	
image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# image = cv2.medianBlur(image, 3)
# image = cv2.threshold(image, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]
# image = cv2.medianBlur(image, 3)


print(width,height)

images = []

r = cv2.selectROI("select the area", image)
cropped_image = image.copy()
cropped_image = cropped_image[int(r[1]):int(r[1]+r[3]),
                      int(r[0]):int(r[0]+r[2])]
images.append(cropped_image)

r = cv2.selectROI("select the area", image)
cropped_image = image.copy()
cropped_image = cropped_image[int(r[1]):int(r[1]+r[3]),
                      int(r[0]):int(r[0]+r[2])]
images.append(cropped_image)



temperature = pytesseract.image_to_string(images[0])
pressure = pytesseract.image_to_string(images[1])

print(temperature,pressure)