from Tkinter import *

class myButtons:
    def __init__(self,master):
        self.printButton= Button(master, text='File',command=self.printMessage)
        self.printButton.pack(side=LEFT)

        self.quitButton = Button(master, text='Quit', command=master.quit)
        self.quitButton.pack(side=LEFT)

    def printMessage(self):
        print('printing message')

root = Tk()
b=myButtons(root)
root.mainloop()