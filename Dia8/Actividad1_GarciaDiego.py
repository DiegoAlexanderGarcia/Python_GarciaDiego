class UsuarioPYTimes:
    def __init__(self, nombre, saldo_inicial, precio_suscripcion=50):
        self.nombre = nombre
        self.precio_suscripcion = precio_suscripcion
        self.años_suscripcion = []  # Lista para almacenar los años de suscripción
        self.saldo_cuenta = saldo_inicial  # Saldo inicial de la cuenta
        print(f"¡Bienvenido(a) {self.nombre}! Se ha creado una nueva cuenta con un saldo inicial de ${self.saldo_cuenta}.")

    def agregar_suscripcion(self, año):
        self.años_suscripcion.append(año)
        print(f"Se ha añadido la suscripción para el año {año}.")

    def suscribirse(self, año):
        if self.saldo_cuenta >= self.precio_suscripcion:
            self.saldo_cuenta -= self.precio_suscripcion
            self.agregar_suscripcion(año)
            print(f"¡Éxito! {self.nombre} se ha suscrito para el año {año}.")
        else:
            print(f"Error: Saldo insuficiente. Saldo actual: ${self.saldo_cuenta}")

    def depositar(self, monto):
        self.saldo_cuenta += monto
        print(f"Se ha depositado ${monto} en la cuenta de {self.nombre}. Saldo actual: ${self.saldo_cuenta}")

    def comprar_suscripcion_regalo(self, otro_usuario, año):
        if self.saldo_cuenta >= otro_usuario.precio_suscripcion:
            self.saldo_cuenta -= otro_usuario.precio_suscripcion
            otro_usuario.agregar_suscripcion(año)
            print(f"¡Éxito! Se compró una suscripción de regalo para {otro_usuario.nombre} para el año {año}.")
        else:
            print(f"Error: Saldo insuficiente para comprar una suscripción de regalo para {otro_usuario.nombre}. Saldo actual: ${self.saldo_cuenta}")

    def obtener_precio_suscripcion(self):
        return self.precio_suscripcion

    def obtener_nombre(self):
        return self.nombre

# Función para solicitar nombre y saldo inicial al usuario
def obtener_informacion_usuario():
    nombre = input("Por favor, ingresa tu nombre: ")
    saldo_inicial = float(input("Por favor, ingresa tu saldo inicial: $"))
    return nombre, saldo_inicial

# Ejemplo de uso
informacion_usuario = obtener_informacion_usuario()
usuario = UsuarioPYTimes(*informacion_usuario)

usuario.depositar(100)
usuario.suscribirse(2024)


    
