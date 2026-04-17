import random

def quickselect_recursivo(arr, k):
    """
    Retorna el k-ésimo elemento más pequeño del arreglo.
    k es índice basado en 0 (k=0 es el menor).
    """

    # Caso base: si el arreglo tiene un solo elemento
    if len(arr) == 1:
        return arr[0]

    # Elegimos un pivote aleatorio
    pivote = random.choice(arr)

    # Particionamos el arreglo en tres partes
    menores = [x for x in arr if x < pivote]
    iguales = [x for x in arr if x == pivote]
    mayores = [x for x in arr if x > pivote]

    # Decidimos en qué parte está el k-ésimo elemento
    if k < len(menores):
        # Está en la parte de los menores
        return quickselect_recursivo(menores, k)
    
    elif k < len(menores) + len(iguales):
        # Está en los iguales (es el pivote)
        return pivote
    
    else:
        # Está en los mayores
        return quickselect_recursivo(mayores, k - len(menores) - len(iguales))