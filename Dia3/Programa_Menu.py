print("Holaaaa....")
nombre = input("Por favor, dime tu nombre: ")

while True:  # Bucle externo para elegir nuevamente las opciones del menú
    menu = f"""
    Te doy la bienvenida, {nombre}.  
    Estás iniciando un programa en el que tienes dos opciones para entrar en dos aplicaciones, cada una con función:

    La opción 1 es un programa cuyo objetivo es determinar si un número, el cual puedes elegir, es primo.
    ¿Qué es un número primo?
    Un número primo es aquel que solo es divisible por 1 y por sí mismo.
    Si no deseas ejecutar el programa, tendrás la opción de volver a elegir otra opción para que elijas la opción 2 o que finalices el programa.

    La opción 2 implementa un generador de contraseñas seguras que permite al usuario especificar la longitud de la contraseña y decidir si desea incluir mayúsculas, minúsculas, caracteres alfanuméricos y símbolos.
    Si no deseas ejecutar el programa, tendrás la opción de volver a elegir otra opción para que elijas la opción 1 o que finalices el programa.
    """

    print(menu)

    opcion = input("Por favor, elige una opción (1/2) o presiona 's' para salir: ")

    if opcion == "s":
        print("¡Adiós!")
        break

    if opcion == "1" or opcion == "2":
        while True:
            menu_opcion = ""
            if opcion == "1":
                menu_opcion = "Determinar si un número es primo"
            elif opcion == "2":
                menu_opcion = "Generar una contraseña segura"

            sub_menu = f"""
            Opción 1: {menu_opcion}.
            Opción 2: Explicar la funcionalidad del programa y volver a empezar.
            Opción 3: Volver al menú principal.
            """
            print(sub_menu)
            sub_opcion = input("Por favor, ingresa una opción: ")

            if sub_opcion == "1":
                if opcion == "1":
                    def es_primo(numero):
                        if numero <= 1:
                            return False
                        for i in range(2, int(numero ** 0.5) + 1):
                            if numero % i == 0:
                                return False
                        return True

                    numero = int(input("Por favor, ingresa un número para verificar si es primo: "))
                    if es_primo(numero):
                        print(f"El número {numero} es primo.")
                    else:
                        print(f"El número {numero} no es primo.")
                elif opcion == "2":
                    # Código para generar contraseña segura
                    import random
                    import string

                    def generar_contrasena(longitud, incluir_mayusculas=True, incluir_minusculas=True, incluir_numeros=True, incluir_simbolos=True):
                    caracteres = ""
                    if incluir_mayusculas:
                        caracteres += string.ascii_uppercase
                    if incluir_minusculas:
                        caracteres += string.ascii_lowercase
                    if incluir_numeros:
                        caracteres += string.digits
                    if incluir_simbolos:
                        caracteres += string.punctuation

                    contrasena = ''.join(random.choice(caracteres) for _ in range(longitud))
                    return contrasena

                    longitud = int(input("Ingrese la longitud de la contraseña: "))
                    incluir_mayusculas = input("¿Desea incluir mayúsculas? (s/n): ").lower() == "s"
                    incluir_minusculas = input("¿Desea incluir minúsculas? (s/n): ").lower() == "s"
                    incluir_numeros = input("¿Desea incluir números? (s/n): ").lower() == "s"
                    incluir_simbolos = input("¿Desea incluir símbolos? (s/n): ").lower() == "s"

                    contrasena_generada = generar_contrasena(longitud, incluir_mayusculas, incluir_minusculas, incluir_numeros, incluir_simbolos)
                    print(f"Contraseña generada: {contrasena_generada}")
                    pass
            elif sub_opcion == "2":
                print("Explicación del programa...")
                break
            elif sub_opcion == "3":
                break
            else:
                print("Opción no válida. Por favor, elige una opción válida (1/2/3).")

    elif opcion == "s":
        print("¡Adiós!")
        break
    else:
        print("Opción no válida. Por favor, elige una opción válida (1/2/s).")