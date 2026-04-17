"""
=============================================================
Universidad del Valle – Sede Norte del Cauca
Análisis y Diseño de Algoritmos
Actividad Integradora: "Desafío 25 Algoritmos"
-------------------------------------------------------------
Equipo 1 : Anghelo, Stiven, Joan y Kristhal
Punto    : 1 – Búsqueda Lineal básica
Versión  : RECURSIVA
Responsable: Kristhal
Fecha    : abril 2026
=============================================================

DESCRIPCIÓN DEL ALGORITMO:
  En lugar de un bucle, la función se llama a sí misma
  avanzando el índice en 1 en cada llamada.

  CASOS BASE:
    1. indice >= len(lista) → no se encontró → retorna -1
    2. lista[indice] == objetivo → encontrado → retorna indice

  CASO RECURSIVO:
    lista[indice] != objetivo → llamar con indice + 1

COMPLEJIDAD:
  Tiempo  → Mejor caso  : O(1)   elemento en posición 0
             Peor caso   : O(n)   elemento no existe o está al final
             Promedio    : O(n)
  Espacio → O(n)  n marcos en la pila de llamadas en peor caso

ECUACIÓN DE RECURRENCIA:
  T(n) = T(n-1) + Θ(1)
  T(0) = Θ(1)

MÉTODO DE EXPANSIÓN:
  T(n) = T(n-1) + c
       = T(n-2) + 2c
       = T(n-k) + k·c
  Con k=n: T(n) = T(0) + n·c = O(n)
=============================================================
"""


def busqueda_lineal_recursiva(lista, objetivo, indice=0):
    """
    Busca 'objetivo' en 'lista' usando recursión.

    Parámetros
    ----------
    lista    : list – lista de números enteros
    objetivo : int  – valor que se quiere encontrar
    indice   : int  – posición actual (no modificar al llamar)

    Retorna
    -------
    int : índice de la primera aparición, o -1 si no existe
    """

    # CASO BASE 1: llegamos al final sin encontrar el objetivo
    if indice >= len(lista):
        return -1

    # CASO BASE 2: encontramos el objetivo en la posición actual
    if lista[indice] == objetivo:
        return indice

    # CASO RECURSIVO: seguimos buscando desde la siguiente posición
    return busqueda_lineal_recursiva(lista, objetivo, indice + 1)


# =============================================================
# PRUEBAS
# =============================================================
if __name__ == "__main__":

    print("=" * 50)
    print("PUNTO 1 – Búsqueda Lineal RECURSIVA")
    print("=" * 50)

    lista_prueba = [5, 3, 8, 6, 2]
    print(f"  Lista : {lista_prueba}\n")

    # Prueba del enunciado: objetivo = 6 → debe retornar índice 3
    r1 = busqueda_lineal_recursiva(lista_prueba, 6)
    print(f"  Buscando  6  →  índice: {r1}   (esperado: 3)")

    # Elemento al inicio → mejor caso (1 sola llamada recursiva)
    r2 = busqueda_lineal_recursiva(lista_prueba, 5)
    print(f"  Buscando  5  →  índice: {r2}   (esperado: 0, mejor caso)")

    # Elemento que no existe → peor caso (n+1 llamadas)
    r3 = busqueda_lineal_recursiva(lista_prueba, 99)
    print(f"  Buscando 99  →  índice: {r3}  (esperado: -1, peor caso)")

    # Árbol de llamadas para objetivo = 6
    print()
    print("  Árbol de llamadas (objetivo=6):")
    print("    busqueda_lineal_recursiva([5,3,8,6,2], 6, i=0)")
    print("      lista[0]=5 ≠ 6  →  llama con i=1")
    print("    busqueda_lineal_recursiva([5,3,8,6,2], 6, i=1)")
    print("      lista[1]=3 ≠ 6  →  llama con i=2")
    print("    busqueda_lineal_recursiva([5,3,8,6,2], 6, i=2)")
    print("      lista[2]=8 ≠ 6  →  llama con i=3")
    print("    busqueda_lineal_recursiva([5,3,8,6,2], 6, i=3)")
    print("      lista[3]=6 == 6  →  RETORNA 3  ✓")
