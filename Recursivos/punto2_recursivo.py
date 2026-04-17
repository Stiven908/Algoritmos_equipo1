"""
=============================================================
Universidad del Valle – Sede Norte del Cauca
Análisis y Diseño de Algoritmos
Actividad Integradora: "Desafío 25 Algoritmos"
-------------------------------------------------------------
Equipo 1 : Anghelo, Stiven, Joan y Kristhal
Punto    : 2 – Búsqueda Lineal con conteo de comparaciones
Versión  : RECURSIVA
Responsable: Kristhal
Fecha    : abril 2026
=============================================================

DESCRIPCIÓN DEL ALGORITMO:
  Igual al punto 1 recursivo, pero el contador de comparaciones
  se acumula a través de las llamadas usando el patrón de
  acumulador: se pasa como parámetro y se incrementa antes
  de cada comparación. Retorna una tupla (índice, comparaciones).

  CASOS BASE:
    1. indice >= len(lista) → retorna (-1, comparaciones)
    2. lista[indice] == objetivo → retorna (indice, comparaciones)

  CASO RECURSIVO:
    lista[indice] != objetivo → llamar con indice+1 y comparaciones actualizado

COMPLEJIDAD:
  Tiempo  → Mejor caso  : O(1)
             Peor caso   : O(n)
             Promedio    : O(n)
  Espacio → O(n)  n marcos en la pila de llamadas en peor caso

  El contador agrega Θ(1) por llamada → no cambia la clase:
  T(n) = O(n) + Θ(1) = O(n)

ECUACIÓN DE RECURRENCIA:
  T(n) = T(n-1) + Θ(1)    (igual que punto 1 recursivo)
  T(0) = Θ(1)

MÉTODO DE EXPANSIÓN:
  T(n) = T(n-1) + c = T(n-k) + k·c
  Con k=n: T(n) = T(0) + n·c = O(n)
=============================================================
"""


def busqueda_lineal_conteo_recursiva(lista, objetivo, indice=0, comparaciones=0):
    """
    Busca 'objetivo' en 'lista' usando recursión.
    Cuenta cuántas comparaciones se realizaron en total.

    Parámetros
    ----------
    lista         : list – lista de números enteros
    objetivo      : int  – valor que se quiere encontrar
    indice        : int  – posición actual (no modificar al llamar)
    comparaciones : int  – acumulador de comparaciones (no modificar al llamar)

    Retorna
    -------
    tuple : (índice, comparaciones)
            índice        = posición encontrada, o -1 si no existe
            comparaciones = cuántas comparaciones se hicieron en total
    """

    # CASO BASE 1: llegamos al final sin encontrar el objetivo
    if indice >= len(lista):
        return -1, comparaciones

    # Incrementamos el contador ANTES de comparar
    comparaciones += 1

    # CASO BASE 2: encontramos el objetivo
    if lista[indice] == objetivo:
        return indice, comparaciones

    # CASO RECURSIVO: seguimos buscando con el contador actualizado
    return busqueda_lineal_conteo_recursiva(
        lista,
        objetivo,
        indice + 1,       # avanzamos al siguiente elemento
        comparaciones     # pasamos el contador actualizado
    )


# =============================================================
# PRUEBAS
# =============================================================
if __name__ == "__main__":

    print("=" * 50)
    print("PUNTO 2 – Búsqueda Lineal con conteo RECURSIVA")
    print("=" * 50)

    lista_prueba = [5, 3, 8, 6, 2]
    print(f"  Lista : {lista_prueba}\n")

    casos = [
        (6,  "caso medio    → 4 comparaciones"),
        (5,  "mejor caso    → 1 comparación"),
        (2,  "casi peor     → 5 comparaciones"),
        (99, "peor caso     → 5 comparaciones, no encontrado"),
    ]

    for objetivo, descripcion in casos:
        idx, comp = busqueda_lineal_conteo_recursiva(lista_prueba, objetivo)
        print(f"  Buscando {objetivo:>2}  →  índice={idx:>2}  |  comparaciones={comp}  ({descripcion})")
