from keyboard import is_pressed
from conf import *

def catchRegisteredKeys():
    if is_pressed('w'):
        print('forward')
        return FORWARD
    if is_pressed('a'):
        print('left')
        return LEFT
    if is_pressed('s'):
        print('slow')
        return SLOW
    if is_pressed('d'):
        print('right')
        return RIGHT