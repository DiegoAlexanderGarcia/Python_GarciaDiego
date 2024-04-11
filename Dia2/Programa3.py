import random

def jugar():
    # Explicación del juego
    print("Bienvenido a 'Adivina el número'!")
    print('¡Hola! ¿Cómo te llamas?')
    miNombre = input()
    print('Bueno, ' + miNombre + ', estoy pensando en un número entre 1 y 100.')
    print("El objetivo del juego es adivinar un número secreto.")
    print("Después de cada intento, recibirás una retroalimentación para ayudarte.")
    print("¡Vamos a empezar!")

    # Generar un número secreto aleatorio entre 1 y 100
    numero_secreto = random.randint(1, 100)

    # Solicitar la entrada del jugador
    intentos = 0
    intentos_maximos = 10
    adivinado = False

    # Bucle principal del juego
    while not adivinado and intentos < intentos_maximos:
        suposicion = input("Ingresa tu suposición (entre 1 y 100): ")
        intentos += 1
        # Validación de entrada
        if not suposicion.isdigit():
            print("Por favor, ingresa un número válido.")
            print(f"Intentos realizados: {intentos}")
            continue
        
        suposicion = int(suposicion)
        
        # Validación de rango
        if suposicion < 1 or suposicion > 100:
            print("El número debe estar en el rango de 1 a 100.")
            print(f"Intentos realizados: {intentos}")
            continue
        

        # Comparación y retroalimentación
        if suposicion < numero_secreto:
            print("Demasiado bajo. ¡Intenta nuevamente!")
        elif suposicion > numero_secreto:
            print("Demasiado alto. ¡Intenta nuevamente!")
        else:
            print(f"¡Felicidades! ¡Adivinaste el número en {intentos} intentos!")
            adivinado = True

        # Contador de intentos
        print(f"Intentos realizados: {intentos}")

    # Finalización del juego
    if not adivinado:
        print(f"¡Agotaste tus {intentos_maximos} intentos! El número secreto era {numero_secreto}.")
        
    jugar_nuevamente = input("¿Deseas jugar nuevamente? (sí/no): ")
    
    if jugar_nuevamente.lower() == 'si':
        jugar()
    else:
        print("Gracias por jugar. ¡Hasta la próxima!")

# Iniciar el juego
jugar()
