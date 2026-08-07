# ==========================================================
# TRACE PROJECT GENERATOR
# Configurador - Memoria
# ==========================================================

_memoria = {}


def obtener(clave, defecto=None):

    return _memoria.get(clave, defecto)


def guardar(clave, valor):

    _memoria[clave] = valor


def limpiar():

    _memoria.clear()


def mostrar():

    print()

    print("=" * 60)
    print("MEMORIA")
    print("=" * 60)

    for clave, valor in _memoria.items():

        print(f"{clave:25} {valor}")

    print()