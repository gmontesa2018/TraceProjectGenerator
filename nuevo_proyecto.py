from clickup import *
from builder import generar_proyecto


# =====================================================
# FUNCIONES AUXILIARES
# =====================================================

def seleccionar_opcion(titulo, opciones):

    while True:

        print()
        print(titulo.upper())
        print("------------------------------")

        for i, item in enumerate(opciones):
            print(f"{i+1}. {item['name']}")

        valor = input(f"\nSeleccione {titulo}: ").strip()

        if not valor.isdigit():
            print("\n❌ Debe ingresar un número.")
            continue

        op = int(valor)

        if op < 1 or op > len(opciones):
            print("\n❌ Opción inválida.")
            continue

        return opciones[op - 1]


def pedir_entero(texto, minimo=0):

    while True:

        valor = input(f"{texto}: ").strip()

        if not valor.isdigit():
            print("❌ Debe ingresar un número.")
            continue

        numero = int(valor)

        if numero < minimo:
            print(f"❌ Debe ser mayor o igual a {minimo}.")
            continue

        return numero


def pedir_si_no(texto):

    while True:

        valor = input(f"{texto} (S/N): ").strip().upper()

        if valor in ["S", "SI", "Y", "YES"]:
            return True

        if valor in ["N", "NO"]:
            return False

        print("❌ Respuesta inválida.")


def pedir_texto(texto):

    while True:

        valor = input(f"{texto}: ").strip()

        if valor == "":
            print("❌ No puede quedar vacío.")
            continue

        return valor


# =====================================================
# NUEVO PROYECTO
# =====================================================

def nuevo_proyecto():

    print()
    print("===========================================")
    print("NUEVO PROYECTO")
    print("===========================================")

    teams = get_teams()

    if len(teams) == 0:
        print("No se encontraron Workspaces.")
        return

    team = seleccionar_opcion("Workspace", teams)

    spaces = get_spaces(team["id"])

    if len(spaces) == 0:
        print("No se encontraron Spaces.")
        return

    space = seleccionar_opcion("Space", spaces)

    folders = get_folders(space["id"])

    if len(folders) == 0:
        print("No se encontraron Folders.")
        return

    folder = seleccionar_opcion("Folder", folders)

    print()
    print("===========================================")
    print("DATOS DEL PROYECTO")
    print("===========================================")

    proyecto = {}

    proyecto["nombre"] = pedir_texto("Nombre del Proyecto")
    proyecto["cliente"] = pedir_texto("Cliente")
    proyecto["torres"] = pedir_entero("Cantidad de Torres", 1)
    proyecto["uf"] = pedir_entero("Cantidad Total de UF", 1)

    proyecto["sum"] = pedir_si_no("¿Tiene SUM?")
    proyecto["gimnasio"] = pedir_si_no("¿Tiene Gimnasio?")

    proyecto["portones"] = pedir_entero("Cantidad de Portones", 0)

    proyecto["cerco"] = pedir_si_no("¿Tiene Cerco Eléctrico?")

    if proyecto["cerco"]:
        proyecto["metros_cerco"] = pedir_entero("Metros de Cerco", 1)
    else:
        proyecto["metros_cerco"] = 0

    proyecto["barreras_ir"] = pedir_entero(
        "Cantidad de Barreras IR", 0
    )

    proyecto["camaras_perimetrales"] = pedir_entero(
        "Cantidad de Cámaras Perimetrales", 0
    )

    proyecto["camaras_subsuelo"] = pedir_entero(
        "Cantidad de Cámaras Subsuelo", 0
    )

    proyecto["frente_portero"] = pedir_si_no(
        "¿Tiene Frente de Portero?"
    )

    print()
    print("VMS")
    print("------------------------------")
    print("1 - iVMS-4200")
    print("2 - HikCentral")

    while True:

        op = input("Seleccione: ").strip()

        if op == "1":
            proyecto["vms"] = "IVMS"
            break

        if op == "2":
            proyecto["vms"] = "HIKCENTRAL"
            break

        print("Opción inválida.")

    print()
    print("Creando proyecto...")

    lista = create_list(
        folder["id"],
        proyecto["nombre"]
    )

    if lista is None:
        print("No fue posible crear la lista.")
        return

    generar_proyecto(
        lista["id"],
        proyecto
    )

    print()
    print("===========================================")
    print("PROYECTO GENERADO CORRECTAMENTE")
    print("===========================================")

    input("\nPresione ENTER para volver al menú...")