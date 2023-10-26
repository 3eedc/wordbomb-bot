from global_hotkeys import *
import os, pyautogui, cv2, pytesseract, time, keyboard

cwd = os.getcwd()
sspath = os.path.join(cwd, 'screenshot.png')
wordlist = open(os.path.join(cwd, 'wordlist.txt')).readlines()

is_alive = True
solvehotkey = '1'
exithotkey = '2'

print('press 1 to solve, and press 2 to exit')

while True:
    aboveorbelow = input("is the prompt above or below the bomb\n").lower()
    if aboveorbelow == 'above' or aboveorbelow == 'below':
        break
    else:
        print("you have to say 'above' or 'below'\n")

vertpos = 430 if aboveorbelow == 'above' else 730 # tells the script where the prompt is gonna be (this only works for one screen resolution oops lmfao)

# ends the program
def exit():
    global is_alive
    is_alive = False

# takes a screenshot of the prompt and returns the letters
def read():
    ss = pyautogui.screenshot(region=(760, vertpos, 100, 40)) # THIS CODE IS FOR WHEn THE TEXT IS BELOW THE BOMB
    #ss = pyautogui.screenshot(region=(760, 430, 100, 40)) # THIS CODE IS FOR WHEN THE TEXT IS ABOVE THE BOMB
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