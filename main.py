import pyautogui

from pynput import keyboard
from pynput.keyboard import Key

pressed = False

print('AutoMinecrafter\nKeyboard shotcuts:\nCtrl - on,off press left mouse button')

def on_release(key):
    global pressed
    if key != Key.ctrl_l:
        return

    if (pressed==False):
        print('Press on')
        pressed = True
        pyautogui.mouseDown(x=0,y=0) # If you want to use in other then rewrite pyautogui.mouseDown(x=0,y=0) with pyautogui.mouseDown()

    else:
        print('Press off')
        pressed = False
        pyautogui.mouseUp(x=0,y=0) # If you want to use in other then rewrite pyautogui.mouseDown(x=0,y=0) with pyautogui.mouseDown()


with keyboard.Listener(on_release=on_release) as listener:
    listener.join()
