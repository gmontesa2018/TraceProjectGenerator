# ==========================================================
# TRACE PROJECT GENERATOR
# Configurador - Asistente
# ==========================================================

from clickup import (
    get_teams,
    get_spaces,
    get_folders,
    create_list
)

from builders.builder import generar_proyecto

from configurador.utilidades import titulo

from configurador.preguntas import (
    pedir_texto,
    pedir_entero,
    pedir_si_no,
    pedir_opcion
)

from configurador.sectores import cargar_sectores
from configurador.resumen import mostrar_resumen


# ==========================================================
# SELECCIONAR
# ==========================================================

def seleccionar(nombre, elementos):

    opciones = []

    for elemento in elementos:
        opciones.append(elemento["name"])

    indice = pedir_opcion(
        nombre,
        opciones
    )

    return elementos[indice - 1]


# ==========================================================
# NUEVO PROYECTO
# ==========================================================

def nuevo_proyecto():

    titulo("Nuevo Proyecto")

    # ------------------------------------------------------
    # Workspace
    # ------------------------------------------------------

    teams = get_teams()

    workspace = seleccionar(
        "Workspace",
        teams
    )

    # ------------------------------------------------------
    # Space
    # ------------------------------------------------------

    spaces = get_spaces(
        workspace["id"]
    )

    space = seleccionar(
        "Space",
        spaces
    )

    # ------------------------------------------------------
    # Folder
    # ------------------------------------------------------

    folders = get_folders(
        space["id"]
    )

    folder = seleccionar(
        "Folder",
        folders
    )

    proyecto = {}

    # ------------------------------------------------------
    # DATOS GENERALES
    # ------------------------------------------------------

    titulo("Datos Generales")

    proyecto["nombre"] = pedir_texto(
        "Nombre del Proyecto",
        "nombre_proyecto"
    )

    proyecto["cliente"] = pedir_texto(
        "Cliente",
        "cliente"
    )

    # ------------------------------------------------------
    # SECTORES
    # ------------------------------------------------------

    titulo("Sectores")

    proyecto["sectores"] = cargar_sectores()

    # ------------------------------------------------------
    # ACCESIBILIDAD
    # ------------------------------------------------------

    titulo("Accesibilidad")

    proyecto["portones"] = pedir_entero(
        "Cantidad de Portones",
        0,
        "portones"
    )

    proyecto["cantidad_frentes_portero"] = pedir_entero(
        "Cantidad de Frentes de Portero",
        0,
        "cantidad_frentes_portero"
    )

    proyecto["porteros_interiores"] = pedir_si_no(
        "¿Tiene Porteros Interiores?",
        "porteros_interiores"
    )

    proyecto["cerraduras"] = pedir_si_no(
        "¿Tiene Cerraduras Biométricas?",
        "cerraduras"
    )

    # ------------------------------------------------------
    # SEGURIDAD
    # ------------------------------------------------------

    titulo("Seguridad")

    proyecto["cerco"] = pedir_si_no(
        "¿Tiene Cerco Eléctrico?",
        "cerco"
    )

    if proyecto["cerco"]:

        proyecto["metros_cerco"] = pedir_entero(
            "Metros de Cerco",
            1,
            "metros_cerco"
        )

    else:

        proyecto["metros_cerco"] = 0

    proyecto["barreras_ir"] = pedir_entero(
        "Cantidad de Barreras IR",
        0,
        "barreras_ir"
    )

    proyecto["camaras_perimetrales"] = pedir_entero(
        "Cantidad de Cámaras Perimetrales",
        0,
        "camaras_perimetrales"
    )

    proyecto["camaras_subsuelo"] = pedir_entero(
        "Cantidad de Cámaras de Subsuelo",
        0,
        "camaras_subsuelo"
    )

    # ------------------------------------------------------
    # VMS
    # ------------------------------------------------------

    titulo("VMS")

    opcion = pedir_opcion(
        "Seleccione el VMS",
        [
            "iVMS-4200",
            "HikCentral"
        ]
    )

    if opcion == 1:
        proyecto["vms"] = "IVMS"
    else:
        proyecto["vms"] = "HIKCENTRAL"

    # ------------------------------------------------------
    # RESUMEN
    # ------------------------------------------------------

    opcion = mostrar_resumen(proyecto)

    if opcion == 3:

        print("\nProyecto cancelado.\n")
        return

    if opcion == 2:

        print("\nEdición de datos en desarrollo.\n")
        return

    # ------------------------------------------------------
    # CREAR LISTA
    # ------------------------------------------------------

    titulo("Creando Proyecto")

    lista = create_list(
        folder["id"],
        proyecto["nombre"]
    )

    if lista is None:

        print("\nNo fue posible crear la lista.\n")
        return

    # ------------------------------------------------------
    # BUILDER
    # ------------------------------------------------------

    generar_proyecto(
        lista["id"],
        proyecto
    )

    # ------------------------------------------------------
    # FIN
    # ------------------------------------------------------

    titulo("Proyecto creado correctamente")

    input("\nPresione ENTER para continuar...")