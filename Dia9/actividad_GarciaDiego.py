cart=[]

def agregar_prod (nombre, precio, cantidad):
    prod = {"nombre": nombre,"precio":precio,"cantidad":cantidad}
    cart.append(prod)
nombre=input("imgresa el nombre del producto: ")
precio=int(input("ingresa el precio del producto: "))
cantidad=int(input("ingresa la cantidad del producto: "))


def mostrar_carrito ():
    print("almacen del carrito") 
    for prod in cart:
        print(f"{prod['nombre']} ${prod['precio']} x {prod['cantidad']}")
        


mostrar_carrito()