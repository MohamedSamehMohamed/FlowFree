from pyautogui import *
import pyautogui
import time
import keyboard
import random
import win32api, win32con
import math
import pydirectinput
import os 

def get_Path(file_name):
    Path = os.path.dirname(os.path.abspath(__file__))
    my_file = os.path.join(Path, file_name)
    return my_file

def moveMouse(x, y):
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

def click_fast():
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)

def objectPosition(name, con = .9):
    obj = pyautogui.locateOnScreen(get_Path(name), confidence = con)
    if obj != None:
        dic = obj
        x = dic[0]
        y = dic[1]
        return [x, y]
    return [-1, -1]    

def clickThePic(name, btn = 'left', con = .9):
    obj = pyautogui.locateOnScreen(get_Path(name), confidence = con)
    if obj != None:
        dic = obj
        x = dic[0]
        y = dic[1]
        clickMouse(x, y, btn)

def thisPicExist(name, con = .9, grayscaleval=False):
    obj = pyautogui.locateOnScreen(get_Path(name), confidence = con, grayscale=grayscaleval)
    if obj != None:
        return 1
    return 0
def read_solution():
    order_list = []
    file = open(get_Path('out.txt'))
    for line in file:
        list = []
        for p in line[:-1].split(' '):
            list.append(int(p))
        order_list.append(list)
    file.close()
    return order_list

def appendToFile(lines):
    file = open(get_Path('input.txt'), 'w')
    for i in lines:    
        file.write(str(i) + ' ')
    file.close()
            
def solve(mat, sz):
    #os.system('g++ main.cpp')
    list = []
    list.append(sz)
    list.append(sz)
    for i in range(sz):
        for j in range(sz):
            list.append(mat[i][j][0])
            list.append(mat[i][j][1])
            list.append(mat[i][j][2][0])
            list.append(mat[i][j][2][1])
            list.append(mat[i][j][2][2])
    appendToFile(list)

    proc = subprocess.Popen(get_Path('a.exe'))
    proc.wait()
    order_list = read_solution()
    print(order_list)
    first_time = 1 
    for i in order_list:
        time.sleep(.1)
        if first_time:
            pyautogui.moveTo(mat[i[0]][i[1]][0], mat[i[0]][i[1]][1]) 
            pyautogui.mouseDown()
            first_time = 0
        if i[0] != -1:
            pyautogui.moveTo(mat[i[0]][i[1]][0], mat[i[0]][i[1]][1]) 
        else:
            pyautogui.mouseUp()
            first_time = 1
    pyautogui.mouseUp()        
    
def see_it(sz):
    img_name_gold = 'name.png'
    [x, y] = objectPosition(name='upper.PNG')
    [x1, y1] = objectPosition(name='upper_right.PNG')
    H = x1 - x + 1
    W = x1 - x + 1
    y += 120
    im = pyautogui.screenshot(img_name_gold, region=(x,y, W, H))
    width = 1 
    hight = 1
    hight_step = H // sz
    width_step = W // sz
    mat = []
    vis = []
    center_value = 25 
    tot = sz * sz 
    while width < W:
        hight = 4 
        list = []
        row_tot = sz 
        while hight < H:
            if tot == 0 or row_tot == 0:
                break 
            #clickMouse(x + hight + center_value, y + width + center_value)
            tot-=1
            row_tot-=1
            #time.sleep(.5)
            X = x + hight + center_value
            Y = y + width + center_value
            #print(X - x, Y - y)
            list.append((X, Y, im.getpixel((X- x, Y - y))))
           # print(pyautogui.pixel(X, Y))
            hight += hight_step
        width += width_step
        mat.append(list)
    solve(mat, sz)
    
import subprocess
    
def main():
    pyautogui.FAILSAFE = False
    pyautogui.PAUSE = 0.01
    cnt = 0
    while cnt < 5:
        cnt += 1 
        see_it(6)
        while not thisPicExist('next.png'):
            continue
        clickThePic('next.png')
        time.sleep(2)    

if __name__ == "__main__":
    main()