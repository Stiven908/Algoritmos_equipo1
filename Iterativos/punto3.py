#ahora utilizamos selection sort para que el algoritmo sea iterativo.
def selection_sort(arr):
    # Obtenemos el tamaño del arreglo
    n = len(arr)
    
    # Recorremos todo el arreglo
    for i in range(n):
        # Suponemos que el elemento actual es el mínimo
        min_idx = i
        
        # Buscamos el elemento más pequeño en el resto del arreglo
        for j in range(i + 1, n):
            # Si encontramos un elemento menor al actual mínimo
            if arr[j] < arr[min_idx]:
                # Actualizamos el índice del nuevo mínimo
                min_idx = j
        
        # Intercambiamos el elemento actual con el mínimo encontrado
        # Esto coloca el elemento más pequeño en la posición correcta
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    
    # Retornamos el arreglo completamente ordenado
    return arr


def k_esimo_elemento(arr, k):
    # Hacemos una copia del arreglo original para no modificarlo
    arr_copia = arr[:]
    
    # Ordenamos el arreglo usando Selection Sort
    ordenado = selection_sort(arr_copia)
    
    # Retornamos el k-ésimo elemento más pequeño
    return ordenado[k - 1]


# Arreglo de entrada
arr = [7, 10, 4, 3, 20, 15]

# Queremos encontrar el 3er elemento más pequeño
k = 3

# Llamamos a la función
resultado = k_esimo_elemento(arr, k)

# Mostramos el resultado
print("El k-ésimo elemento más pequeño es:", resultado)