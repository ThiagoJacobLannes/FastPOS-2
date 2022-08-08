#from win32gui import FindWindow, FindWindowEx, GetWindowRect
import pyautogui
import keyboard
import paths
"""VNC = FindWindow(None, "VNC Viewer")
print(VNC)
window_handle = FindWindowEx(VNC, 0, None, None)
print(window_handle)
window_rect = GetWindowRect(window_handle)
print(window_rect)"""


def teclar(key):
    pyautogui.click(key)

while True:
    if keyboard.is_pressed("1"):
        teclar(paths.key1)
    if keyboard.is_pressed("2"):
        teclar(paths.key2)
