"""
TO-DO::
use imagegrab to get a picture --> use tesseract to get the text from the picture --> use pyautogui to enter characters --> win?
"""

from PIL import ImageGrab
from random import randint, uniform
from time import sleep
import pytesseract
import keyboard as kb
import pyautogui as pya

pytesseract.pytesseract.tesseract_cmd = r'/usr/local/bin/tesseract'

alph="abcdefghijklmnopqrstuvwxyz ,.-':"
global var
sleep(5)

def inputListener(key):
    temp_coords = []
    while len(temp_coords) != 4:
        if kb.is_pressed(key):
            print(temp_coords)
            x = pya.position()[0]
            y = pya.position()[1]
            temp_coords.extend(x*2, y*2)
    if len(temp_coords) == 4:
        temp_coords = tuple(temp_coords)
        print(f"got coordinates at {temp_coords}.")
        var = temp_coords
        
    

def typeText():
    while True:
        im = ImageGrab.grab(var)
        txt_data = pytesseract.image_to_string(im)
        for letter in txt_data:
            try:  
                if letter in alph or letter.lower() in alph:
                    if letter.isupper():
                        pya.keyDown("shift")
                        pya.press(letter)
                        pya.keyUp("shift")
                    else: pya.press(letter)
            except: pass
            sleep(uniform(0, 0.05))


def main():
    inputListener("space")
    typeText()




if __name__ == "__main__":
    main()
