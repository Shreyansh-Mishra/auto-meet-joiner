import pyautogui
import time

def autoconnect(link):
    #click Chrome on Windows Bar
    pyautogui.click(830,1058)
    #wait for x seconds
    x = 20
    time.sleep(x)
    #Click Search Bar
    pyautogui.click(323,66)
    #Type the class link
    pyautogui.write(link, interval=0.04)
    #Press enter
    pyautogui.hotkey('enter')
    #Wait for x seconds for the page to load
    x = 20
    time.sleep(x)
    #Click Switch Off Video button
    pyautogui.click(719,796)
    #Wait for 2 Seconds before clicking the Other Button
    time.sleep(2)
    #Click Switch Off Microphone button
    pyautogui.click(612,798)
    #Wait for x seconds before clicking join now
    x = 3
    time.sleep(x)
    #click on Join Now button
    pyautogui.click(1348,606)