# PyAlcher
# Works only in Fixed - Classic layout

import pyautogui
import sys
import time
import threading

from win32gui import FindWindow, GetWindowRect, GetClassName

old_pos = ""
new_pos = ""
x, y = "", ""

i = 0

window_handle = FindWindow("SunAwtFrame", None)
# GetClassName of a client
# class_name = GetClassName(window_handle)

old_window_rect_pos = ""
x0, y0, x1, y1 = "", "", "", ""

def mouse_and_app_coords():
    global old_pos, new_pos
    global old_window_rect_pos
    global x0, y0, x1, y1

    while 1:
        new_pos = pyautogui.position()
        x0, y0, x1, y1 = GetWindowRect(window_handle)

        if (old_pos != new_pos):
            sys.stdout.write("\r" + f"x1={str(x1)} y0={str(y0)} {str(new_pos)}")
            sys.stdout.flush()

        old_pos = new_pos

        if old_window_rect_pos != (x0, y0, x1, y1):
            sys.stdout.write("\r" + f"x1={str(x1)} y0={str(y0)} {str(new_pos)}")
            sys.stdout.flush()

        old_window_rect_pos = x0, y0, x1, y1


mouse_and_app_coords = threading.Thread(target=mouse_and_app_coords)
mouse_and_app_coords.start()

def spell_casting():
    global old_pos, new_pos
    global x0, y0, x1, y1
    global x, y
    global i

    x0, y0, x1, y1 = GetWindowRect(window_handle)

    # Casting spells
    while i < 3:
        if (x != x1 - 55 and y != y0 + 335):
            # Spell book
            pyautogui.moveTo(x1 - 25, y0 + 205, 1)
            time.sleep(0.2)
            pyautogui.click()

            # Move mouse to high alch spell
            pyautogui.moveTo(x1 - 55, y0 + 335, 1)

            # Update mouse position
            x, y = pyautogui.position()

        if (x == x1 - 55 and y0 + 335):
            # High alch spell
            pyautogui.click()

            # Alch item
            time.sleep(0.2)
            pyautogui.click()
            time.sleep(2.5)

        i += 1


spell_casting()