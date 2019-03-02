from Tkinter import *

def python():
    print('PYTHON GUI')


root = Tk()
main_menu = Menu(root)
root.config(menu=main_menu)

fileMenu= Menu(main_menu)
main_menu.add_cascade(label='file', menu=fileMenu)

editMenu= Menu(main_menu)
main_menu.add_cascade(label='edit', menu=editMenu)

fileMenu.add_command(label="New Project", command=python)

fileMenu.add_separator()
fileMenu.add_command(label="save as", command=python)
fileMenu.add_command(label="open", command=python)
save_menu=Menu(fileMenu)
main_menu.add_cascade(label='save',menu=save_menu)









root.mainloop()