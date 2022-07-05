import imp
import pyautogui,sys,clock


print('press ctrl-c to quit')
print("current time is ",clock.now())
try:
    while True:
        x,y=pyautogui.position()
        positionStr = "X: " + str(x).rjust(4) + " Y: " + str(y).rjust(4)
        print(positionStr,end='')
        print('\b' * len(positionStr),end='',flush=True)
except KeyboardInterrupt:
    print('quit program \n')