from Tkinter import *
root = Tk()

frame = Frame(root)
button1 = Button(frame, text='1')
button2 = Button(frame, text='2')
button3 = Button(frame, text='3')
button1.pack(side=LEFT)
button2.pack(side=LEFT)
button3.pack(side=RIGHT)
frame.pack()
root.mainloop()


from Tkinter import *
root = Tk()

frame = Frame(root, width=300 , height=300)
frame.pack()
root.mainloop()