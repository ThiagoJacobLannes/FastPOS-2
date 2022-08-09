import os
import time
import pyautogui
import keyboard
import paths
import win32gui
import win32clipboard
from tkinter import *
import tkinter.font as font

window_handle = 0
window_wanted = window_handle

def paste(entry):
    
    keyboard_location = pyautogui.locateOnScreen(paths.keyboard) #obtém localização do keyboard

    for number in entry:   # for each character, do action
        if number == "0":
            click_position = pyautogui.locateCenterOnScreen(paths.key0, region = keyboard_location, confidence=0.9)
            pyautogui.click(click_position)
        if number == "1":
            click_position = pyautogui.locateCenterOnScreen(paths.key1, region = keyboard_location, confidence=0.9)
            pyautogui.click(click_position)
        if number == "2":
            click_position = pyautogui.locateCenterOnScreen(paths.key2, region = keyboard_location, confidence=0.9)
            pyautogui.click(click_position)
        if number == "3":
            click_position = pyautogui.locateCenterOnScreen(paths.key3, region = keyboard_location, confidence=0.9)
            pyautogui.click(click_position)
        if number == "4":
            click_position = pyautogui.locateCenterOnScreen(paths.key4, region = keyboard_location, confidence=0.9)
            pyautogui.click(click_position)
        if number == "5":
            click_position = pyautogui.locateCenterOnScreen(paths.key5, region = keyboard_location, confidence=0.9)
            pyautogui.click(click_position)
        if number == "6":
            click_position = pyautogui.locateCenterOnScreen(paths.key6, region = keyboard_location, confidence=0.9)
            pyautogui.click(click_position)
        if number == "7":
            click_position = pyautogui.locateCenterOnScreen(paths.key7, region = keyboard_location, confidence=0.9)
            pyautogui.click(click_position)
        if number == "8":
            click_position = pyautogui.locateCenterOnScreen(paths.key8, region = keyboard_location, confidence=0.9)
            pyautogui.click(click_position)
        if number == "9":
            click_position = pyautogui.locateCenterOnScreen(paths.key9, region = keyboard_location, confidence=0.9)
            pyautogui.click(click_position)
        """else:
            click_position = pyautogui.locateCenterOnScreen(paths.Entra, region = keyboard_location)
            pyautogui.click(click_position)"""

while True:
    
    keyboard_location = pyautogui.locateOnScreen(paths.keyboard) #obtém localização do keyboard

    if keyboard.is_pressed("ctrl+r"):
        window_handle = win32gui.GetForegroundWindow()
        #win32gui.MoveWindow(window_handle, 0, 0, 1386, 600, True)
        window_wanted = window_handle
    
    # Digitação automatizada
    if window_wanted == win32gui.GetForegroundWindow():
        if keyboard.is_pressed("ctrl + v"):
            root = Tk()
            root.geometry("180x40")
            root.title(" ")
            root.iconbitmap("c:/users/" + os.getlogin() + "/Desktop/FastPOS/resources/icon/iconscript.ico")
            root.attributes("-topmost",1) # Open above everything
            
            Code_Entry = Entry(root)
            win32clipboard.OpenClipboard()
            Clipboard = win32clipboard.GetClipboardData()
            Code_Entry.insert(END, Clipboard)
            Code_Entry.place(x=8, y=8, width=120, height=22)

            if keyboard.is_pressed("Enter"):
                Okay()

            def Okay():
                entry = Code_Entry.get()
                paste(entry)
                root.destroy()

            button = Button(root, text= "OK", command=Okay)
            FontSize = font.Font(size=8)
            button['font'] = FontSize
            button.place(x=133, y=8, width=40, height=22)

            root.mainloop()
        
        # Digitação manual no teclado
        if keyboard.is_pressed("0") and pyautogui.locateOnScreen(paths.key0, region = keyboard_location) is not None:
            click_position = pyautogui.locateCenterOnScreen(paths.key0, region = keyboard_location, confidence=0.9)
            pyautogui.click(click_position)

        if keyboard.is_pressed("1") and pyautogui.locateOnScreen(paths.key1, region = keyboard_location) is not None:
            click_position = pyautogui.locateCenterOnScreen(paths.key1, region = keyboard_location, confidence=0.9)
            pyautogui.click(click_position)
        
        if keyboard.is_pressed("2") and pyautogui.locateOnScreen(paths.key2, region = keyboard_location) is not None:
            click_position = pyautogui.locateCenterOnScreen(paths.key2, region = keyboard_location, confidence=0.9)
            pyautogui.click(click_position)

        if keyboard.is_pressed("3") and pyautogui.locateOnScreen(paths.key3, region = keyboard_location) is not None:
            click_position = pyautogui.locateCenterOnScreen(paths.key3, region = keyboard_location, confidence=0.9)
            pyautogui.click(click_position)

        if keyboard.is_pressed("4") and pyautogui.locateOnScreen(paths.key4, region = keyboard_location) is not None:
            click_position = pyautogui.locateCenterOnScreen(paths.key4, region = keyboard_location, confidence=0.9)
            pyautogui.click(click_position)

        if keyboard.is_pressed("5") and pyautogui.locateOnScreen(paths.key5, region = keyboard_location) is not None:
            click_position = pyautogui.locateCenterOnScreen(paths.key5, region = keyboard_location, confidence=0.9)
            pyautogui.click(click_position)
            
        if keyboard.is_pressed("6") and pyautogui.locateOnScreen(paths.key6, region = keyboard_location) is not None:
            click_position = pyautogui.locateCenterOnScreen(paths.key6, region = keyboard_location, confidence=0.9)
            pyautogui.click(click_position)

        if keyboard.is_pressed("7") and pyautogui.locateOnScreen(paths.key7, region = keyboard_location) is not None:
            click_position = pyautogui.locateCenterOnScreen(paths.key7, region = keyboard_location, confidence=0.9)
            pyautogui.click(click_position)

        if keyboard.is_pressed("8") and pyautogui.locateOnScreen(paths.key8, region = keyboard_location) is not None:
            click_position = pyautogui.locateCenterOnScreen(paths.key8, region = keyboard_location, confidence=0.9)
            pyautogui.click(click_position)

        if keyboard.is_pressed("9") and pyautogui.locateOnScreen(paths.key9, region = keyboard_location) is not None:
            click_position = pyautogui.locateCenterOnScreen(paths.key9, region = keyboard_location, confidence=0.9)
            pyautogui.click(click_position)

        if keyboard.is_pressed("Enter") and pyautogui.locateOnScreen(paths.Entra, region = keyboard_location) is not None:
            click_position = pyautogui.locateCenterOnScreen(paths.Entra, region = keyboard_location, confidence=0.9)
            pyautogui.click(click_position)
    
    """         click direto no teclado
    if keyboard.is_pressed("1") and pyautogui.locateOnScreen(paths.key1, region = keyboard_location) is not None:
        click_position = pyautogui.center(pyautogui.locateOnScreen(paths.key1, region = keyboard_location))
        pyautogui.click(click_position)
    
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
        pyautogui.click(paths.Entra)"""
