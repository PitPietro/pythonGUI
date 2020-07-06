import os
import sys

import PySimpleGUI as simpleGUI

'''https://pysimplegui.readthedocs.io/en/latest/cookbook/#recipe-1-shot-window-simple-data-entry-return-values-auto
-numbered If you do not specify a key and the element is an input element, a key will be provided for you in the form 
of an integer, starting numbering with zero. If you don't specify any keys, it will appear as if the values returned 
to you are being returned as a list because the keys are sequential ints. 

'''


def simple_data_entry_win():
    layout = [
        [simpleGUI.Text('Please enter your Name, Address, Phone')],
        [simpleGUI.Text('Name', size=(15, 1)), simpleGUI.InputText()],
        [simpleGUI.Text('Address', size=(15, 1)), simpleGUI.InputText()],
        [simpleGUI.Text('Phone', size=(15, 1)), simpleGUI.InputText()],
        [simpleGUI.Submit(), simpleGUI.Cancel()]
    ]

    window = simpleGUI.Window('Simple data entry window', layout)
    event, values = window.read()
    window.close()
    print(event, values[0], values[1], values[2])  # the input data looks like a simple list when auto numbered


def browse_file():
    if len(sys.argv) == 1:
        event, values = simpleGUI.Window('My Script',
                                         [[simpleGUI.Text('Document to open')],
                                          [simpleGUI.In(), simpleGUI.FileBrowse()],
                                          [simpleGUI.Open(), simpleGUI.Cancel()]]).read(close=True)
        fname = values[0]
    else:
        fname = sys.argv[1]

    if not fname:
        simpleGUI.popup("Cancel", "No filename supplied")
        raise SystemExit("Cancelling: no filename supplied")
    else:
        cmd = 'libreoffice {}'.format(fname)
        os.system(cmd)
        simpleGUI.popup('The filename you chose was', fname)


def browse_file_single_line():
    if len(sys.argv) == 1:
        fname = simpleGUI.Window(
            'My Script',
            [
                [simpleGUI.Text('Document to open')],
                [simpleGUI.In(), simpleGUI.FileBrowse()
                 ],
                [simpleGUI.Open(), simpleGUI.Cancel()]]).read(close=True)[1][0]
    else:
        fname = sys.argv[1]

    if not fname:
        simpleGUI.popup("Cancel", "No filename supplied")
        raise SystemExit("Cancelling: no filename supplied")
    else:
        os.system('libreoffice {}'.format(fname))
        simpleGUI.popup('The filename you chose was', fname)


if __name__ == '__main__':
    # simple_data_entry_win()
    browse_file_single_line()
