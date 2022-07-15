import PySimpleGUI as psg
import pyautogui as pag

psg.theme('DarkBrown3')

layout=[[psg.Text('',key='-XP-',font=('',20))],
        [psg.Text('',key='-YP-',font=('',20))],
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
    #update position infomation per 10ms
    event,values=wnd.read(timeout=10,timeout_key='-timeout-')
    #if click exit button
    if event in (psg.WIN_CLOSED,'exit'):
        break
    #updating position
    elif event == '-timeout-':
        wnd['-XP-'].update(xStr)
        wnd['-YP-'].update(yStr)
    

wnd.close()

