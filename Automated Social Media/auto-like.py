from pynput.keyboard import Key, Controller
import time
keyboard = Controller()
time.sleep(3)
while True:
    keyboard.press('j')
    keyboard.release('j')

    keyboard.press('l')
    keyboard.release('l')
    time.sleep(3)
    keyboard.press(2192)
    keyboard.release(2192)
    time.sleep(3)
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)