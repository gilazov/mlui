# https://pypi.org/project/pure-python-adb/
from core import *

for device in connectAndGetDevices():
    scroll_up(device)
    delay(5)
    tap(device, 'item_back.jpg')

