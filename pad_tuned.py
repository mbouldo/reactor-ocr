from threading import Timer
import keyboard  # using module keyboard
from time import sleep
import time
import sys
import pprint
import re
import cv2
from paddleocr import PaddleOCR,draw_ocr
from PIL import Image


pp = pprint.PrettyPrinter(indent=4)

pattern = re.compile("^[0-9]*\.?[0-9]*$")

ocr = PaddleOCR(use_angle_cls=True, lang='en',use_gpu=False ) # need to run only once to download and load model into memory

def readImage(img_counter,img_path):
    result = ocr.ocr(img_path, cls=True)

    for line in result:
        coordinates = line[1]
        capturedText = line[1][0]
        confidence = line[1][1]
        
        if(pattern.match(capturedText)):
            print(capturedText, confidence)
            print('match')

    image = Image.open(img_path).convert('RGB')
    boxes = [line[0] for line in result]
    txts = [line[1][0] for line in result]
    scores = [line[1][1] for line in result]
    im_show = draw_ocr(image, boxes, txts, scores, font_path='ppocr_img/fonts/latin.ttf')
    im_show = Image.fromarray(im_show)

    img_name = "camera_saves/paddle_frame_{}.png".format(img_counter)
    im_show.save(img_name)

readImage('test1','camera_saves/trail 2/opencv_frame_1.png')