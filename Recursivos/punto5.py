import random

# QUICKSELECT (VERSIÓN RECURSIVA)

def particion(arr, izquierda, derecha, pivote_indice):
    """
    Reorganiza el arreglo colocando:
    - Elementos menores al pivote a la izquierda
    - Elementos mayores al pivote a la derecha

    Parámetros:
    arr: lista de números
    izquierda: índice inicial del subarreglo
    derecha: índice final del subarreglo
    pivote_indice: índice del pivote seleccionado

    Retorna:
    La posición final del pivote después de la partición
    """

    pivote = arr[pivote_indice]

    # Mover el pivote al final
    arr[pivote_indice], arr[derecha] = arr[derecha], arr[pivote_indice]

    store_index = izquierda

    # Reorganizar el arreglo
    for i in range(izquierda, derecha):
        if arr[i] < pivote:
            arr[i], arr[store_index] = arr[store_index], arr[i]
            store_index += 1

    # Colocar el pivote en su posición correcta
    arr[store_index], arr[derecha] = arr[derecha], arr[store_index]

    return store_index


def quickselect_recursivo(notas, izquierda, derecha, k):
    """
    Encuentra el k-ésimo elemento más pequeño en el arreglo
    usando el algoritmo QuickSelect de forma recursiva.

    Parámetros:
    notas: lista de calificaciones
    izquierda: índice inicial
    derecha: índice final
    k: posición buscada (ej: mediana o percentil)

    Retorna:
    El valor del k-ésimo elemento
    """

    # Caso base: un solo elemento
    if izquierda == derecha:
        return notas[izquierda]

    # Seleccionar pivote aleatorio
    pivote_indice = random.randint(izquierda, derecha)

    # Reorganizar el arreglo alrededor del pivote
    pivote_indice = particion(notas, izquierda, derecha, pivote_indice)

    # Comparar posición del pivote con k
    if k == pivote_indice:
        return notas[k]
    elif k < pivote_indice:
        return quickselect_recursivo(notas, izquierda, pivote_indice - 1, k)
    else:
        return quickselect_recursivo(notas, pivote_indice + 1, derecha, k)


def calcular_estadisticas_recursivo(notas):
    """
    Calcula:
    - Mediana
    - Percentil 90

    usando QuickSelect recursivo.

    Parámetros:
    notas: lista de calificaciones

    Retorna:
    (mediana, percentil 90)
    """

    n = len(notas)

    # Mediana (posición central)
    mediana = quickselect_recursivo(notas.copy(), 0, n - 1, n // 2)

    # Percentil 90
    p90 = quickselect_recursivo(notas.copy(), 0, n - 1, int(0.9 * n))

    return mediana, p90


# BÚSQUEDA BINARIA (VERSIÓN RECURSIVA)

def busqueda_binaria_recursiva(notas, izquierda, derecha, objetivo):
    """
    Busca un valor en un arreglo ordenado usando búsqueda binaria recursiva.

    Parámetros:
    notas: lista ordenada de calificaciones
    izquierda: índice inicial
    derecha: índice final
    objetivo: valor a buscar

    Retorna:
    Índice del elemento si existe, -1 si no se encuentra
    """

    if izquierda > derecha:
        return -1

    medio = (izquierda + derecha) // 2

    if notas[medio] == objetivo:
        return medio
    elif notas[medio] < objetivo:
        return busqueda_binaria_recursiva(notas, medio + 1, derecha, objetivo)
    else:
        return busqueda_binaria_recursiva(notas, izquierda, medio - 1, objetivo)


def verificar_aprobacion_recursivo(notas, nota_buscar):
    """
    Verifica si un estudiante con cierta nota:
    - Existe en el sistema
    - Y si está aprobado (nota >= 60)

    Parámetros:
    notas: lista de calificaciones
    nota_buscar: nota del estudiante

    Retorna:
    True si aprobó, False en caso contrario
    """

    # Ordenar notas para aplicar búsqueda binaria
    notas_ordenadas = sorted(notas)

    # Buscar la nota
    indice = busqueda_binaria_recursiva(notas_ordenadas, 0, len(notas)-1, nota_buscar)

    # Verificar existencia y condición de aprobación
    if indice != -1 and nota_buscar >= 60:
        return True
    return False
if __name__ == "__main__":

    # Lista de calificaciones del curso
    notas = [45, 70, 82, 60, 90, 55, 77, 68]

    print("Notas del curso:", notas)

    # Calcular estadísticas
    mediana, p90 = calcular_estadisticas_recursivo(notas)

    print("Mediana:", mediana)
    print("Percentil 90:", p90)

    # Verificar aprobación de estudiantes
    nota1 = 70
    nota2 = 55

    print(f"¿El estudiante con nota {nota1} aprobó?:",
          verificar_aprobacion_recursivo(notas, nota1))

    print(f"¿El estudiante con nota {nota2} aprobó?:",
          verificar_aprobacion_recursivo(notas, nota2))