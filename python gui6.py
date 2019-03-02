from Tkinter import *

root = Tk()

def LeftClick(event):
    print('Naeem')

def MiddleClick(event):
    print('Akhtar')

def RightCLick(event):
    print('Iqra')

frame=Frame(root, width=300,height=300)
frame.bind('<Button_1>' , LeftClick(root))
frame.bind('<Button_2>' , MiddleClick(root))
frame.bind('<Button_3>' , RightCLick(root))

frame.pack()
root.mainloop()