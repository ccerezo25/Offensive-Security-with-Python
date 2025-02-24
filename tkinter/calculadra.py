import tkinter as tk 

class Calculadora: 
    def __init__(self, master):
        self.master = master 
        self.display = tk.Entry(master, width=15, font=("Arial",23), bd=10,justify="right")
        self.display.grid(row=0,column=0)
        
        buttons = [
            "7","8","9","/",
            "4","5","6","*",
            "1","2","3","-"
            "C","0",".","+","="
        ]


root = tk.Tk() #ventana principal
my_gui = Calculadora(root)
root.mainloop() #para poder usar los botones etc
