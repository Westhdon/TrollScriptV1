import time
import pyautogui
import webbrowser
import random
import pyttsx3
import ctypes
import winsound
import tkinter as tk
root = tk.Tk()

variables = {}

def move_mouse_random():
    pyautogui.dragTo(random, random)
    pass

def open_browser(url):
    webbrowser.open(url)

def message(textformb, titleformb):
    pyautogui.alert(textformb, titleformb)

def sleep(timedsleepseconds):
    try:
        seconds = float(timedsleepseconds)  # convert string to number
        time.sleep(seconds)
    except ValueError:
        print("Use A Number In Sleep Function!")

def flip_mouse():
    x, y = pyautogui.position()
    pyautogui.moveTo(x - 100, y, duration=0.1)

def type_spam(text):
    for _ in range(10):
        pyautogui.write(text)
        pyautogui.press("enter")

import pyttsx3
def say(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

def flash():
    root.attributes('-fullscreen', True)
    root.configure(bg='white')
    root.after(300, lambda: root.destroy())
    root.mainloop()

def fake_error():
    ctypes.windll.user32.MessageBoxW(0, "Your PC ran into a problem", "Windows Error", 0x10)

def jumpscare():
    root.attributes("-fullscreen", True)
    root.configure(bg="red")
    tk.Label(root, text="BOO!", font=("Arial", 100), fg="white", bg="red").pack(expand=True)
    winsound.PlaySound("SystemHand", winsound.SND_ALIAS)
    root.after(1000, root.destroy)
    root.mainloop()

def toggle_caps():
    for _ in range(5):
        ctypes.WinDLL("User32").keybd_event(0x14, 0, 0, 0)
        time.sleep(0.3)
        ctypes.WinDLL("User32").keybd_event(0x14, 0, 2, 0)
        time.sleep(0.3)

def text_explode(text):
    for char in text:
        pyautogui.write(char)
        pyautogui.press("enter")
        time.sleep(0.1)

def error_spam():
    for i in range(5):
        ctypes.windll.user32.MessageBoxW(0, "Something went wrong.", f"Error {i+1}", 0x10)

def errorsound():
    winsound.PlaySound("SystemHand", winsound.SND_ALIAS)