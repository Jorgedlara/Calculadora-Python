from tkinter import *

#Configuración de tkinter

window = Tk()
window.title("Calculadora")

#Entrada ecuación y resultado
ecu_int = Entry (window, font = ("Arial 20"))
ecu_int.grid(row = 0, column = 0, columnspan = 4, padx = 5, pady = 5)
ecu_res = Entry (window, font = ("Arial 20"))
ecu_res.grid(row =1, column = 0, columnspan = 4, padx =5, pady = 5)


window.mainloop()