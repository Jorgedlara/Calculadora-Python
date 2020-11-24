from tkinter import *

#Configuración de tkinter

window = Tk()
window.title("Calculadora")

#Variables
i = 0

#Entrada ecuación y resultado

ecu_int = Entry (window, font = ("Arial 16"))
ecu_int.grid(row = 0, column = 0, columnspan = 4, padx = 5, pady = 5)
ecu_res = Entry (window, font = ("Arial 16"))
ecu_res.grid(row =1, column = 0, columnspan = 4, padx =5, pady = 5)

#Funciones

def click_but(valor):
    global i
    ecu_int.insert(i, valor)
    i += 1

def clear():
    ecu_int.delete (0, END)
    ecu_res.delete(0, END)
    i = 0

def resolver():
    ecu_res.delete(0, END)
    ec = ecu_int.get()
    resultado = eval(ec)
    ecu_res.insert(0, resultado)

#Configuración botones calculadora

boton1 = Button(window, text = "1", width = 5, height =2, command = lambda: click_but(1))
boton2 = Button(window, text = "2", width = 5, height =2, command = lambda: click_but(2))
boton3 = Button(window, text = "3", width = 5, height =2, command = lambda: click_but(3))
boton4 = Button(window, text = "4", width = 5, height =2, command = lambda: click_but(4))
boton5 = Button(window, text = "5", width = 5, height =2, command = lambda: click_but(5))
boton6 = Button(window, text = "6", width = 5, height =2, command = lambda: click_but(6))
boton7 = Button(window, text = "7", width = 5, height =2, command = lambda: click_but(7))
boton8 = Button(window, text = "8", width = 5, height =2, command = lambda: click_but(8))
boton9 = Button(window, text = "9", width = 5, height =2, command = lambda: click_but(9))
boton0 = Button(window,text = "0", width = 23, height =2, command = lambda: click_but(0))

boton_clear = Button(window, text = "C", width = 5, height =2, command = lambda: clear())
boton_aparentesis = Button(window, text = "(", width = 5, height =2, command = lambda: click_but("("))
boton_cparentesis = Button(window, text = ")", width = 5, height =2, command = lambda: click_but(")"))

boton_div = Button(window, text = "/", width = 5, height =2, command = lambda: click_but("/"))
boton_mult = Button(window, text = "x", width = 5, height =2, command = lambda: click_but("*"))
boton_sum = Button(window, text = "+", width = 5, height =2, command = lambda: click_but("+"))
boton_res = Button(window, text = "-", width = 5, height =2, command = lambda: click_but("-"))
boton_eq = Button(window, text = "=", width = 5, height =2, command = lambda: resolver())

#Agregar botones a la interfaz

boton7.grid(row = 2, column = 0, padx = 5, pady = 5)
boton8.grid(row = 2, column = 1, padx = 5, pady = 5)
boton9.grid(row = 2, column = 2, padx = 5, pady = 5)
boton_div.grid(row = 2, column = 3, padx = 5, pady = 5)

boton4.grid(row = 3, column = 0, padx = 5, pady = 5)
boton5.grid(row = 3, column = 1, padx = 5, pady = 5)
boton6.grid(row = 3, column = 2, padx = 5, pady = 5)
boton_mult.grid(row = 3, column = 3, padx = 5, pady = 5)

boton1.grid(row = 4, column = 0, padx = 5, pady = 5)
boton2.grid(row = 4, column = 1, padx = 5, pady = 5)
boton3.grid(row = 4, column = 2, padx = 5, pady = 5)
boton_sum.grid(row = 4, column = 3, padx = 5, pady = 5)

boton0.grid(row = 5, column = 0, columnspan = 3, padx = 5, pady = 5)
boton_res.grid(row = 5, column = 3, padx = 5, pady = 5)

boton_clear.grid(row = 6, column = 0, padx = 5, pady = 5)
boton_aparentesis.grid(row = 6, column = 1, padx = 5, pady = 5)
boton_cparentesis.grid(row = 6, column = 2, padx = 5, pady = 5)
boton_eq.grid(row = 6, column = 3, padx = 5, pady = 5)


window.mainloop()