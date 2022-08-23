import cv2
from paddleocr import PaddleOCR,draw_ocr
from PIL import Image
# Paddleocr supports Chinese, English, French, German, Korean and Japanese.
# You can set the parameter `lang` as `ch`, `en`, `french`, `german`, `korean`, `japan`
# to switch the language model in order.
ocr = PaddleOCR(use_angle_cls=True, lang='en',use_gpu=False ) # need to run only once to download and load model into memory

# draw result
cam = cv2.VideoCapture(0)

img_counter = 0

while  True:
    ret,frame = cam.read()

    if not ret:
        print("failed to grab frame")
        break
    cv2.imshow("test",frame)

    k = cv2.waitKey(1)
    if k%256 == 27:
        print("ESC hit, closing app...")
        break
    elif k%256 == 32:
        img_name = "camera_saves/opencv_frame_{}.png".format(img_counter)
        cv2.imwrite(img_name,frame)

        img_path = img_name
        result = ocr.ocr(img_path, cls=True)
        for line in result:
            print(line)

        image = Image.open(img_name).convert('RGB')
        boxes = [line[0] for line in result]
        txts = [line[1][0] for line in result]
        scores = [line[1][1] for line in result]
        im_show = draw_ocr(image, boxes, txts, scores, font_path='ppocr_img/fonts/latin.ttf')
        im_show = Image.fromarray(im_show)
        img_name = "camera_saves/paddle_frame_{}.png".format(img_counter)
        im_show.save(img_name)

        print("screenshot taken")
        img_counter+=1

cam.release()
cam.destroyAllWindows()