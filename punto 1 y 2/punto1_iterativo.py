"""
=============================================================
Universidad del Valle – Sede Norte del Cauca
Análisis y Diseño de Algoritmos
Actividad Integradora: "Desafío 25 Algoritmos"
-------------------------------------------------------------
Equipo 1 : Anghelo, Stiven, Joan y Kristhal
Punto    : 1 – Búsqueda Lineal básica
Versión  : ITERATIVA
Responsable: Kristhal
Fecha    : abril 2026
=============================================================

DESCRIPCIÓN DEL ALGORITMO:
  Recorre la lista elemento por elemento usando un bucle for.
  En cuanto encuentra el objetivo devuelve su índice.
  Si termina el recorrido sin encontrarlo, devuelve -1.

COMPLEJIDAD:
  Tiempo  → Mejor caso  : O(1)   elemento en posición 0
             Peor caso   : O(n)   elemento no existe o está al final
             Promedio    : O(n)
  Espacio → O(1)  solo usa variables simples
=============================================================
"""


def busqueda_lineal_iterativa(lista, objetivo):
    """
    Busca 'objetivo' dentro de 'lista' usando un bucle for.

    Parámetros
    ----------
    lista    : list – lista de números enteros
    objetivo : int  – valor que se quiere encontrar

    Retorna
    -------
    int : índice de la primera aparición, o -1 si no existe
    """

    # Recorremos cada índice de izquierda a derecha
    for i in range(len(lista)):

        # ¿Es este el elemento que buscamos?
        if lista[i] == objetivo:
            return i        # sí → devolvemos la posición inmediatamente

    # Recorrimos toda la lista sin encontrarlo
    return -1


# =============================================================
# PRUEBAS
# =============================================================
if __name__ == "__main__":

    print("=" * 50)
    print("PUNTO 1 – Búsqueda Lineal ITERATIVA")
    print("=" * 50)

    lista_prueba = [5, 3, 8, 6, 2]
    print(f"  Lista : {lista_prueba}\n")

    # Prueba del enunciado: objetivo = 6 → debe retornar índice 3
    r1 = busqueda_lineal_iterativa(lista_prueba, 6)
    print(f"  Buscando  6  →  índice: {r1}   (esperado: 3)")

    # Elemento al inicio → mejor caso
    r2 = busqueda_lineal_iterativa(lista_prueba, 5)
    print(f"  Buscando  5  →  índice: {r2}   (esperado: 0, mejor caso)")

    # Elemento que no existe → peor caso
    r3 = busqueda_lineal_iterativa(lista_prueba, 99)
    print(f"  Buscando 99  →  índice: {r3}  (esperado: -1, peor caso)")
