# PyAlcher
# Works only in Fixed - Classic layout

import pyautogui
import sys
import time
import threading
import keyboard
from win32gui import FindWindow, GetWindowRect, GetClassName

window_handle = FindWindow("SunAwtFrame", None)
# GetClassName of a client
# class_name = GetClassName(window_handle)

is_running = True
start_time = time.time()

def stop():
    global is_running
    is_running = False
    end_time = time.time()

    seconds = end_time - start_time
    minutes = seconds // 60
    hours = minutes // 60

    print("\n" + "Terminating the program. Total run time: " + "%02d:%02d:%02d" % (hours, minutes % 60, seconds % 60))

keyboard.add_hotkey("s", stop)

def mouse_and_app_coords():
    old_pos, new_pos = "", ""
    old_window_rect_pos = ""
    x0, y0, x1, y1 = "", "", "", ""

    while not is_running == False:
        # Difference between old_pos and new_pos indicates mouse/client window movement
        # Mouse
        new_pos = pyautogui.position()

        if old_pos != new_pos:
            sys.stdout.write("\r" + f"x1={str(x1)} y0={str(y0)} {str(new_pos)}")
            sys.stdout.flush()

        old_pos = new_pos

        # Client window
        x0, y0, x1, y1 = GetWindowRect(window_handle)

        if old_window_rect_pos != (x0, y0, x1, y1):
            sys.stdout.write("\r" + f"x1={str(x1)} y0={str(y0)} {str(new_pos)}")
            sys.stdout.flush()

        old_window_rect_pos = x0, y0, x1, y1


# Separate thread due to while loop blocking the main thread
mouse_and_app_coords = threading.Thread(target=mouse_and_app_coords)
mouse_and_app_coords.start()

def spell_casting():
    x0, y0, x1, y1 = GetWindowRect(window_handle)
    x, y = "", ""

    while not is_running == False:
        if x != x1 - 55 and y != y0 + 335:
            # Spell book
            pyautogui.moveTo(x1 - 25, y0 + 205, 1)
            time.sleep(0.2)
            pyautogui.click()

            # High alch spell
            pyautogui.moveTo(x1 - 55, y0 + 335, 1)

            # Updates cursor position
            x, y = pyautogui.position()

        if x == x1 - 55 and y0 + 335:
            # High alch spell
            pyautogui.click()
            time.sleep(0.2)

            # Inventory item
            pyautogui.click()
            time.sleep(2.5)


spell_casting()
