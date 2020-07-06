from random import uniform

import PySimpleGUI as simpleGUI

'''
https://pysimplegui.readthedocs.io/en/latest/cookbook/#themes-window-beautification

The default theme is: Dark Blue 3

> Theme Name Format
You can look at the table of available themes to get the name of a theme you want to try, or you can "guess" at one 
using this formula: <"Dark" | "Light"> <Color> [#] Where Color is one of these: Black, Blue, Green, Teal, Brown, 
Yellow, Gray, Purple The # is optional and is used when there is more than 1 choice for a color. For example, 
for "Dark Blue" there are 12 different themes (Dark Blue, and Dark Blue 1-11). These colors specify the rough color 
of the background.
'''
DEFAULT_THEME = 'Dark Blue 3'


def select_random_theme():
    themes = simpleGUI.theme_list()
    t_num = len(themes) - 1
    r_int = int(uniform(0, t_num))
    random_theme = themes[r_int]
    print('Theme: ', random_theme, r_int)
    return random_theme


def list_all_themes():
    themes = simpleGUI.theme_list()
    t_num = len(themes) - 1
    for i in range(0, t_num):
        print('Theme: ', themes[i], i)


def theme_preview():
    simpleGUI.theme_previewer()


def builtin_theme_viewer():
    simpleGUI.preview_all_look_and_feel_themes()


def theme_list():
    return simpleGUI.theme_list()


def theme_browser():
    """
        Allows you to "browse" through the Theme settings.  Click on one and you'll see a
        Popup window using the color scheme you chose.  It's a simple little program that also demonstrates
        how snappy a GUI can feel if you enable an element's events rather than waiting on a button click.
        In this program, as soon as a listbox entry is clicked, the read returns.
    """

    simpleGUI.theme('Dark Brown')

    layout = [[simpleGUI.Text('Theme Browser')],
              [simpleGUI.Text('Click a Theme color to see demo window')],
              [simpleGUI.Listbox(values=simpleGUI.theme_list(), size=(20, 12), key='-LIST-', enable_events=True)],
              [simpleGUI.Button('Exit')]]

    window = simpleGUI.Window('Theme Browser', layout)

    while True:  # Event Loop
        event, values = window.read()
        if event in (simpleGUI.WIN_CLOSED, 'Exit'):
            break
        simpleGUI.theme(values['-LIST-'][0])
        simpleGUI.popup_get_text('This is {}'.format(values['-LIST-'][0]))

    window.close()


if __name__ == '__main__':
    list_all_themes()
    print(theme_list())
    theme_browser()
    theme_preview()
