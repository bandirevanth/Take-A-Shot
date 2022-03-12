from tkinter import *
import pyautogui 
import os 

s = pyautogui.screenshot() 
s.save(os.getcwd()+"\screenshot.png")
