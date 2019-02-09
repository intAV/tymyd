# -*- coding: utf-8 -*-

import cv2
import aircv as ac
import time
import win32gui, win32ui, win32con, win32api
import pyautogui

  
def getXY(obj):
    imsrc = ac.imread('bg.png')
    imobj = ac.imread(obj)

    pos = ac.find_template(imsrc, imobj)
    bitxy = pos['result']
    print bitxy
    return bitxy


def wincat(filename):
    hwnd = 0
    hwndDC = win32gui.GetWindowDC(hwnd)
    mfcDC = win32ui.CreateDCFromHandle(hwndDC)
    saveDC = mfcDC.CreateCompatibleDC()
    saveBitMap = win32ui.CreateBitmap()
    MoniterDev = win32api.EnumDisplayMonitors(None, None)
    w = MoniterDev[0][2][2]
    h = MoniterDev[0][2][3]
    saveBitMap.CreateCompatibleBitmap(mfcDC, w, h)
    saveDC.SelectObject(saveBitMap)
    saveDC.BitBlt((0, 0), (w, h), mfcDC, (0, 0), win32con.SRCCOPY)
    saveBitMap.SaveBitmapFile(saveDC, filename)




while True:
    '''
    wincat('bg.png')
    try:
        bitxy = getXY('obj.png')
        print bitxy
        #bity = bitxy[1]
        bitx = bitxy[0]
        bity = bitxy[1] - 20
        pyautogui.moveTo(bitx,bity)
        pyautogui.doubleClick()
        #pyautogui.click()
    except:
        print "null"
        '''
    pyautogui.moveTo(798,490,duration=1,tween=pyautogui.easeInQuad)
    pyautogui.doubleClick()
    time.sleep(2)

