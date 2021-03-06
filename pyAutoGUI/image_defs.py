import pyautogui as gui
import os
import datetime


def make_screenshot(name=str(datetime.datetime.now()), ext='.png', path=os.getcwd()):
    """
    :param name: file name
    :param ext: file extension
    :param path: decide where to save the image
    """
    file_path = path + '/images/' + name + ext
    print(file_path)
    return gui.screenshot(file_path)


def find_on_screen(file):
    """
    :param file: image
    :return: the x and y coordinate and width and height dimensions of the image on the screen
    """
    return gui.locateOnScreen(file)


def find_on_screen_center(file):
    """
    :param file: image
    :return: the x and y coordinate of the center of the image on the screen
    """
    return gui.locateCenterOnScreen(file)


if __name__ == '__main__':
    print(make_screenshot())
