from tkinter import *
from turtle import back, position
from pynput.mouse import Controller
import tkinter,sys,pyautogui


class App(Frame):
    def __init__(self,master=None):
        Frame.__init__(self,master)
        self.master=master
        self.label = Label(text="",fg="snow",font=("arial",20))
        self.place(x=50,y=80)
        self.update_pos()
    def update_pos(self):
        x,y=pyautogui.position()
        positionStr = "X: " + str(x).rjust(4) + " Y: " + str(y).rjust(4)
        print(positionStr,end='')
        self.label.configure(text=positionStr)
        self.after(100,self.update_pos)

#Creating a GUI object 
wnd=tkinter.Tk()
app=App(wnd)
#the window size
wnd.geometry("300x200")
wnd.configure(bg='orange')
wnd.title('the window of mouse position.')
wnd.after(100,app.update_pos)
wnd.mainloop()

