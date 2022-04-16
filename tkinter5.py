from tkinter import Tk,Menu
root=Tk()
#create main menu bar
menu_bar=Menu(root)
#create the submenu, tearoff indicates that menu can pop out
fileMenu=Menu(menu_bar,tearoff=0)
#add commands to submenu
fileMenu.add_command(label="stop",command=root.destroy)
fileMenu.add_command(label="kill",command=root.destroy)
fileMenu.add_command(label="exit",command=root.destroy)
#add the file drop menu down sub-menu in the main menu bar
menu_bar.add_cascade(label="File",menu=fileMenu)
root.config(menu=menu_bar)
root.mainloop()