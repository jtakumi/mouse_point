import PySimpleGUI as psg
import pyautogui as pag

psg.theme('DarkBrown3')

x,y=pag.position()
xStr="X: " + str(x).rjust(4)
yStr=" Y: " + str(y).rjust(4)

layout=[[psg.Text('',key='-XP-')],
        [psg.Text('',key='-YP-')],
        [psg.Button('detect',size=(10,3))],
        [psg.Button('exit',size=(10,3))]
]

#window title
wnd=psg.Window('mouse_pointer',layout,size=(300,200))

#loop function
while True:
    x,y=pag.position()
    xStr="X: " + str(x).rjust(4)
    yStr="Y: " + str(y).rjust(4)
    #reading window info
    event,values=wnd.read()
    #if click exit button
    if event in (psg.WIN_CLOSED,'exit'):
        break
    #updating position
    if event == 'detect':
        wnd['-XP-'].update(xStr)
        wnd['-YP-'].update(yStr)
    

wnd.close()

