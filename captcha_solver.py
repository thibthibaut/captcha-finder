import cv2
import numpy as np
import pytesseract as ts

def solve(path):
    img = cv2.imread(path)

    h, w, _ = img.shape

    # Crop
    img = img[10:h-10, 0:w]


    # Threshold
    _, img = cv2.threshold(img,145,255,cv2.THRESH_BINARY)


    # Dilate
    kernel = np.ones((3,3),'uint8')
    img = cv2.dilate(img, kernel )
    img = cv2.dilate(img, kernel )

    # Erode
    img = cv2.erode(img, kernel )
    img = cv2.erode(img, kernel )

    tesseract_config = r"""-c tessedit_char_whitelist=123456789abcdefghijklmnprstuvwxyzABCDEFGHIJKLMNPRSTUVWXYZ -c load_system_dawg=0 -c load_freq_dawg=0 --psm 6 --oem 1"""
    tesseract_language = "eng"

    return ts.image_to_string(img, lang=tesseract_language, config=tesseract_config)

    # cv2.imwrite('./test.png', img)



