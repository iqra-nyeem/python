from Tkinter import *
root = Tk()
one = Label(root, text='1',bg='black')
two = Label(root, text='2',bg='blue')
three= Label(root, text="3",bg='red')

one.pack(fill=X)
two.pack(side=LEFT , fill=Y)
three.pack(fill=X)

bottomFrame =  Frame(root)
four= Label(bottomFrame,text='4',bg='pink')
four.pack(side=RIGHT,fill=Y)

bottomFrame.pack()
root.mainloop()
