import shutil
import os
from tkinter import *

# Create the main window
root = Tk()
root.geometry("600x400")
label2 = Label(root, text="Programa para copear archivos")
label2.pack()
# Create a counter variable and set it to 0
status = "Empezar"


# Create a function that increases the counter by 1 when the button is clicked
def start_copy():
    global status
    status = "Copeando archivos"
    label.config(text=status)
    # Establece la ruta de la carpeta de origen y la ruta de la carpeta de destino
    #origen = r'C:\Users\Administrador\Desktop\PRUEBAS_PYTON\origen'
    #destino = r'C:\Users\24\Desktop\copy files RC python\destino'
    #origen = r'E:\2008\TAMUIN01_2008\2008\TAMUIN\1\Exportar\Pdf'
    origen = '\dev\cdrom'
    destino = r'C:\Users\Administrador\Desktop\PRUEBAS_PYTON\destino'



    # Obtiene la lista de archivos en la carpeta de origen
    archivos = os.listdir(origen)

    # Recorre la lista de archivos y los copia a la carpeta de destino
    for archivo in archivos:
      ruta_archivo = os.path.join(origen, archivo)
      shutil.copy(ruta_archivo, destino)

    print('Los archivos han sido copiados con éxito')
    status = "Finalizado"
    label.config(text=status)


def obtener_nombre():
  nombre = entry.get()
  label.config(text=f"Hola, {nombre}!")
    
# COPY
button = Button(root, text="Copy", command=start_copy)
button.pack()



# Create a label widget to display the counter
label = Label(root, text=F"Status: {status}")
label.pack()


# Run the main loop
root.mainloop()


