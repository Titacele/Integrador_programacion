from ordenar import *
from busqueda import *
from timer import medir_tiempo

def mostrar_menu():
    print("\n--- MENÚ PRINCIPAL ---")
    print("1. Ordenar lista")
    print("2. Buscar elemento")
    print("3. Salir")

def obtener_lista():
    entrada = input("Ingrese números separados por comas: ")
    return list(map(int, entrada.split(",")))

def main():
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            lista = obtener_lista()
            print("Seleccione el método de ordenamiento:")
            print("1. Bubble Sort")
            print("2. Selection Sort")
            print("3. Insertion Sort")
            print("4. Merge Sort")
            print("5. Quick Sort")

            metodo = input("Opción: ")
            algoritmos = {
                "1": bubble_sort,
                "2": selection_sort,
                "3": insertion_sort,
                "4": merge_sort,
                "5": quick_sort
            }

            if metodo in algoritmos:
                resultado, tiempo = medir_tiempo(algoritmos[metodo], lista.copy())
                print("Lista ordenada:", resultado)
                print(f"Tiempo de ejecución: {tiempo:.6f} segundos")
            else:
                print("Opción inválida.")

        elif opcion == "2":
            lista = obtener_lista()
            objetivo = int(input("Ingrese el número a buscar: "))
            print("Seleccione método de búsqueda:")
            print("1. Lineal")
            print("2. Binaria (requiere lista ordenada)")

            metodo = input("Opción: ")
            if metodo == "2":
                lista.sort()

            funciones = {
                "1": busqueda_lineal,
                "2": busqueda_binaria
            }

            if metodo in funciones:
                resultado, tiempo = medir_tiempo(funciones[metodo], lista, objetivo)
                if resultado != -1:
                    print(f"Elemento encontrado en la posición {resultado}")
                else:
                    print("Elemento no encontrado")
                print(f"Tiempo de ejecución: {tiempo:.6f} segundos")
            else:
                print("Opción inválida.")

        elif opcion == "3":
            print("Programa finalizado.")
            break
        else:
            print("Opción inválida. Intente de nuevo.")

if __name__ == "__main__":
    main()
