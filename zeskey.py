
from platform import release
from turtle import onclick
from pynput.keyboard import *
import pygame as pg
import os

os.system("cls")
keyboard = Controller()
print("ZesKey is active. Close terminal to turn off the program.")

pg.mixer.init()
pg.init()
sound=pg.mixer.Sound("press.wav")
pg.mixer.set_num_channels(50)
os.startfile("ZesKeyLoader.exe")
def press_on (key):
    
    sound.play()

  
    
   
    
      
        
   
with Listener(on_press= press_on) as listener:
    listener.join()
