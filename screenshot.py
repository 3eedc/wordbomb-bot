from global_hotkeys import *
import os, pyautogui, cv2, pytesseract, keyboard, time

cwd = os.getcwd()
sspath = os.path.join(cwd, 'screenshot.png')
wordlistpath = open(os.path.join(cwd, 'wordlist.txt'))
lines = wordlistpath.readlines()
wordlist = []
wordlist = lines
latestword = ''
is_alive = True

def read():
    ss = pyautogui.screenshot(region=(760, 730, 100, 40))
    ss.save(sspath)
    ss = cv2.imread(sspath)
    monochromess = cv2.cvtColor(ss, cv2.COLOR_BGR2GRAY)
    darkerss = cv2.convertScaleAbs(monochromess, 1.5, 10)
    return pytesseract.image_to_string(darkerss, config='--psm 10')

def solve():
    prompt = read().strip().lower()
    print(prompt)
    for i in wordlist:
        if prompt in i:
            wordlist.remove(i)
            return(i)
        else:
            pass
        print(latestword)

def win():
    keyboard.press('backspace')
    keyboard.write(solve(), delay=0.05)

bindings = [
    ["1", None, win, True],
]

register_hotkeys(bindings)

start_checking_hotkeys()

while is_alive:
    time.sleep(0.1)