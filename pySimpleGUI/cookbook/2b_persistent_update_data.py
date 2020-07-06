import PySimpleGUI as simpleGUI

from pySimpleGUI.cookbook.themes import (
    select_random_theme,
    DEFAULT_THEME)

'''
https://pysimplegui.readthedocs.io/en/latest/cookbook/#recipe-pattern-2b-persistent-window-multiple-reads-using-an-event-loop-updates-data-in-window
Recipe - Pattern 2B - Persistent window (multiple reads using an event loop + updates data in window)

This is a slightly more complex, but more realistic version that reads input from the user and displays that input as 
text in the window. Your program is likely to be doing both of those activities so this pattern will likely be your 
starting point.

To modify an Element in a window, you call its update method. This is done in 2 steps. First you lookup the element, 
then you call that element's update method. window['-OUTPUT-'] returns the element that has the key '-OUTPUT-'. Then 
the update method for that element is called so that the value of the Text Element is modified. Be sure you have 
supplied a size that is large enough to display your output. If the size is too small, the output will be truncated. 

If you need to interact with elements prior to calling window.read() you will need to "finalize" your window first 
using the finalize parameter when you create your Window. "Interacting" means calling that element's methods such as 
update, draw_line, etc.
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
