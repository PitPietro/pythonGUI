import PySimpleGUI as simpleGUI

from pySimpleGUI.cookbook.themes import select_random_theme, DEFAULT_THEME

'''
https://pysimplegui.readthedocs.io/en/latest/cookbook/#recipe-pattern-2b-persistent-window-multiple-reads-using-an-event-loop-updates-data-in-window
Recipe - Pattern 2B - Persistent window (multiple reads using an event loop + updates data in window)

This is a slightly more complex, but more realistic version that reads input from the user and displays that input as 
text in the window. Your program is likely to be doing both of those activities so this pattern will likely be your 
starting point.
'''


def b_persistent_win(my_theme=DEFAULT_THEME):
    simpleGUI.theme(my_theme)
    layout = [
        [simpleGUI.Text('The typed chars appear here:'),
         simpleGUI.Text(
             size=(15, 1),
             key='-OUTPUT-'
         )],
        [simpleGUI.Input(key='-IN-')],
        [simpleGUI.Button('Show'),
         simpleGUI.Button('Exit')]
    ]

    win = simpleGUI.Window('2B - Update data', layout)

    while True:
        event, values, = win.read()
        print(event, values)
        if event == simpleGUI.WIN_CLOSED or event == 'Exit':
            break
        if event == 'Show':
            win['-OUTPUT-'].update(values['-IN-'])


if __name__ == '__main__':
    b_persistent_win(select_random_theme())
