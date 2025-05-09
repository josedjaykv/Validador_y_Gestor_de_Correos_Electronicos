import sys
from services.correo_service import CorreoService


#mostrar el menu principal
def mostrar_menu():
    while True:
        print("\n=== MENÚ PRINCIPAL ===")
        print("1. Registrar correo")
        print("2. Ver correos registrados")
        print("3. Buscar correo")
        print("4. Salir")
        opcion = input("Seleccione una opción: ")
        ejecutar_opcion(opcion)

#ejecutar la opcion seleccionada
def ejecutar_opcion(opcion):
    if opcion == "1":
        menu_registrar_correo()
    elif opcion == "2":
        menu_ver_correos()
    elif opcion == "3":
        menu_buscar_correo()
    elif opcion == "4":
        print("Saliendo del programa...")
        sys.exit()
    else:
        print("Opción inválida")
'''
cuando se selecciona la opcion 1: accede a registrar correo el cual es un metodo de la clase 
CorreoService el cual se rige por la clase Correo, la cual tiene un metodo para validar el correo
asi como un metodo para clasificar el correo como estudiante o docente

finalmente se retorna un true o false si el correo es valido o no
y se almacena en la variable correo que es una lista de correos
ubicada en la clase CorreoService
'''

#seccion de menus
def menu_registrar_correo():
    while True:
        print("\n=== REGISTRAR CORREO ===")
        print("1. Ingresar nuevo correo")
        print("2. Volver al menú principal")
        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
            registrar_correo()
        elif opcion == "2":
            return
        else:
            print("Opción inválida")

def menu_ver_correos():
    while True:
        print("\n=== VER CORREOS ===")
        print("1. Mostrar todos los correos")
        print("2. Mostrar correos de estudiantes")
        print("3. Mostrar correos de docentes")
        print("4. Volver al menú principal")
        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
            ver_correos()
        elif opcion == "2":
            ver_correos_estudiantes()
        elif opcion == "3":
            ver_correos_docentes()
        elif opcion == "4":
            return
        else:
            print("Opción inválida")

def menu_buscar_correo():
    while True:
        print("\n=== BUSCAR CORREO ===")
        print("1. Buscar por dirección")
        print("2. Buscar por dominio")
        print("3. Volver al menú principal")
        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
            buscar_por_direccion()
        elif opcion == "2":
            buscar_por_dominio()
        elif opcion == "3":
            return
        else:
            print("Opción inválida")

#seccion de metodos para registrar correo, ver correos, ver correos de estudiantes y ver correos de docentes

def registrar_correo():
    print("\n=== REGISTRAR NUEVO CORREO ===")
    direccion = input("Ingrese el correo electrónico: ").strip()
    
    if not direccion:
        print("Error: No se ingresó ningún correo")
        return
        
    if CorreoService.registrar_correo(direccion):
        print("\nCorreo registrado exitosamente")
    else:
        print("\nNo se pudo registrar el correo")

def ver_correos():
    correos = CorreoService.obtener_correos()
    if not correos:
        print("No hay correos registrados")
        return
    
    print("\n=== CORREOS REGISTRADOS ===")
    for correo in correos:
        print(correo)

def ver_correos_estudiantes():
    correos = CorreoService.obtener_por_clasificacion("estudiante")
    if not correos:
        print("No hay correos de estudiantes registrados")
        return
    
    print("\n=== CORREOS DE ESTUDIANTES ===")
    for correo in correos:
        print(correo)

def ver_correos_docentes():
    correos = CorreoService.obtener_por_clasificacion("docente")
    if not correos:
        print("No hay correos de docentes registrados")
        return
    
    print("\n=== CORREOS DE DOCENTES ===")
    for correo in correos:
        print(correo)

def buscar_por_direccion():
    direccion = input("Ingrese la dirección de correo a buscar: ")
    correos = CorreoService.buscar_por_direccion(direccion)
    if correos:
        print("\nCorreos encontrados:")
        for correo in correos:
            print("%s - %s" % (correo.direccion, correo.clasificacion))
    else:
        print("No se encontró ningún correo con esa dirección")

def buscar_por_dominio():
    dominio = input("Ingrese el dominio a buscar (ej: utv.edu.co): ")
    correos = CorreoService.buscar_por_dominio(dominio)
    if correos:
        print(f"\nCorreos encontrados con dominio '{dominio}':")
        for correo in correos:
            print(correo)
    else:
        print(f"No se encontraron correos con el dominio '{dominio}'")

if __name__ == "__main__":
    mostrar_menu()
    
