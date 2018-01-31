from PIL import ImageGrab
import numpy
import time
import pyautogui
from pynput.keyboard import Key,Controller

key=Controller()
web=(200,300)
box=(480,790,570,810)



def startgame():
    pyautogui.click(web)
    time.sleep(0.03)
    pyautogui.keyDown('space')
    time.sleep(0.03)
    pyautogui.keyUp('space')
    print('game start')

def jump():
    key.press(Key.space)
    print('jump')
    time.sleep(0.06)
    key.release(Key.space)

def imageGrab():
    image=ImageGrab.grab(box)
    image=image.convert('1')
    a=numpy.array(image.getcolors())
    print(a.sum())
    return a.sum()







def main():
    last=time.time()
    startgame()
    while 1:
        if imageGrab()!=6255:
            jump()
        print(time.time()-last)
        last=time.time()

main()