import PySimpleGUI as simpleGUI

from pySimpleGUI.cookbook.themes import select_random_theme, DEFAULT_THEME

'''
https://pysimplegui.readthedocs.io/en/latest/cookbook/#recipe-pattern-2a-persistent-window-multiple-reads-using-an-event-loop
Recipe - Pattern 2A - Persistent window (multiple reads using an event loop)

The more advanced/typical GUI programs operate with the window remaining visible on the screen. Input values are 
collected, but rather than closing the window, it is kept visible acting as a way to both input and output 
information. This code will present a window and will print values until the user clicks the exit button or closes 
window using an X. The first thing printed is the "event" which in this program is the buttons. The next thing 
printed is the values variable that holds the dictionary of return values from the read. This dictionary has only 1 
entry. The event returned from the read is set to None (the variable WIN_CLOSED) and so are the input fields in the 
window. This None event is super-important to check for. It must be detected in your windows or else you'll be trying 
to work with a window that's been destroyed and your code will crash. This is why you will find this check after 
every window.read() call you'll find in sample PySimpleGUI code. 

In some circumstances when a window is closed with an X, both of the return values from window.read() will be None. 
This is why it's important to check for event is None before attempting to access anything in the values variable.
'''


def persistent_win(my_theme=DEFAULT_THEME):
    simpleGUI.theme(my_theme)
    layout = [
        [simpleGUI.T('Persist win:')],
        # The "key" for the entry is '-IN-' and matches the key passed into the Input element creation.
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
