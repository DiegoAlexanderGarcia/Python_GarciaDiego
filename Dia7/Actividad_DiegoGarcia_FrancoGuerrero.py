##diccionario de tienda

print("\nhola bienvenido a nuestra tienda online")##saludo al usuario
print("")


productoP={ 
   "0100":{"nombre": "carne","precio":15000},##diccionario para el stock de productos
   "0500":{"nombre": "pollo","precio":14000},
   "2230":{"nombre": "pescado","precio":11000},}

carrito={}##para almacenar los productos del carrito
##mustro al usuario el catalogo de productos
print("catalogo de productos")
print("")
for id_productos, producto in productoP.items():
    print(f"{id_productos}:{producto["nombre"]} - ${producto["precio"]}")##muestro 


def carrito_compras():
    id_productos = input("dame el id del producto que vas a llevar: ")##pido el id del producto
    if id_productos in productoP:##si el id que dio esta en productos entonces
        cantidad=int(input("cuantos kilos vas a llevar: "))##cuanto va a llevar
        if cantidad > 0 :##si cantidad es mayo a 0 entonces
            if id_productos in carrito:##si el id del producto esta en el carrito
                carrito[id_productos]+=cantidad##el producto se almacena en el carrito mas la cantidad ingresada
            else:
                carrito[id_productos]=cantidad
                print("producto agregado al carrito")##si ingreso un producto valido le muestro que se agrego al carrito
        else:
            print("cantidad debe ser mayor a 0")##si no escribe un numero mayor a 0 le escribo que ingrese
    else:
        print("producto no encontrado")##si no escribe el id de un produvto que este en la lista

def mostrarCarrito():##defino la funcion
    print("cosas que lleva en el carrito")##le digo cuantas cosas que lleva
    total=0##le muestro cuantas cosas lleva en el carrito 
    for id_productos, cantidad in carrito.items():##creo un bucle fo que recorra que recorra
        producto=productoP[id_productos]
        totalMedio= cantidad * producto["precio"]
        total += totalMedio
        print(f"{producto["nombre"]}- cantidad:{cantidad}-totalMedio: ${totalMedio}")
    print(f"total de compra: ${total}")

def final_compra():
    mostrarCarrito()
    print("gracias por hacer su compra")
    carrito.clear()
    salir()

def salir():
    print("adio, que tenga buen dia")
    exit()
    
espe=True
while espe==True:
    menu= f"""
    1.agregar productos al carrito
    2.ver contenido del carrito
    3.calcular el total de compra
    4.finalizar compra
    5.salir del programa
    """
    print(menu)
    opcion=input("que opcion desea realizar: ")

    if opcion== "1":
        carrito_compras()
    elif opcion=="2":
        mostrarCarrito()
    elif opcion=="3":
        mostrarCarrito()
    elif opcion=="4":
        final_compra()
    elif opcion=="5":
        salir()
    else:
        print("por favor seleccione una opcion valida")