import shutil
import os
from tkinter import *
from tkinter import ttk

listaMunicipios = 'AHUALULCO','ALAQUINES','AQUISMON','ARMADILLO_DE_LOS_INFANTE','CARDENAS','CATORCE','CEDRAL','CERRITOS','CERRO_DE_SAN_PEDRO','CIUDAD_DEL_MAIZ','CIUDAD_FERNANDEZ','TANCANHUITZ','CIUDAD_VALLES','COXCATLAN','CHARCAS','EBANO','GUADALCAZAR','HUEHUETLAN','LAGUNILLAS','MATEHUALA','MEXQUITIC_DE_CARMONA','MOCTEZUMA','RAYÓN','RIOVERDE','SALINAS','SAN_ANTONIO','SAN_CIRO_DE_ACOSTA','SAN_LUIS_POTOSÍ','SAN_MARTÍN_CHALCHICUAUTLA','SAN_NICOLAS_TOLENTINO','SANTA_CATARINA','SANTA_MARIA_DEL_RIO','SANTO_DOMINGO','SAN_VICENTE_TANCUAYALAB','SOLEDAD_DE_GRACIANO_SANCHEZ','TAMASOPO','TAMAZUNCHALE','TAMPACAN','TAMPAMOLON_CORONA','TAMUIN','TANLAJAS','TANQUIAN_DE_ESCOBEDO','TIERRA_NUEVA','VANEGAS','VENADO','VILLA_DE_ARRIAGA','VILLA_DE_GUADALUPE','VILLA_DE_LA_PAZ','VILLA_DE_RAMOS','VILLA_DE_REYES','VILLA_HIDALGO','VILLA_JUAREZ','AXTLA_DE_TERRAZAS','XILITLA','ZARAGOZA','VILLA_DE_ARISTA','MATLAPA','EL_NARANJO'

print(listaMunicipios[57])
#buscar = input("Ingresa la ruta del archivo: ")
buscar = r"D:\1955\RAYON01_1955"

    

info = buscar.split("\\")
infoCarpetas = info[-1]
print(infoCarpetas)

years = infoCarpetas.split("_")
year = years[-1]
oficialia = years[-2]
numeroOficialia = oficialia[-2:]
print(numeroOficialia)
print(oficialia)
print(year)

for word in listaMunicipios:
    if word in infoCarpetas:
        print("Encontrado")
        break
#listaMunicipios.find("TAMPAMOLON")