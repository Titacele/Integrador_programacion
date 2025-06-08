def busqueda_lineal(arr, objetivo):
    for i in range(len(arr)):
        if arr[i] == objetivo:
            return i
    return -1


def busqueda_binaria(arr, objetivo):
    bajo = 0
    alto = len(arr) - 1

    while bajo <= alto:
        medio = (bajo + alto) // 2
        if arr[medio] == objetivo:
            return medio
        elif arr[medio] < objetivo:
            bajo = medio + 1
        else:
            alto = medio - 1
    return -1
