# ==========================================
# TRACE PROJECT GENERATOR
# menu.py
# ==========================================

from configurador.asistente import nuevo_proyecto


def limpiar():

    print("\n" * 3)


def pausa():

    input("\nPresione ENTER para continuar...")


def mostrar_titulo():

    limpiar()

    print("=" * 55)
    print("        TRACE PROJECT GENERATOR")
    print("=" * 55)
    print()


def menu_principal():

    while True:

        mostrar_titulo()

        print("1 - Nuevo Proyecto")
        print("2 - Abrir Proyecto")
        print("3 - Exportar Proyecto")
        print("4 - Biblioteca Técnica")
        print("5 - Configuración")
        print("0 - Salir")

        print()

        opcion = input("Seleccione una opción: ").strip()

        if opcion == "1":

            nuevo_proyecto()

        elif opcion == "2":

            print("\nFunción en desarrollo.")
            pausa()

        elif opcion == "3":

            print("\nFunción en desarrollo.")
            pausa()

        elif opcion == "4":

            print("\nFunción en desarrollo.")
            pausa()

        elif opcion == "5":

            print("\nFunción en desarrollo.")
            pausa()

        elif opcion == "0":

            print("\nHasta luego.\n")
            break

        else:

            print("\nOpción inválida.")
            pausa()