import tkinter as tk

root = tk.Tk()
root.title("SENAI - Desenvolvimento de Sistemas")
root.config(bg="skyblue")

frame = tk.Frame(root, width=420, height=220)
frame.pack(padx=10, pady=10)

frame_a = tk.Frame(frame, width=190, height=190, bg="red")
frame_a.pack(side="top", padx=10, pady=10)

frame_b = tk.Frame(frame, width=190, height=190, bg="green")
frame_b.pack(side="bottom", padx=10, pady=10)

root.mainloop()