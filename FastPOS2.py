import time
import pyautogui
import keyboard
import paths
import win32gui

window_handle = win32gui.GetForegroundWindow()
window_rect = win32gui.GetWindowRect(window_handle)

def paste():
    print('Hello')



while True:
    if keyboard.is_pressed("ctrl+r"):
        window_handle = win32gui.GetForegroundWindow()
        win32gui.MoveWindow(window_handle, 0, 0, 1386, 600, True)
        time.sleep(.5)
        keyboard_location = pyautogui.locateOnScreen(paths.keyboard) #obtém localização do keyboard
        #print(keyboard_location)
    
    if keyboard.is_pressed("1") and pyautogui.locateOnScreen(paths.key1) is not None:
        pyautogui.click(paths.key1)
    
    if keyboard.is_pressed("2") and pyautogui.locateOnScreen(paths.key2) is not None:
        pyautogui.click(paths.key2)

    if keyboard.is_pressed("3") and pyautogui.locateOnScreen(paths.key3) is not None:
        pyautogui.click(paths.key3)

    if keyboard.is_pressed("4") and pyautogui.locateOnScreen(paths.key4) is not None:
        pyautogui.click(paths.key4)

    if keyboard.is_pressed("5") and pyautogui.locateOnScreen(paths.key5) is not None:
        pyautogui.click(paths.key5)
        
    if keyboard.is_pressed("6") and pyautogui.locateOnScreen(paths.key6) is not None:
        pyautogui.click(paths.key6)

    if keyboard.is_pressed("7") and pyautogui.locateOnScreen(paths.key7) is not None:
        pyautogui.click(paths.key7)

    if keyboard.is_pressed("8") and pyautogui.locateOnScreen(paths.key8) is not None:
        pyautogui.click(paths.key8)

    if keyboard.is_pressed("9") and pyautogui.locateOnScreen(paths.key9) is not None:
        pyautogui.click(paths.key9)

    if keyboard.is_pressed("Enter") and pyautogui.locateOnScreen(paths.Entra) is not None:
        pyautogui.click(paths.Entra)
