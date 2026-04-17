import random

def quickselect_iterativo(arr, k):
    """
    Versión iterativa de QuickSelect.
    """

    while True:
        # Si solo queda un elemento
        if len(arr) == 1:
            return arr[0]

        # Elegir pivote aleatorio
        pivote = random.choice(arr)

        # Particionar
        menores = [x for x in arr if x < pivote]
        iguales = [x for x in arr if x == pivote]
        mayores = [x for x in arr if x > pivote]

        if k < len(menores):
            arr = menores
        
        elif k < len(menores) + len(iguales):
            return pivote
        
        else:
            k = k - len(menores) - len(iguales)
            arr = mayores