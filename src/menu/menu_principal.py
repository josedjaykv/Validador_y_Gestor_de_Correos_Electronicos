import sys

def mostrar_menu():
   #usar un bucle while para mostrar el menu
   while True:
    print("1. Registrar correo")
    print("2. ver correos registrados")
    print("3. Buscar correo")
    print("4. Salir")
    opcion = input("Seleccione una opción: ")
    ejecutar_opcion(opcion)

def ejecutar_opcion(opcion):
    if opcion == "1":
        registrar_correo()
    elif opcion == "2":
        ver_correos()
    elif opcion == "3":
        buscar_correo()
    elif opcion == "4":
        print("Saliendo del programa...")
        sys.exit()
    else:
        print("Opción inválida")

def registrar_correo():
    print("Registrar correo")

def ver_correos():
    print("Ver correos")

def buscar_correo():
    print("Buscar correo")
    
