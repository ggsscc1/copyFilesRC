listaMunicipios = 'AHUALULCO','ALAQUINES','AQUISMON','ARMADILLO_DE_LOS_INFANTE','CARDENAS','CATORCE','CEDRAL','CERRITOS','CERRO_DE_SAN_PEDRO','CIUDAD_DEL_MAIZ','CIUDAD_FERNANDEZ','TANCANHUITZ','CIUDAD_VALLES','COXCATLAN','CHARCAS','EBANO','GUADALCAZAR','HUEHUETLAN','LAGUNILLAS','MATEHUALA','MEXQUITIC_DE_CARMONA','MOCTEZUMA','RAYON','RIOVERDE','SALINAS','SAN_ANTONIO','SAN_CIRO_DE_ACOSTA','SAN_LUIS_POTOSÍ','SAN_MARTIN_CHALCHICUAUTLA','SAN_NICOLAS_TOLENTINO','SANTA_CATARINA','SANTA_MARIA_DEL_RIO','SANTO_DOMINGO','SAN_VICENTE_TANCUAYALAB','SOLEDAD_DE_GRACIANO_SANCHEZ','TAMASOPO','TAMAZUNCHALE','TAMPACAN','TAMPAMOLON_CORONA','TAMUIN','TANLAJAS','TANQUIAN_DE_ESCOBEDO','TIERRA_NUEVA','VANEGAS','VENADO','VILLA_DE_ARRIAGA','VILLA_DE_GUADALUPE','VILLA_DE_LA_PAZ','VILLA_DE_RAMOS','VILLA_DE_REYES','VILLA_HIDALGO','VILLA_JUAREZ','AXTLA_DE_TERRAZAS','XILITLA','ZARAGOZA','VILLA_DE_ARISTA','MATLAPA','EL_NARANJO'

#print(listaMunicipios[57])
#buscar = input("Ingresa la ruta del archivo: ")
#buscar = r"D:\1955\SOLEDAD01_1955"

def manejaRutaOrigen(buscar):
    #desglosa ruta de disco y extrae el nombre del municipio, oficialia y año
    info = buscar.split("\\")
    municipioOfiAño = info[-1]
    print(municipioOfiAño)

    #extrae el año del municipio y la oficialia
    years = municipioOfiAño.split("_")
    year = years[-1]
    #extrae el municipio y la oficialia del conjunto
    municipioOfi = years[-2]
    municipio = municipioOfi[:-2]
    numeroOficialia = municipioOfi[-2:]
    print(municipio)
    print(numeroOficialia)
    #print(oficialia)
    print(year)

    #asigna un numero al municipio para crear la carpeta corresponiente
    valorMunicipio = 0
    for word in listaMunicipios:
        valorMunicipio += 1
        print(valorMunicipio)
        if municipio in word:
            print("Encontrado")
            break
    
    lista = [year, valorMunicipio, numeroOficialia]
    return lista
