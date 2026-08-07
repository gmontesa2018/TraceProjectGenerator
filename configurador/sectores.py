# ==========================================================
# TRACE PROJECT GENERATOR
# Configurador - Sectores
# ==========================================================

from configurador.preguntas import (
    pedir_si_no,
    pedir_entero,
    pedir_texto
)

from configurador.torres import cargar_torres


def cargar_sectores():

    sectores = []

    usar_sectores = pedir_si_no(
        "¿El proyecto está dividido en sectores?",
        "usar_sectores"
    )

    # ------------------------------------------------------
    # Proyecto sin sectores
    # ------------------------------------------------------

    if not usar_sectores:

        sector = {

            "nombre": "Sector Principal",

            "torres": cargar_torres(),

            "cantidad_sum": pedir_entero(
                "Cantidad de SUM",
                0,
                "cantidad_sum"
            ),

            "cantidad_gimnasios": pedir_entero(
                "Cantidad de Gimnasios",
                0,
                "cantidad_gimnasios"
            )

        }

        sectores.append(sector)

        return sectores

    # ------------------------------------------------------
    # Proyecto con sectores
    # ------------------------------------------------------

    cantidad = pedir_entero(
        "Cantidad de Sectores",
        1,
        "cantidad_sectores"
    )

    for numero in range(1, cantidad + 1):

        print()
        print("=" * 60)
        print(f"SECTOR {numero}")
        print("=" * 60)

        nombre = pedir_texto(
            "Nombre del Sector",
            f"sector_{numero}"
        )

        sector = {

            "nombre": nombre,

            "torres": cargar_torres(),

            "cantidad_sum": pedir_entero(
                "Cantidad de SUM",
                0,
                f"sum_sector_{numero}"
            ),

            "cantidad_gimnasios": pedir_entero(
                "Cantidad de Gimnasios",
                0,
                f"gym_sector_{numero}"
            )

        }

        sectores.append(sector)

    return sectores