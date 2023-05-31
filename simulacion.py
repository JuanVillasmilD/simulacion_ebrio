import random
import tkinter as tk
from tkinter import messagebox

def trayecto(cuadras):
    # Definir las posibles direcciones: norte, sur, este, oeste
    direcciones = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    x, y = 0, 0  # Iniciar en la posición (0, 0)

    for _ in range(cuadras):
        dx, dy = random.choice(direcciones)  # Escoger una dirección al azar
        x += dx
        y += dy

    return x, y

def calcular_probabilidad(intentos, cuadras):
    doscuadras_end = 0

    for _ in range(intentos):
        x, y = trayecto(cuadras)
        if abs(x) + abs(y) == 2:  # Verificar si termina a dos cuadras de distancia
            doscuadras_end += 1

    probabilidad = doscuadras_end / intentos
    return probabilidad

def iniciar_codigo():
    intentos = 1000  # Número de simulaciones
    cuadras = 10  # Número de cuadras a caminar

    probabilidad = calcular_probabilidad(intentos, cuadras)
    resultado_text.config(state="normal")
    resultado_text.delete("1.0", tk.END)
    resultado_text.insert(tk.END, f"La probabilidad de terminar a dos cuadras de distancia es: {probabilidad}\n")
    resultado_text.config(state="disabled")

def salir():
    if messagebox.askokcancel("Salir", "¿Estás seguro de que deseas salir?"):
        root.destroy()

# Crear la ventana principal
root = tk.Tk()
root.title("Simulación de Borracho Caminando")

# Personalizar el estilo
root.configure(bg="#222222")  # Fondo
root.geometry("500x400")  # Tamaño de la ventana (ancho x alto)

font = ("Arial", 12)  # Fuente y tamaño del texto

root.option_add("*Font", font)  # Establecer la fuente
root.option_add("*foreground", "white")  # Color de texto

# Espacio de separación
separador1 = tk.Label(root, text="", bg="#222222")
separador1.pack()

# Crear el botón de "Iniciar código"
iniciar_button = tk.Button(root, text="Iniciar código", command=iniciar_codigo, bg="#444444", font=font)  # Botón
iniciar_button.pack()

# Espacio de separación
separador2 = tk.Label(root, text="", bg="#222222")
separador2.pack()

# Crear el cuadro de texto para mostrar el resultado
resultado_text = tk.Text(root, width=40, height=10, bg="#333333", fg="white", font=font)
resultado_text.config(state="disabled")
resultado_text.pack()

# Espacio de separación
separador3 = tk.Label(root, text="", bg="#222222")
separador3.pack()

# Crear el botón de "Salir"
salir_button = tk.Button(root, text="Salir", command=salir, bg="#444444", font=font)
salir_button.pack()

# Ejecutar el bucle principal de la interfaz gráfica
root.mainloop()