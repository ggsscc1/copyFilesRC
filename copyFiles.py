import shutil
import os

# Establece la ruta de la carpeta de origen y la ruta de la carpeta de destino
#origen = r'C:\Users\24\Desktop\copy files RC python\origen'
#destino = r'C:\Users\24\Desktop\copy files RC python\destino'
origen = r'C:\Users\Administrador\Desktop\PRUEBAS_PYTON\origen'
destino = r'C:\Users\Administrador\Desktop\PRUEBAS_PYTON\destino'



# Obtiene la lista de archivos en la carpeta de origen
archivos = os.listdir(origen)

# Recorre la lista de archivos y los copia a la carpeta de destino
for archivo in archivos:
  ruta_archivo = os.path.join(origen, archivo)
  shutil.copy(ruta_archivo, destino)

print('Los archivos han sido copiados con éxito')
