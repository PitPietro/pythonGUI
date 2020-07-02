import PySimpleGUI as simpleGUI

def exiting_win_1(event):
    if event in (simpleGUI.WIN_CLOSED, 'Quite'):
        pass
        # break
    print('Windows exited')


def exiting_win_2(event):
    if event == simpleGUI.WIN_CLOSED or event == 'Quite':
        pass
        # break
    print('Windows exited')