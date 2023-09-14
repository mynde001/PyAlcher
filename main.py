# PyAlcher
# Works only in Fixed - Classic layout

import pyautogui
import sys

from win32gui import FindWindow, GetWindowRect, GetClassName

old_pos = ""
new_pos = ""

window_handle = FindWindow("SunAwtFrame", None)
# GetClassName of a client
# class_name = GetClassName(window_handle)

old_window_rect = ""
new_window_rect = ""

def main_fn():
    global old_pos
    global new_pos
    global old_window_rect
    global new_window_rect

    while 1:
        new_pos = pyautogui.position()
        new_window_rect = GetWindowRect(window_handle)

        if old_pos != new_pos:
            sys.stdout.write("\r" + f"{str(new_window_rect)} {str(new_pos)}")
            sys.stdout.flush()

        old_pos = new_pos

        if old_window_rect != new_window_rect:
            sys.stdout.write("\r" + f"{str(new_window_rect)} {str(new_pos)}")
            sys.stdout.flush()

        old_window_rect = new_window_rect


main_fn()