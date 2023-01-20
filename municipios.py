""" listaMunicipios = 'AHUALULCO','ALAQUINES','AQUISMON','ARMADILLO_DE_LOS_INFANTE','CARDENAS','CATORCE','CEDRAL','CERRITOS','CERRO_DE_SAN_PEDRO','CIUDAD_DEL_MAIZ','CIUDAD_FERNANDEZ','TANCANHUITZ','CIUDAD_VALLES','COXCATLAN','CHARCAS','EBANO','GUADALCAZAR','HUEHUETLAN','LAGUNILLAS','MATEHUALA','MEXQUITIC_DE_CARMONA','MOCTEZUMA','RAYON','RIOVERDE','SALINAS','SAN_ANTONIO','SAN_CIRO_DE_ACOSTA','SAN_LUIS_POTOSI','SAN_MARTIN_CHALCHICUAUTLA','SAN_NICOLAS_TOLENTINO','SANTA_CATARINA','SANTA_MARIA_DEL_RIO','SANTO_DOMINGO','SAN_VICENTE_TANCUAYALAB','SOLEDAD_DE_GRACIANO_SANCHEZ','TAMASOPO','TAMAZUNCHALE','TAMPACAN','TAMPAMOLON_CORONA','TAMUIN','TANLAJAS','TANQUIAN_DE_ESCOBEDO','TIERRA_NUEVA','VANEGAS','VENADO','VILLA_DE_ARRIAGA','VILLA_DE_GUADALUPE','VILLA_DE_LA_PAZ','VILLA_DE_RAMOS','VILLA_DE_REYES','VILLA_HIDALGO','VILLA_JUAREZ','AXTLA_DE_TERRAZAS','XILITLA','ZARAGOZA','VILLA_DE_ARISTA','MATLAPA','EL_NARANJO' """

listaMunicipios = 'AHUALULCO','ALAQUINES','AQUISMON','ARMADILLO DE LOS INFANTE','CARDENAS','CATORCE','CEDRAL','CERRITOS','CERRO DE SAN PEDRO','CIUDAD DEL MAIZ','CIUDAD FERNANDEZ','TANCANHUITZ','CIUDAD VALLES','COXCATLAN','CHARCAS','EBANO','GUADALCAZAR','HUEHUETLAN','LAGUNILLAS','MATEHUALA','MEXQUITIC DE CARMONA','MOCTEZUMA','RAYON','RIOVERDE','SALINAS','SAN ANTONIO','SAN CIRO DE ACOSTA','SAN LUIS POTOSI','SAN MARTIN CHALCHICUAUTLA','SAN NICOLAS TOLENTINO','SANTA CATARINA','SANTA MARIA DEL RIO','SANTO DOMINGO','SAN VICENTE TANCUAYALAB','SOLEDAD DE GRACIANO SANCHEZ','TAMASOPO','TAMAZUNCHALE','TAMPACAN','TAMPAMOLON CORONA','TAMUIN','TANLAJAS','TANQUIAN DE ESCOBEDO','TIERRA NUEVA','VANEGAS','VENADO','VILLA DE ARRIAGA','VILLA DE GUADALUPE','VILLA DE LA PAZ','VILLA DE RAMOS','VILLA DE REYES','VILLA HIDALGO','VILLA JUAREZ','AXTLA DE TERRAZAS','XILITLA','ZARAGOZA','VILLA DE ARISTA','MATLAPA','EL NARANJO'
#print(listaMunicipios[57])
#buscar = input("Ingresa la ruta del archivo: ")
#buscar = r"D:\1955\SOLEDAD01_1955"

def manejaRutaOrigen(buscar):
   
    #desglosa ruta de disco y extrae el nombre del municipio, oficialia y año
    info = buscar.split("\\")
    municipioOfiAño = info[-1]
    print(municipioOfiAño)

    #extrae el AÑO del municipio y la oficialia
    years = municipioOfiAño.split("_")
    year = years[-1]
    #extrae el municipio y la oficialia
    municipioOfi = years[:-1]
    #junta los elementos de la lista para formar el municipio
    municipio = ""
    for elemento in municipioOfi :
        if municipio != "":
            municipio = municipio + " " + elemento
        else:
            municipio = elemento
    #Obtiene la oficialia de la cadena municipio
    numeroOficialia = municipio[-2] + municipio[-1]
    #obtiene el municipio del conjunto con oficialia
    municipio = municipio[:-2]
    #municipioOfi = while(municipioOfi[n])
    print(numeroOficialia)
    print(year)
    print(municipio)
   

    #asigna un numero al municipio para crear la carpeta corresponiente
    valorMunicipio = 0
    for word in listaMunicipios:
        valorMunicipio += 1
        print(valorMunicipio)
        if word in municipio:
            print("Encontrado")
            break
    
    lista = [year, valorMunicipio, numeroOficialia]
    return lista

#manejaRutaOrigen(buscar)


