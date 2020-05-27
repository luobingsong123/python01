import win32
import time
import win32api
import win32con
import win32gui
#
#
# print(win32api.GetCursorPos())#获取并输出鼠标当前坐标
# i = 1
# while i < 3000:
#     win32api.SetCursorPos((425, 72))
#     # print(win32api.GetCursorPos())
#     win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0)
#     win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0, 0, 0)
#     time.sleep(0.1)
#     i += 1


# (423, 74) 下载
# (847, 587) 确认
# win32api.GetCursorPos()#获取鼠标当前坐标
while True:
    win32api.SetCursorPos((425, 72))
    # print(win32api.GetCursorPos())
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0, 0, 0)
    time.sleep(10)
    win32api.SetCursorPos((847, 587))
    # print(win32api.GetCursorPos())
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0, 0, 0)
    time.sleep(10)
