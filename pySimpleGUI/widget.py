# Example of (almost) all widgets, that you can use in PySimpleGUI.

import PySimpleGUI as sG
# import tkinter as tk


def widget():
    sG.change_look_and_feel('GreenTan')
    # ------ Menu Definition ------ #
    menu_def = [['&File', ['&Open', '&Save', 'E&xit', 'Properties']],
                ['&Edit', ['Paste', ['Special', 'Normal', ], 'Undo'], ],
                ['&Help', '&About...'], ]

    # ------ Column Definition ------ #
    column1 = [[sG.Text('Column 1', background_color='lightblue', justification='center', size=(10, 1))],
               [sG.Spin(values=('Spin Box 1', '2', '3'),
                        initial_value='Spin Box 1')],
               [sG.Spin(values=('Spin Box 1', '2', '3'),
                        initial_value='Spin Box 2')],
               [sG.Spin(values=('Spin Box 1', '2', '3'), initial_value='Spin Box 3')]]

    layout = [
        [sG.Menu(menu_def, tearoff=True)],
        [sG.Text('(Almost) All widgets in one Window!', size=(
            30, 1), justification='center', font=("Helvetica", 25), relief=sG.RELIEF_RIDGE)],
        [sG.Text('Here is some text.... and a place to enter text')],
        [sG.InputText('This is my text')],
        [sG.Frame(layout=[
            [sG.CBox('Checkbox', size=(10, 1)),
             sG.CBox('My second checkbox!', default=True)],
            [sG.Radio('My first Radio!     ', "RADIO1", default=True, size=(10, 1)),
             sG.Radio('My second Radio!', "RADIO1")]], title='Options',
            title_color='red',
            relief=sG.RELIEF_SUNKEN,
            tooltip='Use these to set flags')],
        [sG.MLine(default_text='This is the default Text should you decide not to type anything', size=(35, 3)),
         sG.MLine(default_text='A second multi-line', size=(35, 3))],
        [sG.Combo(('Combobox 1', 'Combobox 2'), size=(20, 1)),
         sG.Slider(range=(1, 100), orientation='h', size=(34, 20), default_value=85)],
        [sG.OptionMenu(('Menu Option 1', 'Menu Option 2', 'Menu Option 3'))],
        [sG.Listbox(values=('Listbox 1', 'Listbox 2', 'Listbox 3'), size=(30, 3)),
         sG.Frame('Labelled Group', [[
             sG.Slider(range=(1, 100), orientation='v', size=(5, 20), default_value=25, tick_interval=25),
             sG.Slider(range=(1, 100), orientation='v', size=(5, 20), default_value=75),
             sG.Slider(range=(1, 100), orientation='v', size=(5, 20), default_value=10),
             sG.Col(column1, background_color='lightblue')]])
         ],
        [sG.Text('_' * 80)],
        [sG.Text('Choose A Folder', size=(35, 1))],
        [sG.Text('Your Folder', size=(15, 1), justification='right'),
         sG.InputText('Default Folder'), sG.FolderBrowse()],
        [sG.Submit(tooltip='Click to submit this form'), sG.Cancel()]]

    window = sG.Window('Everything bagel', layout,
                       default_element_size=(40, 1), grab_anywhere=False)

    event, values = window.read()
    sG.popup('Title',
             'The results of the window.',
             'The button clicked was "{}"'.format(event),
             'The values are', values)


if __name__ == '__main__':
    widget()
