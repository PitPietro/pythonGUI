import PySimpleGUI as simpleGUI

from pySimpleGUI.cookbook.themes import select_random_theme, DEFAULT_THEME
'''
https://pysimplegui.readthedocs.io/en/latest/cookbook/#recipe-pattern-1b-one-shot-window-self-closing-single-line
Recipe - Pattern 1B - "One-shot Window" - (Self-closing, single line)

It's possible to create, display, read, and close a window in a single line of code (here is wrote into
 multiple lines to better understand the code).
'''


def b_one_shot(my_theme=DEFAULT_THEME):
    simpleGUI.theme(my_theme)
    event, values = simpleGUI.Window(
        'Login Win',
        [
            [
                simpleGUI.T('Enter your login ID'),
                simpleGUI.In(key='-ID-')],
            [
                simpleGUI.B('OK'),
                simpleGUI.B('Cancel')
            ]
        ]
    ).read(close=True)

    login_id = values['-ID-']
    print(login_id)


if __name__ == '__main__':
    b_one_shot(select_random_theme())
