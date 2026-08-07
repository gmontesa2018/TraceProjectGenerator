# ==========================================================
# TRACE PROJECT GENERATOR
# Configurador - Preguntas
# ==========================================================

from configurador.memoria import obtener, guardar


def pedir_texto(texto, clave=None):

    if clave is None:
        clave = texto

    defecto = obtener(clave)

    while True:

        if defecto is None:
            valor = input(f"{texto}: ").strip()
        else:
            valor = input(f"{texto} [{defecto}]: ").strip()

        if valor == "" and defecto is not None:

            guardar(clave, defecto)

            return defecto

        if valor != "":

            guardar(clave, valor)

            return valor

        print("❌ Valor inválido.")


def pedir_entero(texto, minimo=0, clave=None, defecto=None):

    if clave is None:
        clave = texto

    if defecto is None:
        defecto = obtener(clave)

    while True:

        if defecto is None:
            valor = input(f"{texto}: ").strip()
        else:
            valor = input(f"{texto} [{defecto}]: ").strip()

        if valor == "" and defecto is not None:

            guardar(clave, defecto)

            return defecto

        if valor.isdigit():

            numero = int(valor)

            if numero >= minimo:

                guardar(clave, numero)

                return numero

        print("❌ Valor inválido.")


def pedir_si_no(texto, clave=None):

    if clave is None:
        clave = texto

    defecto = obtener(clave)

    while True:

        if defecto is None:

            valor = input(f"{texto} (S/N): ").strip().upper()

        else:

            sugerencia = "S" if defecto else "N"

            valor = input(
                f"{texto} (S/N) [{sugerencia}]: "
            ).strip().upper()

            if valor == "":
                guardar(clave, defecto)
                return defecto

        if valor in ["S", "SI"]:

            guardar(clave, True)

            return True

        if valor in ["N", "NO"]:

            guardar(clave, False)

            return False

        print("❌ Respuesta inválida.")


def pedir_opcion(titulo, opciones):

    while True:

        print()
        print("=" * 60)
        print(titulo.upper())
        print("=" * 60)

        for i, opcion in enumerate(opciones):

            print(f"{i + 1}. {opcion}")

        valor = input("\nSeleccione: ").strip()

        if valor.isdigit():

            indice = int(valor)

            if 1 <= indice <= len(opciones):
                return indice

        print("❌ Opción inválida.")