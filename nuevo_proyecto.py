from clickup import *
from builders.builder import generar_proyecto


# =====================================================
# AUXILIARES
# =====================================================
def seleccionar_opcion(titulo, opciones):

    while True:

        print()
        print("=" * 60)
        print(titulo.upper())
        print("=" * 60)

        for i, item in enumerate(opciones):

            print(f"{i+1}. {item['name']}")

        valor = input("\nSeleccione: ").strip()

        if not valor.isdigit():
            print("Valor inválido.")
            continue

        indice = int(valor)

        if indice < 1 or indice > len(opciones):
            print("Opción inválida.")
            continue

        return opciones[indice - 1]
        
def pedir_texto(texto):

    while True:

        valor = input(f"{texto}: ").strip()

        if valor:
            return valor

        print("Valor inválido.")


def pedir_entero(texto, minimo=0):

    while True:

        valor = input(f"{texto}: ").strip()

        if valor.isdigit():

            numero = int(valor)

            if numero >= minimo:
                return numero

        print("Valor inválido.")


def pedir_si_no(texto):

    while True:

        valor = input(f"{texto} (S/N): ").strip().upper()

        if valor in ["S", "SI"]:
            return True

        if valor in ["N", "NO"]:
            return False

        print("Respuesta inválida.")


# =====================================================
# GENERAR UF
# =====================================================

def generar_ufs(pb, por_piso, pisos):

    resultado = []

    # Planta Baja

    for i in range(1, pb + 1):

        resultado.append(
            {
                "codigo": f"{i:03}"
            }
        )

    # Pisos

    for piso in range(1, pisos + 1):

        for uf in range(1, por_piso + 1):

            codigo = piso * 100 + uf

            resultado.append(
                {
                    "codigo": f"{codigo:03}"
                }
            )

    return resultado


# =====================================================
# TORRES
# =====================================================

def cargar_torres():

    torres = []

    cantidad = pedir_entero(
        "Cantidad de Torres",
        1
    )

    print()

    for i in range(1, cantidad + 1):

        print("=" * 50)
        print(f"TORRE {i:02}")
        print("=" * 50)

        nombre = pedir_texto(
            "Nombre"
        )

        pisos = pedir_entero(
            "Cantidad de Pisos",
            1
        )

        pb = pedir_entero(
            "UF Planta Baja",
            1
        )

        por_piso = pedir_entero(
            "UF por Piso",
            1
        )

        torres.append(
            {
                "nombre": nombre,
                "pisos": pisos,
                "ufs": generar_ufs(
                    pb,
                    por_piso,
                    pisos
                )
            }
        )

    return torres
    # =====================================================
# NUEVO PROYECTO
# =====================================================

def nuevo_proyecto():

    print()
    print("=" * 60)
    print("NUEVO PROYECTO")
    print("=" * 60)

    teams = get_teams()

    if not teams:
        print("No se encontraron Workspaces.")
        return

    team = seleccionar_opcion("Workspace", teams)

    spaces = get_spaces(team["id"])

    if not spaces:
        print("No se encontraron Spaces.")
        return

    space = seleccionar_opcion("Space", spaces)

    folders = get_folders(space["id"])

    if not folders:
        print("No se encontraron Folders.")
        return

    folder = seleccionar_opcion("Folder", folders)

    proyecto = {}

    print()
    print("=" * 60)
    print("DATOS GENERALES")
    print("=" * 60)

    proyecto["nombre"] = pedir_texto("Nombre del Proyecto")
    proyecto["cliente"] = pedir_texto("Cliente")

    print()
    print("=" * 60)
    print("TORRES")
    print("=" * 60)

    proyecto["torres"] = cargar_torres()

    print()
    print("=" * 60)
    print("ÁREAS COMUNES")
    print("=" * 60)

    proyecto["sum"] = pedir_si_no("¿Tiene SUM?")
    proyecto["gimnasio"] = pedir_si_no("¿Tiene Gimnasio?")

    print()
    print("=" * 60)
    print("ACCESIBILIDAD")
    print("=" * 60)

    proyecto["portones"] = pedir_entero("Cantidad de Portones", 0)
    proyecto["frente_portero"] = pedir_si_no("¿Tiene Frente de Portero?")
    proyecto["porteros_interiores"] = pedir_si_no("¿Tiene Porteros Interiores?")
    proyecto["cerraduras"] = pedir_si_no("¿Tiene Cerraduras Biométricas?")

    print()
    print("=" * 60)
    print("SEGURIDAD PERIMETRAL")
    print("=" * 60)

    proyecto["cerco"] = pedir_si_no("¿Tiene Cerco Eléctrico?")

    if proyecto["cerco"]:
        proyecto["metros_cerco"] = pedir_entero("Metros de Cerco", 1)
    else:
        proyecto["metros_cerco"] = 0

    proyecto["barreras_ir"] = pedir_entero("Cantidad de Barreras IR", 0)
    proyecto["camaras_perimetrales"] = pedir_entero("Cantidad de Cámaras Perimetrales", 0)
    proyecto["camaras_subsuelo"] = pedir_entero("Cantidad de Cámaras de Subsuelo", 0)

    print()
    print("=" * 60)
    print("VMS")
    print("=" * 60)

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
    print("=" * 60)
    print("PROYECTO GENERADO CORRECTAMENTE")
    print("=" * 60)

    input("\nPresione ENTER para continuar...")