import json

large_file = "C:/Users/usuario/Desktop/programacion/Python_GarciaDiego/Dia11/largefile.json"

with open(large_file, encoding="utf-8") as archivo:
    datos = json.load(archivo)

# Función para mostrar el menú y realizar las operaciones CRUD
def menu():
    while True:
        print("\n--- MENÚ ---")
        print("1. Mostrar eventos")
        print("2. Crear evento")
        print("3. Actualizar evento")
        print("4. Eliminar evento")
        print("5. Salir")
        
        opcion = input("Seleccione una opción: ")
        nombres_eventos = {evento["id"] for evento in datos}  # Conjunto de nombres de eventos
        
        if opcion == "1":
            if datos:
                print("--- Eventos ---") 
                for i, evento in enumerate(datos, 1):
                    print(f"{i}. {evento['type']} - {evento['id']}")
            else:
                 print("No hay eventos para mostrar.")

        elif opcion == "2":
            id_evento = input("Ingrese el ID del evento: ")
            # Verificar si el evento ya existe
            if id_evento in nombres_eventos:
                print("¡El evento ya existe!")
            else:
                nombre = input("Ingrese el nombre del evento: ")
                nuevo_evento = {"type": nombre, "id": id_evento }
                datos.append(nuevo_evento)
                nombres_eventos.add(nombre)  # Agregar el nombre del evento al conjunto
                print("Evento creado exitosamente.")
             
        elif opcion == "3":
            if datos:
                id_actualizar = input("Ingrese el ID del evento a actualizar: ")
                for evento in datos:
                    if evento["id"] == id_actualizar:
                        nuevo_nombre = input("Ingrese el nuevo nombre del evento: ")
                        evento["type"] = nuevo_nombre
                        print("Evento actualizado exitosamente.")
                        break
                else:
                    print("El evento no existe.")
            else:
                print("No hay eventos para actualizar.")

        elif opcion == "4":
            if datos:
                id_eliminar = input("Ingrese el ID del evento a eliminar: ")
                for evento in datos:
                    if evento["id"] == id_eliminar:
                        datos.remove(evento)
                        nombres_eventos.remove(id_eliminar)
                        print("Evento eliminado exitosamente.")
                        break
                else:
                    print("El evento no existe.")
            else:
                print("No hay eventos para eliminar.")
                
        elif opcion == "5":
            # Guardar los datos en el archivo JSON antes de salir
            with open(large_file, 'w', encoding="utf-8") as file:
                json.dump(datos, file, indent=4)
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida. Por favor, seleccione una opción válida.")

# Llamada a la función del menú
menu()
