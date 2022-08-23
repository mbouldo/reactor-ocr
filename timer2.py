from threading import Timer
import keyboard  # using module keyboard
from time import sleep
import time
import sys

import cv2
from paddleocr import PaddleOCR,draw_ocr
from PIL import Image

class RepeatedTimer(object):
    def __init__(self, interval, function, *args, **kwargs):
        self._timer     = None
        self.interval   = interval
        self.function   = function
        self.args       = args
        self.kwargs     = kwargs
        self.is_running = False
        self.start()

    def _run(self):
        self.is_running = False
        self.start()
        self.function(*self.args, **self.kwargs)

    def start(self):
        if not self.is_running:
            self._timer = Timer(self.interval, self._run)
            self._timer.start()
            self.is_running = True

    def stop(self):
        self._timer.cancel()
        self.is_running = False

cam = cv2.VideoCapture(0)



def hello(name):
    img_counter = int(time.time())
    ret,frame = cam.read() 
    img_name = "camera_saves/opencv_frame_{}.png".format(img_counter)
    cv2.imwrite(img_name,frame)
    print("screenshot taken")
    readImage(img_counter,img_name)

def readImage(img_counter,img_path):
    result = ocr.ocr(img_path, cls=True)
    for line in result:
        print(line)

    image = Image.open(img_path).convert('RGB')
    boxes = [line[0] for line in result]
    txts = [line[1][0] for line in result]
    scores = [line[1][1] for line in result]
    im_show = draw_ocr(image, boxes, txts, scores, font_path='ppocr_img/fonts/latin.ttf')
    im_show = Image.fromarray(im_show)

    img_name = "camera_saves/paddle_frame_{}.png".format(img_counter)
    im_show.save(img_name)

print ("loading PaddleOCR")
ocr = PaddleOCR(use_angle_cls=True, lang='en',use_gpu=False ) # need to run only once to download and load model into memory


while True:  # making a loop
    ret,frame = cam.read()

    if not ret:
        print("failed to grab frame")
        break
    cv2.imshow("test",frame)
    k = cv2.waitKey(1)
    if k%256 == 27:
        print("ESC hit, closing app...")
        cam.release()
        cam.destroyAllWindows()
        break
    elif k%256 == 32:    
        print('start program')
        rt = RepeatedTimer(5, hello, "World") # it auto-starts, no need of rt.start()

