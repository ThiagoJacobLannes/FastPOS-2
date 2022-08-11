import os
import time
import pyautogui
import keyboard
import win32gui
import win32clipboard
from tkinter import *
import tkinter.font as font

import paths

window_handle = 0
window_wanted = window_handle

def login():
    settings_path = "c:/users/" + os.getlogin() + "/Desktop/FastPOS/settings.txt"
    try:
        with open(settings_path) as f:
            read = f.readlines()
            read = ' '.join(read)
            credenciais = read.split()
            user = credenciais[0]
            password = credenciais[1]

            paste(user)
            paste(password)

    except FileNotFoundError:
        print("O documento não existe")

def paste(entry):
    
    keyboard_location = pyautogui.locateOnScreen(paths.keyboard) #obtém localização do keyboard

    for number in entry:   # for each character, do action
        if number == "0":
            if pyautogui.locateOnScreen(paths.key0, region = keyboard_location, confidence=0.8) is not None:
                click_position = pyautogui.locateCenterOnScreen(paths.key0, region = keyboard_location, confidence=0.9)
                pyautogui.click(click_position)
        elif number == "1":
            if pyautogui.locateOnScreen(paths.key1, region = keyboard_location, confidence=0.8) is not None:
                click_position = pyautogui.locateCenterOnScreen(paths.key1, region = keyboard_location, confidence=0.9)
                pyautogui.click(click_position)
        elif number == "2":
            if pyautogui.locateOnScreen(paths.key2, region = keyboard_location, confidence=0.8) is not None:
                click_position = pyautogui.locateCenterOnScreen(paths.key2, region = keyboard_location, confidence=0.9)
                pyautogui.click(click_position)
        elif number == "3":
            if pyautogui.locateOnScreen(paths.key3, region = keyboard_location, confidence=0.8) is not None:
                click_position = pyautogui.locateCenterOnScreen(paths.key3, region = keyboard_location, confidence=0.9)
                pyautogui.click(click_position)
        elif number == "4":
            if pyautogui.locateOnScreen(paths.key4, region = keyboard_location, confidence=0.8) is not None:
                click_position = pyautogui.locateCenterOnScreen(paths.key4, region = keyboard_location, confidence=0.9)
                pyautogui.click(click_position)
        elif number == "5":
            if pyautogui.locateOnScreen(paths.key5, region = keyboard_location, confidence=0.8) is not None:
                click_position = pyautogui.locateCenterOnScreen(paths.key5, region = keyboard_location, confidence=0.9)
                pyautogui.click(click_position)
        elif number == "6":
            if pyautogui.locateOnScreen(paths.key6, region = keyboard_location, confidence=0.8) is not None:
                click_position = pyautogui.locateCenterOnScreen(paths.key6, region = keyboard_location, confidence=0.9)
                pyautogui.click(click_position)
        elif number == "7":
            if pyautogui.locateOnScreen(paths.key7, region = keyboard_location, confidence=0.8) is not None:
                click_position = pyautogui.locateCenterOnScreen(paths.key7, region = keyboard_location, confidence=0.9)
                pyautogui.click(click_position)
        elif number == "8":
            if pyautogui.locateOnScreen(paths.key8, region = keyboard_location, confidence=0.8) is not None:
                click_position = pyautogui.locateCenterOnScreen(paths.key8, region = keyboard_location, confidence=0.9)
                pyautogui.click(click_position)
        elif number == "9":
            if pyautogui.locateOnScreen(paths.key9, region = keyboard_location, confidence=0.8) is not None:
                click_position = pyautogui.locateCenterOnScreen(paths.key9, region = keyboard_location, confidence=0.9)
                pyautogui.click(click_position)

    if pyautogui.locateOnScreen(paths.Entra, region = keyboard_location, confidence=0.8) is not None:
        click_position = pyautogui.locateCenterOnScreen(paths.Entra, region = keyboard_location, confidence=0.5)
        pyautogui.click(click_position)

