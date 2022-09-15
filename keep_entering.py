import pyautogui
import time
from threading import Timer

def setInterval(timer, task):
    isStop = task()
    if not isStop:
        Timer(timer, setInterval, [timer, task]).start()


def hello():
    pyautogui.hotkey('alt', 'tab')
    time.sleep(1)
    pyautogui.press('enter')
    return False # return True if you want to stop

if __name__ == "__main__":
    setInterval(15, hello) # every 2 seconds, "do something" will be printed

# pyautogui.hotkey('alt', 'tab')
# pyautogui.press('enter')