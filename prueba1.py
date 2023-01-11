import shutil
import os
from tkinter import *
from tkinter import ttk

#Function that print the operation status
def changeStatus(status):
  ttk.Label(mainframe, text=status).grid(column=3, row=2, sticky=E)

# Create a function that increases the counter by 1 when the button is clicked
def start_copy():
    changeStatus("                                            ")
    changeStatus("Copeando archivos")
    
    # Establece la ruta de la carpeta de origen y la ruta de la carpeta de destino
    #origen = r'C:\Users\Administrador\Desktop\PRUEBAS_PYTON\origen'
    #destino = r'C:\Users\24\Desktop\copy files RC python\destino'
    #origen = r'E:\2008\TAMUIN01_2008\2008\TAMUIN\1\Exportar\Pdf'
    #origen = '\dev\cdrom'
    #destino = r'C:\Users\Administrador\Desktop\PRUEBAS_PYTON\destino'
    # Obtiene la lista de archivos en la carpeta de origen
    #archivos = os.listdir(origen)

    # Recorre la lista de archivos y los copia a la carpeta de destino
    #for archivo in archivos:
      #ruta_archivo = os.path.join(origen, archivo)
      #shutil.copy(ruta_archivo, destino)
    changeStatus("                                             ")
    changeStatus("Finalizado")
    print(ruta.get())
    print('Los archivos han sido copiados con éxito')
    

# Create the main window
root = Tk()
root.title("Copy Files")
#root.geometry("600x400")

#Apariencia
mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
  #root.geometry("600x400")
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)


ruta = StringVar()
ruta_entry = ttk.Entry(mainframe, width=30, textvariable=ruta)
ruta_entry.grid(column=3, row=1, sticky=(W, E))

ttk.Button(mainframe, text="Inciar", command=start_copy, width=30).grid(column=3, row=3, sticky=W)

#Labels
ttk.Label(mainframe, text="Ruta Inicial", width=15).grid(column=1, row=1, sticky=W)

changeStatus("Introduzca ruta inicial")

ttk.Label(mainframe, text="Status", width=15).grid(column=1, row=2, sticky=W)

for child in mainframe.winfo_children(): 
    child.grid_configure(padx=5, pady=5)

# Run the main loop
root.mainloop()


 