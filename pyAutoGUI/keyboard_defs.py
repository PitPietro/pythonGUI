from time import sleep

import pyautogui


def write(text, time):
    """
    :param text: The message to write
    :param time: The seconds between each word
    """
    pyautogui.typewrite(text, interval=time)


def print_all_keys():
    return pyautogui.KEYBOARD_KEYS


def press_single_key(key):
    pyautogui.press(key)


def press_multi_keys(keys):
    pyautogui.hotkey('ctrl', 'shift', 'A')


if __name__ == '__main__':
    print(print_all_keys())
    sleep(4)
    # write(['H', 'y', 'left', 'e', 'right', '!'], 0.2)
    press_multi_keys('fads')
