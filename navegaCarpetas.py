import os

#Sorigen  = input("Introduce la ruta de la carpeta de origen: ")

#Funcion que navega en las carpetas
def navegacionCarpetas(origen):
  #lista los archivos dentro de la ruta origen dada
  listaDirectorios = os.listdir(origen)
  #imprime el primer archivo de la lista
  print('los archivos son: ', listaDirectorios[0])
  #junta la ruta origen con el primer archivo de la lista para entrar en esa ruta
  path = os.path.join(origen, listaDirectorios[0])
  print("la ruta actual es: ", path)
  #navega en las carpetas con el path creado
  os.chdir(path)
  #os.mkdir('ihritik')
  #manejaRutaOrigen(origen)


#Funcion para navegar entre carpetas FUNCIONAL
def navegacionCarpeta(origen):
  while True:
        print("primero")
        for folder in os.listdir(origen):
            #print(folder)
            #print("segundo")
            
            #auxiliar para regresar ruta original en caso de que no sea una carpeta
            auxi = origen
            origen = os.path.join(origen, folder)
            #si la ruta es un directorio
            if os.path.isdir(origen):
                print(origen)
                
                print('tercero')
                if folder == 'Pdf':
                    print("Pdf encontrado")
                
                break
            else: origen = auxi
        else:
            print("quinto")
            print(origen)
            return origen
    
#navegacionCarpeta(origen)