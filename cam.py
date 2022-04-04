import requests
import cv2
import numpy as np
import imutils

url = "https://100.64.124.240:8080/shot.jpg"

while True:
    img_resp = requests.get(url)
    img_arr = np.array(bytearray(img_resp.content), dtype=np.uint8)
    img = cv2.imdecoder(img_arr, -1)
    img = imutils.resize(img, wigth = 1000, height = 1800)
    cv2.imshow("Android_cam_", img)

    if cv2.waitkey(1) == 27:
        break

cv2.destroyAllWindows()