# ==========================================================
# TRACE PROJECT GENERATOR
# Builder - Gestión
# ==========================================================

from builders.helpers import crear


def crear_gestion(list_id):

    gestion = crear(
        list_id,
        "📋 Gestión"
    )

    crear(list_id, "📑 Relevamiento", gestion)
    crear(list_id, "💰 Presupuesto", gestion)
    crear(list_id, "📐 Ingeniería", gestion)
    crear(list_id, "📅 Planificación", gestion)
    crear(list_id, "🛒 Compras", gestion)