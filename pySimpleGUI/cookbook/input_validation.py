"""
Restrict the characters allowed in an input element to digits and . or -
Accomplished by removing last character input if not a valid character.

This code only allows entry of the correct characters. Note that this example does not fully validate that the entry
is a valid floating point number, but rather that it has the correct characters. If you wanted to take it a step
further and verify that the entry is actually a valid floating point number, then you can change the "if" statement
to test for valid floating point number.
"""
import PySimpleGUI as simpleGUI


def validation():
    layout = [[simpleGUI.Text('Input only floating point numbers')],
              [simpleGUI.Input(key='-IN-', enable_events=True)],
              [simpleGUI.Button('Exit')]]

    window = simpleGUI.Window('Floating point input validation', layout)

    while True:
        event, values = window.read()
        if event in (simpleGUI.WIN_CLOSED, 'Exit'):
            break
        # if last character in input element is invalid, remove it
        if event == '-IN-' and values['-IN-'] and values['-IN-'][-1] not in '0123456789.-':
            window['-IN-'].update(values['-IN-'][:-1])
    simpleGUI.popup(f"Your float is {values['-IN-']}")
    window.close()


def complete_validation():
    layout = [[simpleGUI.Text('Input only floating point numbers')],
              [simpleGUI.Input(key='-IN-', enable_events=True)],
              [simpleGUI.Button('Exit')]]

    window = simpleGUI.Window('Floating point input validation', layout)

    while True:
        event, values = window.read()
        if event in (simpleGUI.WIN_CLOSED, 'Exit'):
            break
        # if last character in input element is invalid, remove it
        if event == '-IN-' and values['-IN-']:
            try:
                in_as_float = float(values['-IN-'])
            except ValueError:
                if len(values['-IN-']) == 1 and values['-IN-'][0] == '-':
                    continue
                window['-IN-'].update(values['-IN-'][:-1])
    simpleGUI.popup(f"Your float is {values['-IN-']}")
    window.close()


if __name__ == '__main__':
    validation()
    complete_validation()
