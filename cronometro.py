import tkinter as tk

def iniciar():
    global corriendo
    corriendo = True
    cuenta_atras()

def pausar():
    global corriendo
    corriendo = False
    
def reiniciar():
    global tiempo, corriendo
    corriendo = False
    tiempo = 10
    lbl.config(text=str(tiempo))
    
def cuenta_atras():
    global tiempo
    if corriendo:
        tiempo -= 1
        lbl.config(text=str(tiempo))
        root.after(1000, cuenta_atras)
    elif tiempo == 0 and corriendo:
        lbl.config(text="Tiempo!!!!")
        
        
root = tk.Tk()
root.title("Cronómetro")
tiempo = 10
corriendo =  False

lbl = tk.Label(root, text=str(tiempo), font={"Arial", 32})
lbl.pack(pady=15)

bin_iniciar = tk.Button(root, text="Iniciar", command=iniciar)
bin_iniciar.pack(side="left", padx=10)

bin_pausar = tk.Button(root, text="Pausar", command=pausar)
bin_pausar.pack(side="left", padx=10)

bin_reiniciar = tk.Button(root, text="Reiniciar", command=reiniciar)
bin_reiniciar.pack(side="left", padx=10)

root.mainloop()