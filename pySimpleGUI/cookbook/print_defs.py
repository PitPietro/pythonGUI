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
> 3. The Multiline Element


"""
import PySimpleGUI as simpleGUI


def print_on_debug_win():
    simpleGUI.Print('Re-routing the stdout', do_not_reroute_stdout=False)
    print('This is a normal print that has been re-routed.')


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


if __name__ == '__main__':
    print_on_debug_win()
    print_colors()
