tareas = []

def mostrar_tareas():
    if not tareas:
        print("No hay tareas pendientes")
    else:
        print("Tareas pendientes:")
        for i, tarea in enumerate(tareas, 1):
            print(f"{i}. {tarea}")

def agregar_tareas():
    tarea = input("Agrega una tarea: ")
    tareas.append(tarea)
    print(f"Tarea '{tarea}' ha sido agregada")

def borrar_tareas():
    mostrar_tareas()
    try:
        num_tarea = int(input("Ingresa el número de la tarea a eliminar: "))
        if 1 <= num_tarea <= len(tareas):
            tarea_eliminada = tareas.pop(num_tarea - 1)
            print(f"Tarea '{tarea_eliminada}' eliminada")
        else:
            print("Número de tarea inválido")
    except ValueError:
        print("Debes ingresar un número válido")

def main():
    while True:
        print("\n---- App Tareas ----")
        print("1. Mostrar tareas")
        print("2. Agregar tareas")
        print("3. Eliminar tareas")
        print("4. Salir")

        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            mostrar_tareas()
        elif opcion == "2":
            agregar_tareas()
        elif opcion == "3":
            borrar_tareas()
        elif opcion == "4":
            print("Saliendo de la aplicación...")
            break
        else:
            print("Opción no válida")

if __name__ == "__main__":
    main()
    
