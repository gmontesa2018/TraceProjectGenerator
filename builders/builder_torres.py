# ==========================================================
# TRACE PROJECT GENERATOR
# Builder - Torres
# ==========================================================

from builders.helpers import crear

from biblioteca.plantillas.monitor_interior import aplicar as aplicar_monitor
from biblioteca.plantillas.cerradura import aplicar as aplicar_cerradura


# ==========================================================
# TORRES
# ==========================================================

def crear_torres(list_id, parent, sector, proyecto):

    for torre in sector["torres"]:

        crear_torre(
            list_id,
            parent,
            torre,
            proyecto
        )


# ==========================================================
# TORRE
# ==========================================================

def crear_torre(list_id, parent, torre, proyecto):

    nodo = crear(
        list_id,
        f"🏢 Torre {torre['nombre']}",
        parent
    )

    crear(list_id, "📐 Ingeniería", nodo)
    crear(list_id, "🏗️ Infraestructura", nodo)
    crear(list_id, "🌐 Red Torre", nodo)

    if proyecto["camaras_perimetrales"] > 0:
        crear(list_id, "📷 CCTV Hall", nodo)

    crear(list_id, "🚪 Control Acceso Hall", nodo)
    crear(list_id, "📄 Documentación", nodo)

    # -----------------------------------------
    # UNIDADES FUNCIONALES
    # -----------------------------------------

    nodo_ufs = crear(
        list_id,
        "🏠 Unidades Funcionales",
        nodo
    )

    crear_ufs(
        list_id,
        nodo_ufs,
        torre,
        proyecto
    )


# ==========================================================
# UFS
# ==========================================================

def crear_ufs(list_id, parent, torre, proyecto):

    for uf in torre["ufs"]:

        nodo_uf = crear(
            list_id,
            f"🏠 UF {uf['codigo']}",
            parent
        )

        # -----------------------------------------
        # Monitor Interior
        # -----------------------------------------

        if proyecto["porteros_interiores"]:

            monitor = crear(
                list_id,
                "📺 Monitor Interior",
                nodo_uf
            )

            aplicar_monitor(
                list_id,
                monitor
            )

        # -----------------------------------------
        # Cerradura Inteligente
        # -----------------------------------------

        if proyecto["cerraduras"]:

            cerradura = crear(
                list_id,
                "🔐 Cerradura Inteligente",
                nodo_uf
            )

            aplicar_cerradura(
                list_id,
                cerradura
            )