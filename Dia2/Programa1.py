#1. Al inicio, el programa dará la bienvenida y explicará la naturaleza
#de la Secuencia de Fibonacci, donde solicitará al usuario ingresar
#un valor entero "n", representando hasta qué término de la secuencia 
#se generará. Aquí mostrará la secuencia de Fibonacci hasta el enésimo 
#término ingresado por el usuario. Luego, preguntará si el usuario desea 
#continuar o salir, donde si se decide salir, el programa se detendrá;
#de lo contrario, se repetirá el proceso.
print("Bienvenido a 'Adivina el número'!")
print('¡Hola! ¿Cómo te llamas?')
miNombre = input()
print('Bueno, ' + miNombre + ',A continoacion te explicare la sucesión de Fibonacci .')
print("¡Vamos a empezar!")
print("En matemática, la sucesión de Fibonacci se trata de una serie infinita\nde números naturales que empieza con un 0 y un 1 y continúa añadiendo \nnúmeros que son la suma de los dos anteriores: 0, 1, 1, 2, 3, 5")
print("¡Vamos a empezar!")
while True:
    num = int(input('Cuántos valores de la sucesión de Fibonacci deseas?: '))
    a, b = 0, 1
    for i in range(num):
        print(a, end=' ')
        a, b = b, a + b

    play_again = input('\n¿Quieres jugar de nuevo? (sí/no): ')
    if play_again.lower() != 'sí':
        break
