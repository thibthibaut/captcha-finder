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


    return (ts.image_to_string(img, lang='eng', config="--psm 6 --oem 1 -c load_system_dawg=0 -c load_freq_dawg=0 -c tessedit_char_whitelist=ABCDEFGHIJKLMNPRSTUVWXYZabcdefghijklmnprstuvwxyz123456789"))

    # cv2.imwrite('./test.png', img)



