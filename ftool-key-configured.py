'''
@MrT0xiC

Free, open-source ftool for your convenience
'''

import win32api
import win32gui
import win32con

KEYBD_CONSTS = {'0':0x30,
           '1':0x31,
           '2':0x32,
           '3':0x33,
           '4':0x34,
           '5':0x35,
           '6':0x36,
           '7':0x37,
           '8':0x38,
           '9':0x39,
           'F1':0x70,
           'F2':0x71,
           'F3':0x72,
           'F4':0x73,
           'F5':0x74,
           'F6':0x75,
           'F7':0x76,
           'F8':0x77,
           'F9':0x78,
           'F10':0x79}

global handlers
handlers = []

def enumHandler(hwnd, lParam):
    if win32gui.IsWindowVisible(hwnd):
        win_name = win32gui.GetWindowText(hwnd)
        if win_name.find("Insanity MMORPG (") != -1:
            handlers.append([win32gui.FindWindow(None, win_name), win_name])

def main():
    win32gui.EnumWindows(enumHandler, None)

    print("Choose client to attach:")
    [print(f'{i+1}.{handlers[i][1]}') for i in range(len(handlers))]
    client_id = handlers[int(input())-1][0]
    while True:
        if win32api.GetAsyncKeyState(KEYBD_CONSTS['F1']):
            win32gui.SendMessage(client_id, win32con.WM_KEYDOWN, KEYBD_CONSTS['F1'], 0)
            win32gui.SendMessage(client_id, win32con.WM_KEYUP, KEYBD_CONSTS['F1'], 0)

if __name__ == '__main__':
    main()