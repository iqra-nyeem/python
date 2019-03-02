
from Tkinter  import *
root = Tk()

name = Label(root, text='Name')
password=Label(root, text='Password')

entry1=Entry(root)
entry2=Entry(root)

name.grid(row=0,column=0)
entry1.grid(row=0,column=1)

password.grid(row=1,column=0)
entry2.grid(row=1,column=1)

c=Checkbutton(root,text='keep me logged in')
c.grid(columnspan=2)


root.mainloop()