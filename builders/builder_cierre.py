# ==========================================================
# TRACE PROJECT GENERATOR
# Builder - Cierre
# ==========================================================

from builders.helpers import crear


def crear_cierre(list_id):

    cierre = crear(
        list_id,
        "🏁 Cierre del Proyecto"
    )

    crear(list_id, "✅ QA General", cierre)
    crear(list_id, "📚 Capacitación", cierre)
    crear(list_id, "📄 Documentación Conforme a Obra", cierre)
    crear(list_id, "🤝 Entrega Final", cierre)