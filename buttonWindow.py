import tkinter as tk

# Crea la ventana principal
root = tk.Tk()
root.title("Contador")

# Crea un contador y una etiqueta para mostrar el contador
count = 0
label = tk.Label(root, text=count)
label.pack()

# Crea un botón para aumentar el contador
def increment_count():
    global count
    count += 1
    label.config(text=count)

button = tk.Button(root, text="Incrementar", command=increment_count)
button.pack()

# Inicia el bucle de eventos
root.mainloop()
