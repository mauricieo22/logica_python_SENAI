import tkinter as tk

root = tk.Tk()

root.geometry("200x200")

root.resizable(True,True)

root.minsize(300,200)
root.maxsize(800,600)

root.attributes("-alpha", 0.6) #translucido

root.mainloop()