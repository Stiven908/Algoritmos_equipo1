#primero utilizamos merge sort para ordenar el arreglo
def merge_sort(arr):
    # Caso base: si el arreglo tiene 0 o 1 elemento, ya está ordenado
    if len(arr) <= 1:
        return arr
    
    # Dividimos el arreglo en dos mitades
    mid = len(arr) // 2
    
    # Llamadas recursivas para ordenar cada mitad
    izquierda = merge_sort(arr[:mid])
    derecha = merge_sort(arr[mid:])
    
    # Combinamos (merge) las dos mitades ya ordenadas
    return merge(izquierda, derecha)


def merge(izq, der):
    # Lista donde se guardará el resultado ordenado
    resultado = []
    
    # Índices para recorrer ambas listas
    i = 0
    j = 0
    
    # Recorremos ambas listas y comparamos elemento por elemento
    while i < len(izq) and j < len(der):
        if izq[i] < der[j]:
            # Si el elemento de la izquierda es menor, lo agregamos
            resultado.append(izq[i])
            i += 1  # avanzamos en la lista izquierda
        else:
            # Si el de la derecha es menor, lo agregamos
            resultado.append(der[j])
            j += 1  # avanzamos en la lista derecha
    
    # Si quedaron elementos en la lista izquierda, los agregamos
    # (ya están ordenados, así que se pueden añadir directamente)
    resultado.extend(izq[i:])
    
    # Si quedaron elementos en la lista derecha, los agregamos
    resultado.extend(der[j:])
    
    # Retornamos la lista completamente ordenada
    return resultado


def k_esimo_elemento(arr, k):
    # Primero ordenamos todo el arreglo (enfoque ingenuo)
    ordenado = merge_sort(arr)
    
    # Retornamos el k-ésimo elemento más pequeño
    # k-1 porque los índices en Python empiezan en 0
    return ordenado[k - 1]


# -------- PRUEBA --------

# Arreglo de entrada
arr = [7, 10, 4, 3, 20, 15]

# Queremos el 3er elemento más pequeño
k = 3

# Llamamos a la función
resultado = k_esimo_elemento(arr, k)

# Mostramos el resultado
print("El k-ésimo elemento más pequeño es:", resultado)