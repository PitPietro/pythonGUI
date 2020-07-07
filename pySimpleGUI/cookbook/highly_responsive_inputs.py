"""
Sometimes it's desirable to begin processing input information when a user makes a selection rather than requiring
the user to click an OK button. Let's say you've got a listbox of entries and a user can select an item from it.

> enable_events parameter
Maybe you're impatient and don't want to have to click "Ok". Maybe you don't want an OK
button at all. If that's you, then you'll need the enable_events parameter that is available for nearly all elements.
Setting enable_events means that like button presses, when that element is interacted with (e.g. clicked on,
a character entered into) then an event is immediately generated causing your window.read() call to return.
"""
import PySimpleGUI as simpleGUI
choices = ('Red', 'Green', 'Blue', 'Yellow', 'Orange', 'Purple', 'Chartreuse')


def responsive_list_ok_btn():
    layout = [[simpleGUI.Text('What is your favorite color?')],
              [simpleGUI.Listbox(choices, size=(15, len(choices)), key='-COLOR-')],
              [simpleGUI.Button('Ok')]]

    window = simpleGUI.Window('Pick a color', layout)

    while True:  # the event loop
        event, values = window.read()
        if event == simpleGUI.WIN_CLOSED:
            break
        if event == 'Ok':
            if values['-COLOR-']:  # if something is highlighted in the list
                simpleGUI.popup(f"Your favorite color is {values['-COLOR-'][0]}")
    window.close()


def most_responsive_windows():
    layout = [[simpleGUI.Text('What is your favorite color?')],
              [simpleGUI.Listbox(choices, size=(15, len(choices)), key='-COLOR-', enable_events=True)]]

    window = simpleGUI.Window('Pick a color', layout)

    while True:  # the event loop
        event, values = window.read()
        if event == simpleGUI.WIN_CLOSED:
            break
        if values['-COLOR-']:  # if something is highlighted in the list
            simpleGUI.popup(f"Your favorite color is {values['-COLOR-'][0]}")
    window.close()


if __name__ == '__main__':
    responsive_list_ok_btn()
    most_responsive_windows()
