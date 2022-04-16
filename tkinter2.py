from tkinter import Tk
root=Tk()
#to print screen size
screen_width=root.winfo_screenwidth()
screen_height=root.winfo_screenheight()
print("Screen width:",screen_width)
print("Screen height:",screen_height)
#resize tkinter window 400x200 and place at position (150,150)root.geometry("400x200+150+150")
root.mainloop()