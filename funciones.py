import time
datos = []

# def validar_patente(patente):
#     if len(patente) != 6:
#         return



def agregarDatos():
    tipo = input("Ingrese el tipo de vehiculo: ")
    
    patente = input("Ingrese La patente del vehiculo: ")
    # while not validar_patente(patente):
    #     print("Patente invalida. Intente nuevamente.")
    #     patente = input("Ingrese La patente del vehiculo: ")
    
    marca = input("Ingrese marca del vehiculo: ")
    # while len(marca) > 2:
    #         print("La marca debe tener al menos 2 caracteres")        
    #         marca = input("Ingrese marca: ")

    precio = int(input("Ingrese el precio del vehiculo: "))
    while precio < 5000000:
        print("El precio debe ser mayor a $5.000.000. Intente nuevamente.")
        precio = int(input("Ingrese el precio del vehiculo: "))
    multa = []
    multap = int(input('Ingrese valor de la multa: '))
    fecmulta = input("Ingrese la Fecha de la multa: ")
    ingmult = {
        'Multap': multap,
        'FecMulta': fecmulta
    }
    multa.append(ingmult)
    fecregistro = input('Fecha de ingreso: ')
    nom = input('Dueño del vehiculo: ')
    dato = {
        'Tipo': tipo,
        'Patente': patente,
        'Marca': marca,
        'Precio': precio,
        'Multa': multa,
        'Fecregistro': fecregistro,
        'Nombre': nom
    }
    datos.append(dato)
    print("Registro almacenado exitosamente.")
    time.sleep(1)


def buscarDato():
    patente = input("Ingrese la Patente a buscar: ")
    encontrado = False
    for dato in datos:
        if dato['Patente'] == patente:
            print("*  Información del Vehiculo  *")
            print("Patente:", dato['Patente'])
            print("Marca:", dato['Marca'])
            print("Precio:", "$",dato['Precio'])
            print("Multa:", dato['Multa'])
            print("Fecha de registro:", dato['Fecregistro'])
            print("Nombre:", dato['Nombre'])
            encontrado = True
            deseo = input('esta seguro que desea volver? \n')
            break
    if not encontrado:
        print("No se encontró ningun vehiculo con esa Patente.")


def ImprimirCer():
    patente = input("Ingrese la Patente de la cual quiere buscar certificado: ")
    encontrado = False
    for dato in datos:
        if dato['Patente'] == patente:
            print('*  Emision de contaminantes  *')
            print("Patente:", dato['Patente'])
            print("Nombre:", dato['Nombre'])
            print('')
            print('*  Anotaciones vigentes  *')
            print("Patente:", dato['Patente'])
            print("Nombre:", dato['Nombre'])
            print('')
            print('*  Emision de multas  *')
            print("Patente:", dato['Patente'])
            print("Nombre:", dato['Nombre'])
            print("Multa:", dato['Multa'])
            encontrado = True
            # time.sleep(4)
            deseo = input('esta seguro que desea volver? \n')
    if not encontrado:
        print("No se encontró ningun vehiculo con esa Patente.")
        time.sleep(2)