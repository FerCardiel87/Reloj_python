import tkinter as tk


def obtener_hora_actual():
    from datetime import datetime
    return datetime.now().strftime("%H:%M:%S")

raiz = tk.Tk()
variable_hora_actual = tk.StringVar(raiz, value=obtener_hora_actual())
raiz.etiqueta = tk.Label(
    raiz, textvariable=variable_hora_actual, font=f"Consolas 60")
raiz.etiqueta.pack(side="top")
app = tk.Frame()
raiz.title("Reloj en Tkinter - By Parzibyte")

app.pack()
app.mainloop()