from global_hotkeys import *
import os, pyautogui, cv2, pytesseract, time, keyboard

cwd = os.getcwd()
sspath = os.path.join(cwd, 'screenshot.png')
wordlist = open(os.path.join(cwd, 'wordlist.txt')).readlines()

is_alive = True
solvehotkey = '1'
exithotkey = '2'

# ends the program
def exit():
    global is_alive
    is_alive = False

# takes a screenshot of the prompt and returns the letters
def read():
    ss = pyautogui.screenshot(region=(760, 730, 100, 40))
    #s = pyautogui.screenshot(region=(760, 430, 100, 40))
    ss.save(sspath)
    ss = cv2.imread(sspath)
    monochromess = cv2.cvtColor(ss, cv2.COLOR_BGR2GRAY)
    darkerss = cv2.convertScaleAbs(monochromess, 1.5, 10)
    return pytesseract.image_to_string(darkerss, config='--psm 10')

# returns a word from the wordlist with the prompt in it, then removes the word from the list
def solve():
    prompt = read().strip().lower()
    print(prompt)
    for i in wordlist:
        if prompt in i:
            wordlist.remove(i)
            return(i)
        else:
            pass

# types the word
def type():
    keyboard.press('backspace')
    try:
       keyboard.write(solve(), delay=0.05)
    except TypeError:
       print('no words found')

bindings = [
    [solvehotkey, None, type, True],
    [exithotkey, None, exit, True]
]

register_hotkeys(bindings)

start_checking_hotkeys()

while is_alive:
    time.sleep(0.1)