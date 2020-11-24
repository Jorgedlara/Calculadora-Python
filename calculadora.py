from tkinter import *

#Configuración de tkinter

window = Tk()
window.title("Calculadora")

#Entrada ecuación y resultado

ecu_int = Entry (window, font = ("Arial 16"))
ecu_int.grid(row = 0, column = 0, columnspan = 4, padx = 5, pady = 5)
ecu_res = Entry (window, font = ("Arial 16"))
ecu_res.grid(row =1, column = 0, columnspan = 4, padx =5, pady = 5)

#Configuración botones calculadora

boton1 = Button(window, text = "1", width = 5, height =2)
boton2 = Button(window, text = "2", width = 5, height =2)
boton3 = Button(window, text = "3", width = 5, height =2)
boton4 = Button(window, text = "4", width = 5, height =2)
boton5 = Button(window, text = "5", width = 5, height =2)
boton6 = Button(window, text = "6", width = 5, height =2)
boton7 = Button(window, text = "7", width = 5, height =2)
boton8 = Button(window, text = "8", width = 5, height =2)
boton9 = Button(window, text = "9", width = 5, height =2)
boton0 = Button(window,text = "0", width = 23, height =2)

boton_clear = Button(window, text = "C", width = 5, height =2)
boton_aparentesis = Button(window, text = "(", width = 5, height =2)
boton_cparentesis = Button(window, text = ")", width = 5, height =2)

boton_div = Button(window, text = "/", width = 5, height =2)
boton_mult = Button(window, text = "x", width = 5, height =2)
boton_sum = Button(window, text = "+", width = 5, height =2)
boton_res = Button(window, text = "-", width = 5, height =2)
boton_eq = Button(window, text = "=", width = 5, height =2)
boton = Button(window, text = "", width = 5, height =2)

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