import PySimpleGUI as simpleGUI

'''
https://pysimplegui.readthedocs.io/en/latest/cookbook/#recipe-pattern-1a-one-shot-window-the-simplest-pattern
Recipe - Pattern 1A - "One-shot Window" - (The Simplest Pattern)

The One-shot window is one that pops up, collects some data, and then disappears. It is more or less a 'form' meant to
quickly grab some information and then be closed.

The window is read and then closed. When you "read" a window, you are returned a tuple consisting of an 'event' and a
dictionary of 'values'. The 'event' is what caused the read to return. It could be a button press, some text clicked,
a list item chosen, etc, or 'WIN_CLOSED' if the user closes the window using the X. The 'values' is a dictionary of
values of all the input-style elements. Dictionaries use keys to define entries. If your elements do not specificy a
key, one is provided for you. These auto-numbered keys are ints starting at zero. This design pattern does not
specify a key for the 'InputText' element, so its key will be auto-numbered and is zero in this case. Thus the design
pattern can get the value of whatever was input by referencing 'values[0]'.
'''


def one_shot(my_theme=''):
    layout = [
        [simpleGUI.Text('My one-shot window.')],
        [simpleGUI.InputText()],
        [simpleGUI.Submit(), simpleGUI.Cancel()]
    ]

    window = simpleGUI.Window('One Shot Title', layout)

    event, values = window.read()
    window.close()

    text_input = values[0]
    simpleGUI.popup('You entered', text_input)


'''
If you want to use your own key instead of an auto-generated once.
'''


def one_shot_key():
    layout = [
        [simpleGUI.Text('My one-shot windows whit own key')],
        [simpleGUI.InputText(key='-IN-')],
        [simpleGUI.Submit(), simpleGUI.Cancel()]
    ]
    window = simpleGUI.Window('One Shot Title - key', layout)

    event, values = window.read()
    window.close()

    text_input = values['-IN-']
    simpleGUI.popup('You entered', text_input)


if __name__ == '__main__':
    one_shot()
    one_shot_key()
