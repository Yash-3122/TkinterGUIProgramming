from tkinter import Tk,Canvas
root=Tk()
canvas=Canvas(root,width=250,height=200)
canvas.pack()#draw orange dashed line
canvas.create_line(0,0,250,200,fill='orange',dash=(5,15))#draw yellow rectangle at (100,50)to (150,60)
canvas.create_rectangle(100,50,150,60,fill='yellow')#draw oval(circle) from (30,30) to (50,50)
canvas.create_oval(30,30,50,50,fill='green')
root.mainloop()