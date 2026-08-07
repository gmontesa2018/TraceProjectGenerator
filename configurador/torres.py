# ==========================================================
# TRACE PROJECT GENERATOR
# Configurador - Torres
# ==========================================================

from configurador.preguntas import (
    pedir_texto,
    pedir_entero,
    pedir_si_no,
    pedir_opcion
)


def generar_ufs(plantas):

    resultado = []

    for piso, cantidad in enumerate(plantas):

        if piso == 0:

            for uf in range(1, cantidad + 1):

                resultado.append(
                    {
                        "codigo": f"{uf:03}"
                    }
                )

        else:

            for uf in range(1, cantidad + 1):

                codigo = piso * 100 + uf

                resultado.append(
                    {
                        "codigo": f"{codigo:03}"
                    }
                )

    return resultado


def cargar_torres():

    torres = []

    cantidad = pedir_entero(
        "Cantidad de Torres",
        1,
        "cantidad_torres"
    )

    torre_anterior = None

    for numero in range(1, cantidad + 1):

        print()
        print("=" * 60)
        print(f"TORRE {numero:02}")
        print("=" * 60)

        nombre = pedir_texto(
            "Nombre",
            f"torre_{numero}_nombre"
        )

        if torre_anterior is not None:

            print()
            opcion = pedir_opcion(
                "Configuración de la Torre",
                [
                    "Igual a la torre anterior",
                    "Copiar y modificar",
                    "Nueva configuración"
                ]
            )

            if opcion == 1:

                plantas = torre_anterior["plantas"][:]

            elif opcion == 2:

                plantas = modificar_plantas(
                    torre_anterior["plantas"]
                )

            else:

                plantas = cargar_plantas()

        else:

            plantas = cargar_plantas()

        torre = {

            "nombre": nombre,
            "plantas": plantas,
            "ufs": generar_ufs(plantas)

        }

        torres.append(torre)

        torre_anterior = torre

        mostrar_resumen_torre(torre)

    return torres


def cargar_plantas(defecto=None):

    if defecto is None:

        cantidad_plantas = pedir_entero(
            "Cantidad de Plantas",
            1,
            "cantidad_plantas"
        )

        iguales = pedir_si_no(
            "¿Todas las plantas tienen la misma cantidad de UF?",
            "uf_iguales"
        )

    else:

        cantidad_plantas = len(defecto)

        iguales = False

    plantas = []

    if iguales:

        cantidad = pedir_entero(
            "Cantidad de UF por planta",
            1,
            "uf_por_planta"
        )

        for _ in range(cantidad_plantas):
            plantas.append(cantidad)

    else:

        for piso in range(cantidad_plantas):

            if piso == 0:
                texto = "UF Planta Baja"
            else:
                texto = f"UF Piso {piso}"

            valor_defecto = None

            if defecto is not None:
                valor_defecto = defecto[piso]

            cantidad = pedir_entero(
                texto,
                minimo=1,
                clave=texto,
                defecto=valor_defecto
            )

            plantas.append(cantidad)

    return plantas

def modificar_plantas(plantas_originales):

    plantas = plantas_originales.copy()

    while True:

        print()
        print("-" * 50)
        print("CONFIGURACIÓN ACTUAL")
        print("-" * 50)

        for piso, cantidad in enumerate(plantas):

            if piso == 0:
                print(f"1 - Planta Baja : {cantidad}")
            else:
                print(f"{piso+1} - Piso {piso} : {cantidad}")

        print()
        print("M - Modificar todas las plantas")
        print("0 - Continuar")

        opcion = input("\nSeleccione: ").strip().upper()

        if opcion == "0":
            break

        if opcion == "M":

            return cargar_plantas(plantas)

        if opcion.isdigit():

            indice = int(opcion) - 1

            if 0 <= indice < len(plantas):

                if indice == 0:
                    texto = "Nueva cantidad UF Planta Baja"
                else:
                    texto = f"Nueva cantidad UF Piso {indice}"

                plantas[indice] = pedir_entero(
                    texto,
                    minimo=1,
                    clave=f"torre_mod_{indice}",
                    defecto=plantas[indice]
                )

    return plantas

def mostrar_resumen_torre(torre):

    print()
    print("-" * 50)
    print(torre["nombre"])
    print("-" * 50)

    total = 0

    for piso, cantidad in enumerate(torre["plantas"]):

        if piso == 0:
            print(f"PB : {cantidad}")
        else:
            print(f"P{piso} : {cantidad}")

        total += cantidad

    print("-" * 50)
    print(f"TOTAL UF : {total}")
    print("-" * 50)