import tkinter as tk

def operar(operacion):
    try:
        
        num1 = float(txt_num1.get())
        num2 = float(txt_num2.get())
        
# Programar lógica de cada operación

        if operacion == '+':
            resultado = num1 + num2
        elif operacion == '-':
            resultado = num1 - num2
        elif operacion == '*':
            resultado = num1 * num2
        elif operacion == '/':
            if num2 == 0:
                lbl_resultado.config(text="Error, no puedes dividir entre cero")
                return
            resultado = num1 / num2

        lbl_resultado.config(text="Resultado " + str(resultado))

    except ValueError:
        lbl_resultado.config(text="Error, introduce solo números")
        
# Generar una ventana principal. Motor gráfico

ventana = tk.Tk()
ventana.title("Calculadora")

tk.Label(ventana, text="Primer número :").grid(row=0, column=0, padx=10, pady=10)
txt_num1 = tk.Entry(ventana)
txt_num1.grid(row=0, column=1, padx=10, pady=10)

tk.Label(ventana, text="Segundo número :").grid(row=1, column=0, padx=10, pady=10)
txt_num2 = tk.Entry(ventana)
txt_num2.grid(row=1, column=1, padx=10, pady=10)

#Botones calculadora

btn_sumar = tk.Button(ventana, text="Sumar", command=lambda: operar('+'))
btn_sumar.grid(row=2, column=0, padx=10, pady=5, sticky="we")

btn_restar = tk.Button(ventana, text="Restar", command=lambda: operar('-'))
btn_restar.grid(row=2, column=1, padx=10, pady=5, sticky="we")

btn_multiplicar = tk.Button(ventana, text="Multiplicar", command=lambda: operar('*'))
btn_multiplicar.grid(row=3, column=0, padx=10, pady=5, sticky="we")

btn_dividir = tk.Button(ventana, text="Dividir", command=lambda: operar('/'))
btn_dividir.grid(row=3, column=1, padx=10, pady=5, sticky="we")

#Etiqueta resultado

lbl_resultado = tk.Label(ventana, text="Resultado")
lbl_resultado.grid(row=4, column=0, columnspan=2, pady=15)

ventana.mainloop()