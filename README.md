# Python-FTool
Simple flyff ftool written in python :)
Its listening on main window to a specific keystroke and presses the a key on the secondary client.

All you need to do is replace the listening keypress listener(line 48) and the key to press(lines 49-50)

## Example:
```
        if win32api.GetAsyncKeyState(KEYBD_CONSTS['F1']):
            win32gui.SendMessage(client_id, win32con.WM_KEYDOWN, KEYBD_CONSTS['F1'], 0)
            win32gui.SendMessage(client_id, win32con.WM_KEYUP, KEYBD_CONSTS['F1'], 0)
```
listens to `F1` on main client and presses `F1` on attached client

```
        if win32api.GetAsyncKeyState(KEYBD_CONSTS['F9']):
            win32gui.SendMessage(client_id, win32con.WM_KEYDOWN, KEYBD_CONSTS['F1'], 0)
            win32gui.SendMessage(client_id, win32con.WM_KEYUP, KEYBD_CONSTS['F1'], 0)
```
listens to `F9` on main client and presses `F1` on attached client