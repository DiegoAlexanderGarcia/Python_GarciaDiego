#aqui inicio la importacion de json para trabajar con python
import json

# Función para cargar los datos del archivo JSON
def cargar_datos():
    with open('largefile.json') as openfile:#abro el archivo 
        datos = json.load(openfile)#y le digo que los almacene en datos
    return datos

# Función para mostrar los eventos
def mostrar_eventos(eventos):
    for i, evento in enumerate(eventos):
        print(f"{i + 1}. ID: {evento['id']}, Tipo: {evento['type']}, Creado en: {evento['created_at']}")

# Función para crear un nuevo evento
def crear_evento(eventos):
    nuevo_evento = {
        "id": input("Ingrese el ID del nuevo evento: "),
        "type": input("Ingrese el tipo del nuevo evento: "),
        "created_at": input("Ingrese la fecha de creación del nuevo evento (en formato YYYY-MM-DDTHH:MM:SSZ): ")
    }
    eventos.append(nuevo_evento)
    print("Evento creado con éxito.")

    with open("eventos.json", "w") as outfile:
        json.dump(eventos, outfile)

# Función para actualizar un evento existente
def actualizar_evento(eventos):
    id_evento = input("Ingrese el ID del evento que desea actualizar: ")
    for evento in eventos:
        if evento['id'] == id_evento:
            evento['type'] = input("Ingrese el nuevo tipo del evento: ")
            evento['created_at'] = input("Ingrese la nueva fecha de creación del evento (en formato YYYY-MM-DDTHH:MM:SSZ): ")
            print("Evento actualizado con éxito.")
            return
    print("Evento no encontrado.")

# Función para eliminar un evento existente
def eliminar_evento(eventos):
    id_evento = input("Ingrese el ID del evento que desea eliminar: ")
    for evento in eventos:
        if evento['id'] == id_evento:
            eventos.remove(evento)
            print("Evento eliminado con éxito.")
            return
    print("Evento no encontrado.")

# Función principal
def main():
    eventos = cargar_datos()

    while True:
        print("\nMenú de Eventos:")
        print("1. Mostrar Eventos")
        print("2. Crear Evento")
        print("3. Actualizar Evento")
        print("4. Eliminar Evento")
        print("5. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            mostrar_eventos(eventos)
        elif opcion == "2":
            crear_evento(eventos)
        elif opcion == "3":
            actualizar_evento(eventos)
        elif opcion == "4":
            eliminar_evento(eventos)
        elif opcion == "5":
            break
        else:
            print("Opción no válida. Por favor, seleccione una opción válida.")

        with open('archivo.json', 'w') as f:
            json.dump(eventos, f, indent=4)

if __name__ == "__main__":
    main()
