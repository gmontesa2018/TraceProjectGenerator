# ==========================================================
# TRACE PROJECT GENERATOR
# Builder - Áreas Comunes
# ==========================================================

from builders.helpers import crear


def crear_areas_comunes(list_id, parent, sector, proyecto):

    # ------------------------------------------------------
    # SUM
    # ------------------------------------------------------

    for i in range(sector["cantidad_sum"]):

        crear_sum(
            list_id,
            parent,
            i + 1
        )

    # ------------------------------------------------------
    # GIMNASIOS
    # ------------------------------------------------------

    for i in range(sector["cantidad_gimnasios"]):

        crear_gimnasio(
            list_id,
            parent,
            i + 1
        )


# ==========================================================
# SUM
# ==========================================================

def crear_sum(list_id, parent, numero):

    nodo = crear(
        list_id,
        f"🏢 SUM {numero}",
        parent
    )

    crear(list_id, "📐 Ingeniería", nodo)
    crear(list_id, "🏗️ Infraestructura", nodo)
    crear(list_id, "🌐 Red", nodo)
    crear(list_id, "📷 CCTV", nodo)
    crear(list_id, "🚪 Control de Accesos", nodo)
    crear(list_id, "📺 Monitor Interior", nodo)
    crear(list_id, "🔐 Cerradura Inteligente", nodo)
    crear(list_id, "⚡ Alimentación", nodo)
    crear(list_id, "🔧 Configuración", nodo)
    crear(list_id, "🧪 Pruebas", nodo)
    crear(list_id, "📄 Documentación", nodo)
    crear(list_id, "📷 Fotos", nodo)


# ==========================================================
# GIMNASIOS
# ==========================================================

def crear_gimnasio(list_id, parent, numero):

    nodo = crear(
        list_id,
        f"💪 Gimnasio {numero}",
        parent
    )

    crear(list_id, "📐 Ingeniería", nodo)
    crear(list_id, "🏗️ Infraestructura", nodo)
    crear(list_id, "🌐 Red", nodo)
    crear(list_id, "📷 CCTV", nodo)
    crear(list_id, "🚪 Control de Accesos", nodo)
    crear(list_id, "📺 Monitor Interior", nodo)
    crear(list_id, "🔐 Cerradura Inteligente", nodo)
    crear(list_id, "⚡ Alimentación", nodo)
    crear(list_id, "🔧 Configuración", nodo)
    crear(list_id, "🧪 Pruebas", nodo)
    crear(list_id, "📄 Documentación", nodo)
    crear(list_id, "📷 Fotos", nodo)