def keyboardinput(key_pressed):

    keyboard_location = pyautogui.locateOnScreen(paths.keyboard) #obtém localização do keyboard
    keyboard_bdc_location = pyautogui.locateOnScreen(paths.keyboard_bdc) #obtém localização do keyboard BDC

    if key_pressed in paths.keys_list_main and pyautogui.locateOnScreen(paths.keyboard) is not None:
        if pyautogui.locateOnScreen(paths.keyboard) is not None:
            path = paths.initial_path + key_pressed + ".png"
            print(path)
            if pyautogui.locateOnScreen(path, region = keyboard_location, confidence=0.8) is not None:
                click_position = pyautogui.locateCenterOnScreen(path, region = keyboard_location)
                pyautogui.click(click_position)
    if key_pressed in paths.keys_list_bdc and pyautogui.locateOnScreen(paths.keyboard_bdc) is not None:
        if pyautogui.locateOnScreen(paths.keyboard_bdc) is not None:
            path = paths.initial_path + key_pressed + "_bdc.png"
            if pyautogui.locateOnScreen(path, region = keyboard_bdc_location, confidence=0.8) is not None:
                click_position = pyautogui.locateCenterOnScreen(path, region = keyboard_bdc_location)
                pyautogui.click(click_position)

while True:

    # Obtenção de janela
    if keyboard.is_pressed("ctrl+r"):
        window_handle = win32gui.GetForegroundWindow()
        #win32gui.MoveWindow(window_handle, 0, 0, 1386, 600, True)
        window_wanted = window_handle

    # Entrada de operador automatizada
    if keyboard.is_pressed("ctrl+1"):
        login()
    
    # Digitações no teclado
    if window_wanted == win32gui.GetForegroundWindow():
        # Digitação automatizada
        if keyboard.is_pressed("ctrl + v"):
            root = Tk()
            root.geometry("180x40")
            root.title(" ")
            root.iconbitmap("c:/users/" + os.getlogin() + "/Desktop/FastPOS/resources/icon/iconscript.ico")
            root.attributes("-topmost",1) # Open above everything
            
            Code_Entry = Entry(root)
            try:
                win32clipboard.OpenClipboard()
                Clipboard = win32clipboard.GetClipboardData()
                Clipboard = Clipboard[:30]
                win32clipboard.CloseClipboard()
            except TypeError:
                Clipboard = ""
            Code_Entry.insert(END, Clipboard)
            Code_Entry.place(x=8, y=8, width=120, height=22)

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

        # Através de Função
        tecla = keyboard.read_key()
        keyboardinput(tecla)

        # Através de condições
        """if keyboard.is_pressed("0"):
            if pyautogui.locateOnScreen(paths.key0, region = keyboard_location, confidence=0.8) is not None:
                click_position = pyautogui.locateCenterOnScreen(paths.key0, region = keyboard_location, confidence=0.9)
                pyautogui.click(click_position)
            if pyautogui.locateOnScreen(paths.bdc_0, region = keyboard_bdc_location, confidence=0.8) is not None:
                click_position = pyautogui.locateCenterOnScreen(paths.bdc_0, region = keyboard_bdc_location, confidence=0.9)
                pyautogui.click(click_position)

        if keyboard.is_pressed("1"):
            if pyautogui.locateOnScreen(paths.key1, region = keyboard_location, confidence=0.8) is not None:
                click_position = pyautogui.locateCenterOnScreen(paths.key1, region = keyboard_location)
                pyautogui.click(click_position)
            if pyautogui.locateOnScreen(paths.bdc_1, region = keyboard_bdc_location, confidence=0.8) is not None:
                click_position = pyautogui.locateCenterOnScreen(paths.bdc_1, region = keyboard_bdc_location)
                pyautogui.click(click_position)
        
        if keyboard.is_pressed("2"):
            if pyautogui.locateOnScreen(paths.key2, region = keyboard_location, confidence=0.8) is not None:
                click_position = pyautogui.locateCenterOnScreen(paths.key2, region = keyboard_location)
                pyautogui.click(click_position)
            if pyautogui.locateOnScreen(paths.bdc_2, region = keyboard_bdc_location, confidence=0.8) is not None:
                click_position = pyautogui.locateCenterOnScreen(paths.bdc_2, region = keyboard_bdc_location)
                pyautogui.click(click_position)

        if keyboard.is_pressed("3"):
            if pyautogui.locateOnScreen(paths.key3, region = keyboard_location, confidence=0.8) is not None:
                click_position = pyautogui.locateCenterOnScreen(paths.key3, region = keyboard_location)
                pyautogui.click(click_position)
            if pyautogui.locateOnScreen(paths.bdc_3, region = keyboard_bdc_location, confidence=0.8) is not None:
                click_position = pyautogui.locateCenterOnScreen(paths.bdc_3, region = keyboard_bdc_location)
                pyautogui.click(click_position)

        if keyboard.is_pressed("4"):
            if pyautogui.locateOnScreen(paths.key4, region = keyboard_location, confidence=0.8) is not None:
                click_position = pyautogui.locateCenterOnScreen(paths.key4, region = keyboard_location)
                pyautogui.click(click_position)
            if pyautogui.locateOnScreen(paths.bdc_4, region = keyboard_bdc_location, confidence=0.8) is not None:
                click_position = pyautogui.locateCenterOnScreen(paths.bdc_4, region = keyboard_bdc_location)
                pyautogui.click(click_position)

        if keyboard.is_pressed("5"):
            if pyautogui.locateOnScreen(paths.key5, region = keyboard_location, confidence=0.8) is not None:
                click_position = pyautogui.locateCenterOnScreen(paths.key5, region = keyboard_location)
                pyautogui.click(click_position)
            if pyautogui.locateOnScreen(paths.bdc_5, region = keyboard_bdc_location, confidence=0.8) is not None:
                click_position = pyautogui.locateCenterOnScreen(paths.bdc_5, region = keyboard_bdc_location)
                pyautogui.click(click_position)
            
        if keyboard.is_pressed("6"):
            if pyautogui.locateOnScreen(paths.key6, region = keyboard_location, confidence=0.8) is not None:
                click_position = pyautogui.locateCenterOnScreen(paths.key6, region = keyboard_location)
                pyautogui.click(click_position)
            if pyautogui.locateOnScreen(paths.bdc_6, region = keyboard_bdc_location, confidence=0.8) is not None:
                click_position = pyautogui.locateCenterOnScreen(paths.bdc_6, region = keyboard_bdc_location)
                pyautogui.click(click_position)

        if keyboard.is_pressed("7"):
            if pyautogui.locateOnScreen(paths.key7, region = keyboard_location, confidence=0.8) is not None:
                click_position = pyautogui.locateCenterOnScreen(paths.key7, region = keyboard_location)
                pyautogui.click(click_position)
            if pyautogui.locateOnScreen(paths.bdc_7, region = keyboard_bdc_location, confidence=0.8) is not None:
                click_position = pyautogui.locateCenterOnScreen(paths.bdc_7, region = keyboard_bdc_location)
                pyautogui.click(click_position)

        if keyboard.is_pressed("8"): 
            if pyautogui.locateOnScreen(paths.key8, region = keyboard_location, confidence=0.8) is not None:
                click_position = pyautogui.locateCenterOnScreen(paths.key8, region = keyboard_location)
                pyautogui.click(click_position)
            if pyautogui.locateOnScreen(paths.bdc_8, region = keyboard_bdc_location, confidence=0.8) is not None:
                click_position = pyautogui.locateCenterOnScreen(paths.bdc_8, region = keyboard_bdc_location)
                pyautogui.click(click_position)

        if keyboard.is_pressed("9"):
            if pyautogui.locateOnScreen(paths.key9, region = keyboard_location, confidence=0.8) is not None:
                click_position = pyautogui.locateCenterOnScreen(paths.key9, region = keyboard_location)
                pyautogui.click(click_position)
            if pyautogui.locateOnScreen(paths.bdc_9, region = keyboard_bdc_location, confidence=0.8) is not None:
                click_position = pyautogui.locateCenterOnScreen(paths.bdc_9, region = keyboard_bdc_location)
                pyautogui.click(click_position)

        if keyboard.is_pressed("Enter") and pyautogui.locateOnScreen(paths.Entra, region = keyboard_location, confidence=0.8) is not None:
            click_position = pyautogui.locateCenterOnScreen(paths.Entra, region = keyboard_location, confidence=0.7)
            pyautogui.click(click_position)

        if keyboard.is_pressed("Backspace"):
            if pyautogui.locateOnScreen(paths.Limpa, region = keyboard_location, confidence=0.8) is not None:
                click_position = pyautogui.locateCenterOnScreen(paths.Limpa, region = keyboard_location)
                pyautogui.click(click_position)
            if pyautogui.locateOnScreen(paths.Limpa_bdc, region = keyboard_bdc_location, confidence=0.8) is not None:
                click_position = pyautogui.locateCenterOnScreen(paths.Limpa_bdc, region = keyboard_bdc_location)
                pyautogui.click(click_position)

        if keyboard.is_pressed("x"):
            if pyautogui.locateOnScreen(paths.X, region = keyboard_location, confidence=0.8) is not None:
                click_position = pyautogui.locateCenterOnScreen(paths.X, region = keyboard_location)
                pyautogui.click(click_position)
            if pyautogui.locateOnScreen(paths.x_bdc, region = keyboard_bdc_location, confidence=0.8) is not None:
                click_position = pyautogui.locateCenterOnScreen(paths.x_bdc, region = keyboard_bdc_location)
                pyautogui.click(click_position)

        if keyboard.is_pressed("Tab"):
            if pyautogui.locateOnScreen(paths.Anula, region = keyboard_location, confidence=0.8) is not None:
                click_position = pyautogui.locateCenterOnScreen(paths.Anula, region = keyboard_location)
                pyautogui.click(click_position)
            if pyautogui.locateOnScreen(paths.Anula_bdc, region = keyboard_bdc_location, confidence=0.8) is not None:
                click_position = pyautogui.locateCenterOnScreen(paths.Anula_bdc, region = keyboard_bdc_location)
                pyautogui.click(click_position)
    
        # Digitação manual exclusivo BDC
        if keyboard.is_pressed("q"):
            if pyautogui.locateOnScreen(paths.q_bdc, region = keyboard_bdc_location, confidence=0.8) is not None:
                click_position = pyautogui.locateCenterOnScreen(paths.q_bdc, region = keyboard_bdc_location, confidence=0.9)
                pyautogui.click(click_position)
        if keyboard.is_pressed("w"):
            if pyautogui.locateOnScreen(paths.w_bdc, region = keyboard_bdc_location, confidence=0.8) is not None:
                click_position = pyautogui.locateCenterOnScreen(paths.w_bdc, region = keyboard_bdc_location, confidence=0.9)
                pyautogui.click(click_position)
        if keyboard.is_pressed("e"):
            if pyautogui.locateOnScreen(paths.e_bdc, region = keyboard_bdc_location, confidence=0.8) is not None:
                click_position = pyautogui.locateCenterOnScreen(paths.e_bdc, region = keyboard_bdc_location, confidence=0.9)
                pyautogui.click(click_position)
        if keyboard.is_pressed("r"):
            if pyautogui.locateOnScreen(paths.r_bdc, region = keyboard_bdc_location, confidence=0.8) is not None:
                click_position = pyautogui.locateCenterOnScreen(paths.r_bdc, region = keyboard_bdc_location, confidence=0.9)
                pyautogui.click(click_position)
        if keyboard.is_pressed("t"):
            if pyautogui.locateOnScreen(paths.t_bdc, region = keyboard_bdc_location, confidence=0.8) is not None:
                click_position = pyautogui.locateCenterOnScreen(paths.t_bdc, region = keyboard_bdc_location, confidence=0.9)
                pyautogui.click(click_position)
        if keyboard.is_pressed("y"):
            if pyautogui.locateOnScreen(paths.y_bdc, region = keyboard_bdc_location, confidence=0.8) is not None:
                click_position = pyautogui.locateCenterOnScreen(paths.y_bdc, region = keyboard_bdc_location, confidence=0.9)
                pyautogui.click(click_position)
        if keyboard.is_pressed("u"):
            if pyautogui.locateOnScreen(paths.u_bdc, region = keyboard_bdc_location, confidence=0.8) is not None:
                click_position = pyautogui.locateCenterOnScreen(paths.u_bdc, region = keyboard_bdc_location, confidence=0.9)
                pyautogui.click(click_position)
        if keyboard.is_pressed("i"):
            if pyautogui.locateOnScreen(paths.i_bdc, region = keyboard_bdc_location, confidence=0.8) is not None:
                click_position = pyautogui.locateCenterOnScreen(paths.i_bdc, region = keyboard_bdc_location, confidence=0.9)
                pyautogui.click(click_position)
        if keyboard.is_pressed("o"):
            if pyautogui.locateOnScreen(paths.o_bdc, region = keyboard_bdc_location, confidence=0.8) is not None:
                click_position = pyautogui.locateCenterOnScreen(paths.o_bdc, region = keyboard_bdc_location)
                pyautogui.click(click_position)
        if keyboard.is_pressed("p"):
            if pyautogui.locateOnScreen(paths.p_bdc, region = keyboard_bdc_location, confidence=0.8) is not None:
                click_position = pyautogui.locateCenterOnScreen(paths.p_bdc, region = keyboard_bdc_location, confidence=0.9)
                pyautogui.click(click_position)
        if keyboard.is_pressed("a"):
            if pyautogui.locateOnScreen(paths.a_bdc, region = keyboard_bdc_location, confidence=0.8) is not None:
                click_position = pyautogui.locateCenterOnScreen(paths.a_bdc, region = keyboard_bdc_location, confidence=0.9)
                pyautogui.click(click_position)
        if keyboard.is_pressed("s"):
            if pyautogui.locateOnScreen(paths.s_bdc, region = keyboard_bdc_location, confidence=0.8) is not None:
                click_position = pyautogui.locateCenterOnScreen(paths.s_bdc, region = keyboard_bdc_location)
                pyautogui.click(click_position)
        if keyboard.is_pressed("d"):
            if pyautogui.locateOnScreen(paths.d_bdc, region = keyboard_bdc_location, confidence=0.8) is not None:
                click_position = pyautogui.locateCenterOnScreen(paths.d_bdc, region = keyboard_bdc_location, confidence=0.9)
                pyautogui.click(click_position)
        if keyboard.is_pressed("f"):
            if pyautogui.locateOnScreen(paths.f_bdc, region = keyboard_bdc_location, confidence=0.8) is not None:
                click_position = pyautogui.locateCenterOnScreen(paths.f_bdc, region = keyboard_bdc_location, confidence=0.9)
                pyautogui.click(click_position)
        if keyboard.is_pressed("g"):
            if pyautogui.locateOnScreen(paths.g_bdc, region = keyboard_bdc_location, confidence=0.8) is not None:
                click_position = pyautogui.locateCenterOnScreen(paths.g_bdc, region = keyboard_bdc_location, confidence=0.9)
                pyautogui.click(click_position)
        if keyboard.is_pressed("h"):
            if pyautogui.locateOnScreen(paths.h_bdc, region = keyboard_bdc_location, confidence=0.8) is not None:
                click_position = pyautogui.locateCenterOnScreen(paths.h_bdc, region = keyboard_bdc_location, confidence=0.9)
                pyautogui.click(click_position)
        if keyboard.is_pressed("j"):
            if pyautogui.locateOnScreen(paths.j_bdc, region = keyboard_bdc_location, confidence=0.8) is not None:
                click_position = pyautogui.locateCenterOnScreen(paths.j_bdc, region = keyboard_bdc_location, confidence=0.9)
                pyautogui.click(click_position)
        if keyboard.is_pressed("k"):
            if pyautogui.locateOnScreen(paths.k_bdc, region = keyboard_bdc_location, confidence=0.8) is not None:
                click_position = pyautogui.locateCenterOnScreen(paths.k_bdc, region = keyboard_bdc_location, confidence=0.9)
                pyautogui.click(click_position)
        if keyboard.is_pressed("l"):
            if pyautogui.locateOnScreen(paths.l_bdc, region = keyboard_bdc_location, confidence=0.8) is not None:
                click_position = pyautogui.locateCenterOnScreen(paths.l_bdc, region = keyboard_bdc_location, confidence=0.9)
                pyautogui.click(click_position)
        if keyboard.is_pressed("z"):
            if pyautogui.locateOnScreen(paths.z_bdc, region = keyboard_bdc_location, confidence=0.8) is not None:
                click_position = pyautogui.locateCenterOnScreen(paths.z_bdc, region = keyboard_bdc_location, confidence=0.9)
                pyautogui.click(click_position)
        if keyboard.is_pressed("c"):
            if pyautogui.locateOnScreen(paths.c_bdc, region = keyboard_bdc_location, confidence=0.8) is not None:
                click_position = pyautogui.locateCenterOnScreen(paths.c_bdc, region = keyboard_bdc_location, confidence=0.9)
                pyautogui.click(click_position)
        if keyboard.is_pressed("v"):
            if pyautogui.locateOnScreen(paths.v_bdc, region = keyboard_bdc_location, confidence=0.8) is not None:
                click_position = pyautogui.locateCenterOnScreen(paths.v_bdc, region = keyboard_bdc_location, confidence=0.9)
                pyautogui.click(click_position)
        if keyboard.is_pressed("b"):
            if pyautogui.locateOnScreen(paths.b_bdc, region = keyboard_bdc_location, confidence=0.8) is not None:
                click_position = pyautogui.locateCenterOnScreen(paths.b_bdc, region = keyboard_bdc_location, confidence=0.9)
                pyautogui.click(click_position)
        if keyboard.is_pressed("c"):
            if pyautogui.locateOnScreen(paths.c_bdc, region = keyboard_bdc_location, confidence=0.8) is not None:
                click_position = pyautogui.locateCenterOnScreen(paths.c_bdc, region = keyboard_bdc_location, confidence=0.9)
                pyautogui.click(click_position)
        if keyboard.is_pressed("v"):
            if pyautogui.locateOnScreen(paths.v_bdc, region = keyboard_bdc_location, confidence=0.8) is not None:
                click_position = pyautogui.locateCenterOnScreen(paths.v_bdc, region = keyboard_bdc_location, confidence=0.9)
                pyautogui.click(click_position)
        if keyboard.is_pressed("b"):
            if pyautogui.locateOnScreen(paths.b_bdc, region = keyboard_bdc_location, confidence=0.8) is not None:
                click_position = pyautogui.locateCenterOnScreen(paths.b_bdc, region = keyboard_bdc_location, confidence=0.9)
                pyautogui.click(click_position)
        if keyboard.is_pressed("n"):
            if pyautogui.locateOnScreen(paths.n_bdc, region = keyboard_bdc_location, confidence=0.8) is not None:
                click_position = pyautogui.locateCenterOnScreen(paths.n_bdc, region = keyboard_bdc_location, confidence=0.9)
                pyautogui.click(click_position)
        if keyboard.is_pressed("m"):
            if pyautogui.locateOnScreen(paths.m_bdc, region = keyboard_bdc_location, confidence=0.8) is not None:
                click_position = pyautogui.locateCenterOnScreen(paths.m_bdc, region = keyboard_bdc_location, confidence=0.9)
                pyautogui.click(click_position)

        # Teclas principais BDC
        if keyboard.is_pressed("Space"):
            if pyautogui.locateOnScreen(paths.espaco_bdc, region = keyboard_bdc_location, confidence=0.8) is not None:
                click_position = pyautogui.locateCenterOnScreen(paths.espaco_bdc, region = keyboard_bdc_location, confidence=0.9)
                pyautogui.click(click_position)"""