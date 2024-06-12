import os
import msvcrt
import time


nombre = []
apellido = []
cargo = []
sueldo_bruto = []

os.system("cls")
print(" Bienvenido a Plantilla de trabajadores")

while True:

    print ("""
    1. Registrar trabajador
    2. Listar los todos los trabajadores
    3. Imprimir planilla de sueldos
    4. Salir del Programa
           """)

    opc = int(input("seleccione una opcion: "))

    if opc ==1:
        
        nombre.append (input("ingrese el nombre de la persona: "))
        apellido.append (input("ingrese el apellido: "))
        cargo.append (input("ingrese el cargo: "))
        sueldo_bruto.append (input("ingrese el sueldo bruto: "))
    elif opc ==2:
        print("nombre y apellido: " (nombre, apellido))
    elif opc ==3:
        pass
    elif opc ==4:
        print("estamos para servirle, hasta luego")
        time.sleep(2)
        break
    else:
        print ("el numero de opcion que a elejido no concuerda vuelva a intentarlo.")
        time.sleep(2)
        continue
