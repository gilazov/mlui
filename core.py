# https://pypi.org/project/pure-python-adb/
import cv2
import numpy as np
import time
from adb.client import Client as AdbClient
from imageai.Prediction import ImagePrediction
from imageai.Detection import ObjectDetection
import os

execution_path = os.getcwd()
prediction = ImagePrediction()
prediction.setModelTypeAsResNet()
prediction.setModelPath(os.path.join(execution_path, "resnet50_weights_tf_dim_ordering_tf_kernels.h5"))
print(os.path.join(execution_path, "resnet50_weights_tf_dim_ordering_tf_kernels.h5"))
prediction.loadModel()

execution_path = os.getcwd()

detector = ObjectDetection()
detector.setModelTypeAsYOLOv3()
detector.setModelPath( os.path.join(execution_path , "yolo.h5"))
detector.loadModel()


def findOneAndGetCenter(screenshot_src, item_src):
    img_rgb = cv2.imread(screenshot_src)
    img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)
    template = cv2.imread(item_src, 0)
    w, h = template.shape[::-1]

    method = cv2.TM_CCOEFF_NORMED
    res = cv2.matchTemplate(img_gray, template, method)

    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)

    if method in [cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]:
        top_left = min_loc
    else:
        top_left = max_loc
    bottom_right = (top_left[0] + w, top_left[1] + h)

    center = ((top_left[0] + bottom_right[0])/2, (top_left[1] + bottom_right[1])/2)

    return center

def findOne():
    img_rgb = cv2.imread('screens/1.jpg')
    img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)
    template = cv2.imread('items/item_back.jpg', 0)
    w, h = template.shape[::-1]

    method = cv2.TM_CCOEFF_NORMED
    res = cv2.matchTemplate(img_gray, template, method)

    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)

    if method in [cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]:
        top_left = min_loc
    else:
        top_left = max_loc
    bottom_right = (top_left[0] + w, top_left[1] + h)
    img = img_rgb.copy()

    cv2.rectangle(img, top_left, bottom_right, 255, 2)

    cv2.imwrite('res.png', img)

# получаем несколько вхождений
def findAll():
    img_rgb = cv2.imread('screens/1.jpg')
    img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)
    template = cv2.imread('items/item_home.jpg', 0)
    w, h = template.shape[::-1]

    method = cv2.TM_CCOEFF_NORMED
    res = cv2.matchTemplate(img_gray, template, method)
    threshold = 0.8
    loc = np.where(res >= threshold)
    for pt in zip(*loc[::-1]):
        cv2.rectangle(img_rgb, pt, (pt[0] + w, pt[1] + h), (0, 0, 255), 2)

    cv2.imwrite('res.png', img_rgb)

def connectAndGetDevices():
    # Connect to devices Default is "127.0.0.1" and 5037
    client = AdbClient(host="127.0.0.1", port=5037)
    devices = client.devices()
    return devices

def takeScreenShot(device):
    # take a screenshot
    result = device.screencap()
    screenshotPath = "screens/screen.png"
    with open(screenshotPath, "wb") as fp:
        fp.write(result)
    return screenshotPath

def tap(device, item):
    # detect item
    item_x, item_y = findOneAndGetCenter(takeScreenShot(device), 'items/' + item)

    # tap home button
    device.shell('input tap ' + str(item_x) + " " + str(item_y))

def double_tap(device, item):
    # detect item
    item_x, item_y = findOneAndGetCenter(takeScreenShot(device), 'items/' + item)

    # tap home button
    device.shell('input tap ' + str(item_x) + " " + str(item_y))
    time.sleep(0.4)
    device.shell('input tap ' + str(item_x) + " " + str(item_y))

def scroll_up(device):
    device.shell('input swipe 300 300 500 1000')

def scroll_down(device):
    device.shell('input swipe 500 1000 300 300')

def scroll_down_before_find(device):
    device.shell('input swipe 500 1000 300 300')


def delay(sec):
    time.sleep(sec)




