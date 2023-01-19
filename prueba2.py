import shutil
import os
from tkinter import *
from tkinter import ttk
from municipios import * #importa el archivo municipios.py
from navegaCarpetas import *

#Function that print the operation status
def changeStatus(status):
  ttk.Label(mainframe, text=status).grid(column=3, row=2, sticky=E)

# Function that copy files depending of the path
def start_copy():
    
    changeStatus("                                            ")
    changeStatus("Copeando archivos")
    
    #Establece la ruta de la carpeta de origen y la ruta de la carpeta de destino
    #origen = r"C:\Users\24\Desktop\copy files RC python\origen"
    origen = ruta.get()
    destino = r'C:\Users\24\Desktop\copy files RC python\destino'
    lista = manejaRutaOrigen(origen) #funcion para manejar la ruta de origen y dividir respecto a municipio, oficialia
    rutaPdf = navegacionCarpeta(origen) #funcion para llegar a la carpeta de pdfs
    year = lista[0]
    municipio = lista[1]
    oficialia = lista[2]
    #Create new directory
    # Path
    path = os.path.join(destino, year)
    os.makedirs(path)
    path = os.path.join(path, str(municipio))
    os.makedirs(path)
    path = os.path.join(path, oficialia)
    os.makedirs(path)
    destino = path
    # Obtiene la lista de archivos en la carpeta de origen
    archivos = os.listdir(rutaPdf)

    # Recorre la lista de archivos y los copia a la carpeta de destino
    for archivo in archivos:
      ruta_archivo = os.path.join(rutaPdf, archivo)
      shutil.copy(ruta_archivo, destino)

    #change the operation status when finish and print by console
    ruta_entry.delete(0, END); #borra ruta en textEntry una vez finalizado el proceso
    changeStatus("                                             ")
    changeStatus("Finalizado")
    print("El origen es: ", rutaPdf)
    print('Los archivos han sido copiados con éxito')

# Create the main window
root = Tk()
root.title("Copy Files")

#Apariencia
mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
#root.geometry("600x400")
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

#Variable ruta that is used on the function
ruta = StringVar()
# entry textBox 
ruta_entry = ttk.Entry(mainframe, width=30, textvariable=ruta)
ruta_entry.grid(column=3, row=1, sticky=(W, E))

#Labels
ttk.Label(mainframe, text="Ruta Inicial", width=15).grid(column=1, row=1, sticky=W)
ttk.Label(mainframe, text="Status", width=15).grid(column=1, row=2, sticky=W)
#Button that calls the main function
ttk.Button(mainframe, text="Inciar", command=start_copy, width=30).grid(column=3, row=3, sticky=W)
changeStatus("Introduzca ruta inicial")

# size of principal rectangle
for child in mainframe.winfo_children(): 
    child.grid_configure(padx=5, pady=5)

# Run the main loop
root.mainloop()


 #1 borrar ruta cuando acabe proceso
 #2 click en boton y resetea estado