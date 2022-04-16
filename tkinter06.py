from tkinter import Tk,Entry,Button,INSERT
root=Tk()
#create empty box
entry =Entry(root)
entry.pack()
#print the contents of entry box in a console
def printMsg():
    print(entry.get())
#create a button,when clicked will print the contents of the entry box
button=Button(root,text='print content',command=printMsg)
button.pack()
root.mainloop()