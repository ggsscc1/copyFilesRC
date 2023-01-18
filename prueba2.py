import shutil
import os
from tkinter import *
from tkinter import ttk

listaMunicipios = 'AHUALULCO','ALAQUINES','AQUISMON','ARMADILLO_DE_LOS_INFANTE','CARDENAS','CATORCE','CEDRAL','CERRITOS','CERRO_DE_SAN_PEDRO','CIUDAD_DEL_MAIZ','CIUDAD_FERNANDEZ','TANCANHUITZ','CIUDAD_VALLES','COXCATLAN','CHARCAS','EBANO','GUADALCAZAR','HUEHUETLAN','LAGUNILLAS','MATEHUALA','MEXQUITIC_DE_CARMONA','MOCTEZUMA','RAYÓN','RIOVERDE','SALINAS','SAN_ANTONIO','SAN_CIRO_DE_ACOSTA','SAN_LUIS_POTOSÍ','SAN_MARTÍN_CHALCHICUAUTLA','SAN_NICOLAS_TOLENTINO','SANTA_CATARINA','SANTA_MARIA_DEL_RIO','SANTO_DOMINGO','SAN_VICENTE_TANCUAYALAB','SOLEDAD_DE_GRACIANO_SANCHEZ','TAMASOPO','TAMAZUNCHALE','TAMPACAN','TAMPAMOLON_CORONA','TAMUIN','TANLAJAS','TANQUIAN_DE_ESCOBEDO','TIERRA_NUEVA','VANEGAS','VENADO','VILLA_DE_ARRIAGA','VILLA_DE_GUADALUPE','VILLA_DE_LA_PAZ','VILLA_DE_RAMOS','VILLA_DE_REYES','VILLA_HIDALGO','VILLA_JUAREZ','AXTLA_DE_TERRAZAS','XILITLA','ZARAGOZA','VILLA_DE_ARISTA','MATLAPA','EL_NARANJO'

#print(listaMunicipios[57])

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
    directory = "ihritik"
    
    for word in listaMunicipios:
      if word in origen:
          print("Encontrado")
          break


    #Create new directory
    # Path
    path = os.path.join(destino, directory)
    os.makedirs(path)

    # Obtiene la lista de archivos en la carpeta de origen
    archivos = os.listdir(origen)

    # Recorre la lista de archivos y los copia a la carpeta de destino
    for archivo in archivos:
      ruta_archivo = os.path.join(origen, archivo)
      shutil.copy(ruta_archivo, destino)

    #change the operation status when finish and print by console
    ruta_entry.delete(0, END); #borra ruta en textEntry una vez finalizado el proceso
    changeStatus("                                             ")
    changeStatus("Finalizado")
    print("El origen es: ", origen)
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