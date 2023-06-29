import os
import time
from funciones import *

menu = True
while menu: 
    os.system('cls')
    print('*   Auto Seguro   *')
    print('')
    print('1. Guardar datos de Vehiculo')
    print('2. Buscar vehiculo')
    print('3. Imprimir certificados ')
    print('4. Salir')
    opcion = int(input('ingrese una opción:\n'))
    if opcion > 0 and opcion < 5:
        if opcion == 1:
            print("*  Datos que desea guardar  *")
            print('')
            agregarDatos()
            time.sleep(1)           
        elif opcion == 2:
            print("*  Vehiculo a buscar  *")
            print('')
            buscarDato()
            time.sleep(1)
        elif opcion == 3:
            print("*  Certificado  *")
            print('')
            ImprimirCer()
        elif opcion == 4:
            op = int(input("esta seguro que desea salir?\n 1. SI\n 2. NO\n"))
            if op == 1:
                menu = False
                
print('*  Gracias por usar nuestro sistema  *')
print('*  Yurfran Uzcategui                 *')
print('*  Version 1                         *')