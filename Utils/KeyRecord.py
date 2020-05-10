from keyboard import *
from conf import *

def catchRegisteredKeys():
    """
        Catch only one key press/not press action
    """
    if is_pressed('w'):
        # print('forward')
        return FORWARD
    elif is_pressed('a'):
        # print('left')
        return LEFT
    elif is_pressed('s'):
        # print('slow')
        return SLOW
    elif is_pressed('d'):
        # print('right')
        return RIGHT
    else:
        # print("no action")
        return NO_ACTION