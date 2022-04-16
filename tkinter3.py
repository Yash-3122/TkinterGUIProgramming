from tkinter import Tk,Button
root=Tk()
#exit window will close GUI window when clicked
exitButton=Button(root,text='Exit program',command=root.destroy)
exitButton.pack()
#to write a message on the screen
def my_callback():
    print("you clicked the button....")
msg_button=Button(root,text='click here',command=my_callback)
msg_button.pack()
root.mainloop()