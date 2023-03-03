import pyautogui 
import os 

import random
import math

def init():
    pyautogui.FAILSAFE = False
    pyautogui.PAUSE = 0.01

def get_Path(file_name):
    Path = os.path.dirname(os.path.abspath(__file__))
    my_file = os.path.join(Path, file_name)
    return my_file

def mouseUp():
    pyautogui.mouseUp()
def mouseDown():
    pyautogui.mouseDown()
def moveMouse(x, y):
    pyautogui.moveTo(x, y)

def moveTo(x, y):
    pyautogui.moveTo(x, y)

def holdKey(key):
    down(key)
    up(key)

def clickMouse(x, y, btn = 'left'):
    pyautogui.click(x = x, y =  y, button=btn)

def down(key):
    pyautogui.keyDown(key)
def up(key):
    pyautogui.keyUp(key)

def objectPosition(name, con = .9):
    obj = pyautogui.locateOnScreen(get_Path(name), confidence = con)
    if obj != None:
        dic = obj
        x = dic[0]
        y = dic[1]
        return [x, y]
    return [-1, -1]    
def ScreenShot(img_name_gold, area):
    im = pyautogui.screenshot(img_name_gold, region=area)
    return im
def clickThePic(name, btn = 'left', con = .5):
    obj = pyautogui.locateOnScreen(get_Path(name), confidence = con)
    if obj != None:
        dic = obj
        x = dic[0]
        y = dic[1]
        clickMouse(x, y, btn)

def thisPicExist(name, con = .5):
    obj = pyautogui.locateOnScreen(get_Path(name), confidence = con)
    if obj != None:
        return 1
    return 0