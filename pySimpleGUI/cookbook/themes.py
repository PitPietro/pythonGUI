import PySimpleGUI as simpleGUI
from random import uniform

'''
The default theme is: Dark Blue 3
'''
DEFAULT_THEME = 'Dark Blue 3'


def select_random_theme():
    themes = simpleGUI.theme_list()
    t_num = len(themes) - 1
    r_int = int(uniform(0, t_num))
    random_theme = themes[r_int]
    print('Theme: ', random_theme, r_int)
    return random_theme
