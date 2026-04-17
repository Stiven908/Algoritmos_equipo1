import random

# QUICKSELECT (VERSIÓN ITERATIVA)

def quickselect_iterativo(notas, k):
    """
    Encuentra el k-ésimo elemento más pequeño en el arreglo
    usando el algoritmo QuickSelect de forma iterativa.

    Parámetros:
    notas: lista de calificaciones
    k: posición buscada (ej: mediana o percentil)

    Retorna:
    El valor del k-ésimo elemento
    """

    izquierda = 0
    derecha = len(notas) - 1

    while True:
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
            derecha = pivote_indice - 1
        else:
            izquierda = pivote_indice + 1


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


def calcular_estadisticas_iterativo(notas):
    """
    Calcula:
    - Mediana
    - Percentil 90

    usando QuickSelect iterativo.

    Parámetros:
    notas: lista de calificaciones

    Retorna:
    (mediana, percentil 90)
    """

    n = len(notas)

    # Mediana (posición central)
    mediana = quickselect_iterativo(notas.copy(), n // 2)

    # Percentil 90
    p90 = quickselect_iterativo(notas.copy(), int(0.9 * n))

    return mediana, p90


# BÚSQUEDA BINARIA (VERSIÓN ITERATIVA)

def busqueda_binaria_iterativa(notas, objetivo):
    """
    Busca un valor en un arreglo ordenado usando búsqueda binaria iterativa.

    Parámetros:
    notas: lista ordenada de calificaciones
    objetivo: valor a buscar

    Retorna:
    Índice del elemento si existe, -1 si no se encuentra
    """

    izquierda = 0
    derecha = len(notas) - 1

    while izquierda <= derecha:
        medio = (izquierda + derecha) // 2

        if notas[medio] == objetivo:
            return medio
        elif notas[medio] < objetivo:
            izquierda = medio + 1
        else:
            derecha = medio - 1

    return -1


def verificar_aprobacion_iterativo(notas, nota_buscar):
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
    indice = busqueda_binaria_iterativa(notas_ordenadas, nota_buscar)

    # Verificar existencia y condición de aprobación
    if indice != -1 and nota_buscar >= 60:
        return True
    return False


# EJEMPLO DE EJECUCIÓN

if __name__ == "__main__":

    # Lista de calificaciones del curso
    notas = [45, 70, 82, 60, 90, 55, 77, 68]

    print("Notas del curso:", notas)

    # Calcular estadísticas
    mediana, p90 = calcular_estadisticas_iterativo(notas)

    print("Mediana:", mediana)
    print("Percentil 90:", p90)

    # Verificar aprobación de estudiantes
    nota1 = 70
    nota2 = 55

    print(f"¿El estudiante con nota {nota1} aprobó?:",
          verificar_aprobacion_iterativo(notas, nota1))

    print(f"¿El estudiante con nota {nota2} aprobó?:",
          verificar_aprobacion_iterativo(notas, nota2))