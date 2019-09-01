# MLUI

Machine learning UI tests framework for Android apps with autoclicking and image detection.

## Features
* Autoscroll
* Click and double click to elements using object detection
* (WIP) context recognition for click
* (WIP) comparing result for test

## Example

Scrolling, click to home button, pull to refresh

```
scroll_down(device)
delay(2)
scroll_down(device)
delay(2)
tap(device, 'item_home.jpg')
delay(3)
scroll_up(device)
```

Result

![](demo.gif)

## Instaling
Clone this project and open it in PyCharm (all dependecies included in virtualEnv image)

## How to use

Connect device with developer mode and Run script. (Use ``` add devices ``` for obtain device connection status)

## Commands
Click to item 
```
tap(device, 'item_home.jpg')
```

Double Click to item 

```
double_tap(device, 'item_home.jpg')
```

Scroll up/down

```
scroll_up(device)
scroll_down(device)
```
Delay (seconds)

```
delay(5)
```

## Built With
* [pure-python-adb](https://pypi.org/project/pure-python-adb/) - Pure-python implementation of the ADB client.
* [opencv](https://github.com/opencv/opencv) - OpenCV

