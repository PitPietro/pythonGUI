"""
https://pysimplegui.readthedocs.io/en/latest/cookbook/#recipe-printing
There are 3 ways to transform print statements into GUI solution:
> 1. The Debug window
The functions Print, eprint, EasyPrint all refer to the same funtion. There is no difference which you use as they point
to identical code. The one you'll see used in Demo Programs is Print.
One method for routing your print statements to the debug window is to reassign the print keyword to be the PySimpleGUI
function Print. This can be done through simple assignment.
`print = simpleGUI.Print`
You can also remap stdout to the debug window by calling Print with the parameter do_not_reroute_stdout = False.
This will reroute all of your print statements out to the debug window.

> 2. The Output Element
If you want to re-route your standard out to your window, then placing an Output Element in your layout will do just
that. When you call "print", your text will be routed to that Output Element. Note you can only have 1 of these in your
layout because there's only 1 stdout. Of all of the "print" techniques, this is the best to use if you cannot change
your print statements. The Output element is the best choice if your prints are in another module that you don't have
control over such that "redefining / reassigning" what print does isn't a possibility. This layout with an
Output element shows the results of a few clicks of the Go Button.

> 3. The Multiline Element
Beginning in 4.18.0 you can "print" to any Multiline Element in your layouts. The Multiline.print method acts similar
to the Print function described earlier. It has the normal print parameters sep & end and also has color options. It's like a super-charged print statement.

"""
import time

import PySimpleGUI as simpleGUI


def print_on_debug_win():
    simpleGUI.Print('Re-routing the stdout', do_not_reroute_stdout=False)
    print('This is a normal print that has been re-routed.')
    time.sleep(10)


def print_colors():
    simpleGUI.Print('This text is white on a green background', text_color='white', background_color='green',
                    font='Courier 10')
    simpleGUI.Print('The first call sets some window settings like font that cannot be changed')
    simpleGUI.Print('This is plain text just like a print would display')
    simpleGUI.Print('White on Red', background_color='red', text_color='white')
    simpleGUI.Print('The other print', 'parms work', 'such as sep', sep=',')
    simpleGUI.Print('To not extend a colored line use the "end" parm', background_color='blue', text_color='white',
                    end='')
    simpleGUI.Print('\nThis line has no color.')
    time.sleep(10)


def print_to_output_element():
    layout = [[simpleGUI.Text('What you print will display below:')],
              [simpleGUI.Output(size=(50, 10), key='-OUTPUT-')],
              [simpleGUI.In(key='-IN-')],
              [simpleGUI.Button('Go'), simpleGUI.Button('Clear'), simpleGUI.Button('Exit')]]

    window = simpleGUI.Window('Window Title', layout)

    while True:  # Event Loop
        event, values = window.read()
        print(event, values)
        if event in (simpleGUI.WIN_CLOSED, 'Exit'):
            break
        if event == 'Clear':
            window['-OUTPUT-'].update('')
    window.close()


def print_to_multiline():
    layout = [[simpleGUI.Text('Demonstration of Multiline Element Printing')],
              [simpleGUI.MLine(key='-ML1-' + simpleGUI.WRITE_ONLY_KEY, size=(40, 8))],
              [simpleGUI.MLine(key='-ML2-' + simpleGUI.WRITE_ONLY_KEY, size=(40, 8))],
              [simpleGUI.Button('Go'), simpleGUI.Button('Exit')]]

    window = simpleGUI.Window('Window Title', layout, finalize=True)

    # Note, need to finalize the window above if want to do these prior to calling window.read()
    window['-ML1-' + simpleGUI.WRITE_ONLY_KEY].print(1, 2, 3, 4, end='', text_color='red', background_color='yellow')
    window['-ML1-' + simpleGUI.WRITE_ONLY_KEY].print('\n', end='')
    window['-ML1-' + simpleGUI.WRITE_ONLY_KEY].print(1, 2, 3, 4, text_color='white', background_color='green')
    counter = 0

    while True:  # Event Loop
        event, values = window.read(timeout=100)
        if event in (simpleGUI.WIN_CLOSED, 'Exit'):
            break
        if event == 'Go':
            window['-ML1-' + simpleGUI.WRITE_ONLY_KEY].print(event, values, text_color='red')
        window['-ML2-' + simpleGUI.WRITE_ONLY_KEY].print(counter)
        counter += 1
    window.close()


if __name__ == '__main__':
    print_on_debug_win()
    print_colors()
    print_to_output_element()
    print_to_multiline()
