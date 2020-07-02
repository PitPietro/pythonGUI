import PySimpleGUI as simpleGUI

from pySimpleGUI.cookbook.themes import select_random_theme, DEFAULT_THEME

'''
Recipe - Pattern 2A - Persistent window (multiple reads using an event loop)

The more advanced/typical GUI programs operate with the window remaining visible on the screen. Input values are 
collected, but rather than closing the window, it is kept visible acting as a way to both input and output 
information. This code will present a window and will print values until the user clicks the exit button or closes 
window using an X.
'''


def persistent_win(my_theme=DEFAULT_THEME):
    simpleGUI.theme(my_theme)
    layout = [
        [simpleGUI.T('Persist win:')],
        [simpleGUI.I(key='-PIT-')],
        [simpleGUI.B('Read'), simpleGUI.Exit()]
    ]
    win = simpleGUI.Window('Window that stays open', layout)

    while True:
        event, values = win.read()
        print(event, values)
        if event == simpleGUI.WIN_CLOSED or event == 'Exit':
            break

    win.close()


if __name__ == '__main__':
    persistent_win(select_random_theme())
