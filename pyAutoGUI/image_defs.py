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


if __name__ == '__main__':
    print(make_screenshot())
