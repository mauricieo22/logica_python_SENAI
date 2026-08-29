from tkinter import Tk,Canvas

janela = Tk()
janela. geometry("500x400")

canvas = Canvas(janela, width= 400, height= 300, bg="black")

canvas.create_text(80,150, text="ITALICO", font=("Arial", 12,"italic"), fill= "orange")
canvas.create_text(130,200, text="TEXTO", font=("Arial", 20), fill= "green", anchor="e")
canvas.create_text(200,100, text="TEXTINHO", font=("Arial", 5,"bold"), fill= "pink", anchor="w")
canvas.create_text(300,250, text="TEXTÃO", font=("Arial", 35,"bold"), fill= "white")

canvas.pack()
janela.mainloop()