import win32api
import win32gui
import win32con
from win32con import KEYEVENTF_KEYUP
import win32ui
import pywintypes
from selenium import webdriver
import time


# driver = webdriver.Chrome("C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe")
# driver.get('http://www.baidu.com')
# print(win32gui.FindWindow(driver, None))
# time.sleep(1)
# title = driver.title
# print(win32ui.GetActiveWindow())
win32api.keybd_event(18,0,0,0)
time.sleep(0.5)
win32api.keybd_event(9,0,0,0)
time.sleep(0.5)
win32api.keybd_event(9,0,KEYEVENTF_KEYUP,0)
time.sleep(0.5)
win32api.keybd_event(18,0,KEYEVENTF_KEYUP,0)
time.sleep(0.5)
print(win32gui.FindWindow("Notepad", None) )
print(win32api.GetSystemTime())
# print(win32gui.IsWindow(win32ui.GetForegroundWindow()))