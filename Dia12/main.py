import json

def abrirArchivo():
    miJSON=[]
    with open('info.json','r') as openfile:
        miJSON= json.load(openfile)
    return miJSON

def guardarArchivo(miData):
    with open("info.json","w") as outfile:
        json.dump(miData,outfile)

def main():
    print("################")
    print("## PLATAFORMA DE GESTION ##")
    print("################")
    print("")
    print("Hola! Por favor escoge alguna de las opciones:\n1.Revisar estudiantes\n2.Modificar estudiante\n3.Crear grupo\n4.Crear estudiante\n5.Eliminar grupo\n6.Eliminar estudiante\n7.salir")
    opcion=int(input("Que opcion quiere elegir?: "))
    miInfo=[]
    if opcion == 1:
        miInfo=abrirArchivo()
        for grupo in miInfo:
            print("################")
            print(f"Grupo: {grupo['grupo']}")
            for estudiante in grupo['estudiantes']:
                print("################")
                print("ID:", estudiante["id"])
                print("Nombre:", estudiante["nombre"])
                print("Apellido:", estudiante["apellido"])
                print("Edad", estudiante["edad"])
                print("Fecha de Nacimiento (DD-MM-AAAA):", estudiante["fechaNacimiento"])
                print("Cédula:", estudiante["cedula"])
                print("E-mail:", estudiante["email"])
                print("GitHub:", estudiante["github"])
                print("################")
                print("")
    elif opcion == 2:
        miInfo=abrirArchivo()
        contador = 0
        for grupo in miInfo:
            print("################")
            print(f"Grupo: {grupo['grupo']}")
            for estudiante in grupo['estudiantes']:
                contador=contador+1
                print("################")
                print("ID:", estudiante["id"])
                print("Nombre:", estudiante["nombre"])
                print("Apellido:", estudiante["apellido"])
                print("Edad", estudiante["edad"])
                print("Fecha de Nacimiento (DD-MM-AAAA):", estudiante["fechaNacimiento"])
                print("Cédula:", estudiante["cedula"])
                print("E-mail:", estudiante["email"])
                print("GitHub:", estudiante["github"])
                print("################")
                print("")
        
        grupo_modificar = input("¿Qué grupo de estudiantes quieres modificar? ")
        for grupo in miInfo:
            if grupo["grupo"] == grupo_modificar:
                estudiante = int(input("¿Cuál número de identificación quieres modificar? "))
                print("¿Qué te gustaría cambiar del estudiante?\n1.ID\n2.Nombre\n3.Apellido\n4.Edad\n5.Fecha de Nacimiento\n6.Cédula\n7.Gmail\n8.GitHub")
                dato_cambiar = int(input("Que cambio deceas hacer?: "))
                if dato_cambiar == 1:
                    nuevo_id = input("Ingresa el nuevo ID: ")
                    grupo['estudiantes'][estudiante - 1]['id'] = nuevo_id
                elif dato_cambiar == 2:
                    nuevo_nombre = input("Ingresa el nuevo nombre: ")
                    grupo['estudiantes'][estudiante - 1]['nombre'] = nuevo_nombre
                elif dato_cambiar == 3:
                    nuevo_apellido = input("Ingresa el nuevo apellido: ")
                    grupo['estudiantes'][estudiante - 1]['apellido'] = nuevo_apellido
                elif dato_cambiar == 4:
                    nueva_edad = input("Ingresa la nueva edad: ")
                    grupo['estudiantes'][estudiante - 1]['edad'] = nueva_edad
                elif dato_cambiar == 5:
                    nueva_fecha = input("Ingresa la nueva fecha de nacimiento (DD-MM-AAAA): ")
                    grupo['estudiantes'][estudiante - 1]['fechaNacimiento'] = nueva_fecha
                elif dato_cambiar == 6:
                    nueva_cedula = input("Ingresa la nueva cédula: ")
                    grupo['estudiantes'][estudiante - 1]['cedula'] = nueva_cedula
                elif dato_cambiar == 7:
                    nuevo_email = input("Ingresa el nuevo email: ")
                    grupo['estudiantes'][estudiante - 1]['email'] = nuevo_email
                elif dato_cambiar == 8:
                    nuevo_github = input("Ingresa el nuevo GitHub: ")
                    grupo['estudiantes'][estudiante - 1]['github'] = nuevo_github
                    

        guardarArchivo(miInfo)
        print("Cambio realizado!")
        contador = 0
        for grupo in miInfo:
            print("################")
            print(f"Grupo: {grupo['grupo']}")
            for estudiante in grupo['estudiantes']:
                contador=contador+1
                print("################")
                print("ID:", estudiante["id"])
                print("Nombre:", estudiante["nombre"])
                print("Apellido:", estudiante["apellido"])
                print("Edad", estudiante["edad"])
                print("Fecha de Nacimiento (DD-MM-AAAA):", estudiante["fechaNacimiento"])
                print("Cédula:", estudiante["cedula"])
                print("E-mail:", estudiante["email"])
                print("GitHub:", estudiante["github"])
                print("################")
                print("")
main()