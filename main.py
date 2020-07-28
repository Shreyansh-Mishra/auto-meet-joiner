##########################################
#                                        #
#Author: Sarthak Mishra, Shreyansh Mishra#
#                                        #
##########################################

import pyautogui
import datetime
import pause
import time
from autoconnect import autoconnect

current_time = datetime.date.today()
year = current_time.year
month = current_time.month
day = current_time.day
#in 24 hours format
hours = 22
#minutes from 1 to 60
minutes = 31
seconds = 13
#waits till specific time
dt = datetime.datetime(year, month, day, hours, minutes, seconds)
pause.until(dt)
#autoconnect process with the specified link in the function
autoconnect('https://meet.google.com/yaf-untz-smm?pli=1&authuser=1')
#set time for the next class
hours,minutes,seconds=22,33,5
#wait till class is over
dt = datetime.datetime(year, month, day, hours, minutes, seconds)
pause.until(dt)
#close chrome
pyautogui.click(1876,21)
#wait to regain control on pc
time.sleep(3)
#autoconnect process with the specified link in the function
autoconnect('https://meet.google.com/jnr-zmjz-uko?pli=1&authuser=1')
#set time for the next class
hours,minutes,seconds=22,35,3
#wait till class is over
dt = datetime.datetime(year, month, day, hours, minutes, seconds)
pause.until(dt)
#close chrome
pyautogui.click(1876,21)
time.sleep(3)
#autoconnect process with the specified link in the function
autoconnect('https://meet.google.com/edt-kaag-azn?pli=1&authuser=1')
#set time for leaving the class
hours,minutes,seconds=22,37,1
#wait till class is over
dt = datetime.datetime(year, month, day, hours, minutes, seconds)
pause.until(dt)
pyautogui.click(1876,21)
