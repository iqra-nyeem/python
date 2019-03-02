from Tkinter import *
root =Tk()
def call_me():
    print('Iqra Naeem')

button = Button(root,text='click me',command=call_me)

button.pack()
root.mainloop()

