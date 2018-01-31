from PIL import ImageGrab
import numpy
import time
import pyautogui
from pynput.keyboard import Key,Controller

key=Controller()
web=(260,400)
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
    image=pyautogui.screenshot()
    image.show()
    for n in range(250,260,2):
        a=image.getpixel((n,400))

        print(a[0]+a[1]+a[2])
        if (a[0]+a[1]+a[2])!=741 :
            jump()











def main():
    last=time.time()
    startgame()
    #while 1:
    image = pyautogui.screenshot()
    print(time.time()-last)

'''        if imageGrab():
            jump()
        print(time.time()-last)
        last=time.time()
'''
main()