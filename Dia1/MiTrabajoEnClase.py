#------------------------------
#-----Dia 1 CHEAT SHEET PYTHON-----
#------------------------------

#Imprimir Hola Mundo
print("Hola Mundoooooooooooo")

#Datos Primitivos

#Numero
numerito = 1 #nombreVariable = valor
print(numerito) #imprimir(variable)
print(type(numerito)) #imprimir(tipo(variable))

#Decimal
numeritoDecimal = 1.1
print(numeritoDecimal)
print(type(numeritoDecimal))

#Booleano
miBooleanito = True
print(miBooleanito)
print(type(miBooleanito))

#Cadena de texto
texto = "MI TIBU"
print(texto)
print(type(texto))

#Ingresa por teclado la infomarcion(input)
#ingreso
numeroF = input("ingrese tu numero favorito ")

numeroF =(int(numeroF))
print("seguro que tu numero favorto es",numeroF,"si o no")

print("si",numeroF,"es mi numero favorito")

x = "mucho gusto"

def myfunc():
  print("Soy Diego " + x)

myfunc()
#Conversion de tipos de variable (tipos de variables primitivos)
#comvertir de cadena a entero
Num_entero = int("10")
print(Num_entero)
print(type(Num_entero))
#comvertir de cadena a flotante
Num_flot=float("5.0")
print(Num_flot)
print(type(Num_flot))
#comvertir de entero a cadena
NCadena=str(16)
print(NCadena)
print(type(NCadena))
#Bucles For y While
#Bucle for 
for s in range(4):
  print(s)
#Bucle While
contador=0
while contador < 4:
  print(contador)
  contador +=1

#Funciones
#-función sin parámetros o retorno 
def diHola():
  print("Hello!")

diHola()  # llamada a la función, 'Hello!' se muestra en la consola
#-funcion con parametros y sin rotorno
def holaConNombre(name):
  print("Hello " + name + "!")

holaConNombre("Diego")  # llamada a la función, 'Hello Ada!' se muestra en la consola
#-función sin parametro y con retorno

def obtener_saludo():
  return "¡holaaaaa!"

saludo= obtener_saludo()

print(saludo," como esta")

def obtener_numero():
  return "16"
#llamo la fncion sin parametros
print("el numero obtenido es:",obtener_numero(),)


#-función con parametros y con retono


def multiplicar(a, b):
  resultado= a* b
  return resultado

resultado_multiplica = multiplicar(2, 4)  # muestra 15 en la consola

print("el resultado es: ", resultado_multiplica,)
#actualizar
#Desarrollado por Garcia Rodriguez - C.C 1.093.780.794
