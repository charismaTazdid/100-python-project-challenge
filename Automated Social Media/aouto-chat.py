import time
import pyautogui

# while True:
#     time.sleep(4)
#     pyautogui.typewrite("are you ok?")
#     time.sleep(3)
#     pyautogui.press('enter')
    
message = ['I miss you', 'I love you', 'I am sorry', 'forgive me', 'trust me', 'She is my JustFried']

for index in range (100):
    time.sleep(4)
    pyautogui.typewrite(message [index % 6])
    time.sleep(3)
    pyautogui.press('enter')