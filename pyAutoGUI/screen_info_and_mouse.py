import pyautogui


def get_screen_size():
    return pyautogui.size()


def get_screen_in_dict():
    width, height = pyautogui.size()
    return {'width': width, 'height': height}


def mouse_position():
    return pyautogui.position()


def move_mouse_abs(x, y, time=0):
    # move the mouse to an absolute position on the screen
    dim = get_screen_in_dict()
    if x > dim['width'] or y > dim['height']:
        print('You are trying to move the mouse out of the screen.')
        return
    try:
        pyautogui.moveTo(x, y, duration=time)
    except pyautogui.FailSafeException:
        print('PyAutoGUI fail-safe triggered from mouse moving to a corner of the screen.')
    print('Mouse moved to ({}; {})'.format(x, y))


def move_mouse_rel(x, y, time=0):
    pyautogui.moveRel(x, y, duration=time)


def mouse_single_click(x, y):
    pyautogui.click(x, y)


if __name__ == '__main__':
    print(get_screen_size())
    print(get_screen_in_dict())
    print(mouse_position())
    move_mouse_abs(50, 50, 3)
    move_mouse_rel(100, 200, 3)
    mouse_single_click(538, 52)
