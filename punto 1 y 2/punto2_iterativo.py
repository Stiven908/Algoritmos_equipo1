"""
=============================================================
Universidad del Valle – Sede Norte del Cauca
Análisis y Diseño de Algoritmos
Actividad Integradora: "Desafío 25 Algoritmos"
-------------------------------------------------------------
Equipo 1 : Anghelo, Stiven, Joan y Kristhal
Punto    : 2 – Búsqueda Lineal con conteo de comparaciones
Versión  : ITERATIVA
Responsable: Kristhal
Fecha    : abril 2026
=============================================================

DESCRIPCIÓN DEL ALGORITMO:
  Igual al punto 1 iterativo, pero agrega una variable
  'comparaciones' que se incrementa en cada iteración antes
  de comparar. Retorna una tupla (índice, comparaciones).

  Esto permite medir el rendimiento real del algoritmo,
  no solo el teórico.

COMPLEJIDAD:
  Tiempo  → Mejor caso  : O(1)   elemento en posición 0
             Peor caso   : O(n)   elemento no existe
             Promedio    : O(n)
  Espacio → O(1)  el contador es solo una variable entera

  El contador agrega Θ(1) por iteración → no cambia la clase:
  T(n) = Θ(n) + Θ(1) = Θ(n)
=============================================================
"""


def busqueda_lineal_conteo_iterativa(lista, objetivo):
    """
    Busca 'objetivo' dentro de 'lista' usando un bucle for.
    Además cuenta cuántas comparaciones se realizaron.

    Parámetros
    ----------
    lista    : list – lista de números enteros
    objetivo : int  – valor que se quiere encontrar

    Retorna
    -------
    tuple : (índice, comparaciones)
            índice        = posición encontrada, o -1 si no existe
            comparaciones = cuántas comparaciones se hicieron
    """

    comparaciones = 0       # iniciamos el contador en cero

    for i in range(len(lista)):

        comparaciones += 1  # contamos ANTES de comparar

        if lista[i] == objetivo:
            return i, comparaciones      # encontrado: índice + conteo

    return -1, comparaciones             # no encontrado: -1 + conteo total


# =============================================================
# PRUEBAS
# =============================================================
if __name__ == "__main__":

    print("=" * 50)
    print("PUNTO 2 – Búsqueda Lineal con conteo ITERATIVA")
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
        idx, comp = busqueda_lineal_conteo_iterativa(lista_prueba, objetivo)
        print(f"  Buscando {objetivo:>2}  →  índice={idx:>2}  |  comparaciones={comp}  ({descripcion})")
