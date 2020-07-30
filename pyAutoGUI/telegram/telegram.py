from time import sleep

import pyautogui
import pyperclip


def open_file(path):
    with open(path, 'r') as my_file:
        text_lines = my_file.readlines()
    return text_lines


def recognize(image_path):
    return pyautogui.locateCenterOnScreen(image_path)


def telegram():
    firefox = recognize('../images/test_1.png')
    pyautogui.click(firefox)
    print(firefox)


def person_img():
    p = recognize('../images/fed_2.png')
    pyautogui.click(p)


def type_link(msg_l):
    for char in msg_l:
        pyperclip.copy(char)
        pyautogui.hotkey('ctrl', 'v', interval=0.01)


if __name__ == '__main__':
    users = open_file('user.txt')
    telegram()
    sleep(1)
    for u in users:
        pyautogui.click(330, 90)
        sleep(1)
        type_link('https://web.telegram.org/')
        pyautogui.press('enter')
        sleep(1)
        pyautogui.doubleClick(1000, 90)
        type_link('im?p=' + u)
        sleep(1)
        pyautogui.press('enter')
        # person_img()
        msg = 'Ciao'
        for i in range(100):
            sleep(0.15)
            type_link(msg)
            sleep(0.15)
            pyautogui.press('enter')
