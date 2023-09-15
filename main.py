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

old_window_rect_pos = ""
x0, y0, x1, y1 = "", "", "", ""

def main_fn():
    global old_pos
    global new_pos
    global old_window_rect_pos
    global x0, y0, x1, y1

    flag = False

    while 1:
        # Mouse and client coordinates
        new_pos = pyautogui.position()
        x0, y0, x1, y1 = GetWindowRect(window_handle)

        if old_pos != new_pos:
            sys.stdout.write("\r" + f"x0={str(x0)} y0={str(x1)} x1={str(y0)} y1={str(y1)} {str(new_pos)}")
            sys.stdout.flush()

        old_pos = new_pos

        if old_window_rect_pos != (x0, y0, x1, y1):
            sys.stdout.write("\r" + f"x0={str(x0)} y0={str(x1)} x1={str(y0)} y1={str(y1)} {str(new_pos)}")
            sys.stdout.flush()

        old_window_rect_pos = x0, y0, x1, y1

        # Casting spells
        if flag == False:
            # Spell book
            pyautogui.moveTo(x1 - 25, y0 + 205, 1)
            pyautogui.click()
            # High alch spell
            pyautogui.moveTo(x1 - 55, y0 + 335, 1)
            pyautogui.click()
            # Alch item
            pyautogui.click()

            flag = True


main_fn()