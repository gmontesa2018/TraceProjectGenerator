# ==========================================================
# TRACE PROJECT GENERATOR
# Builder - Comunicaciones
# ==========================================================

from builders.helpers import crear


def crear_comunicaciones(list_id, proyecto):

    comunicaciones = crear(
        list_id,
        "🌐 Comunicaciones"
    )

    crear_centro_control(
        list_id,
        comunicaciones,
        proyecto
    )

    crear_backbone(
        list_id,
        comunicaciones,
        proyecto
    )


# ==========================================================
# CENTRO DE CONTROL
# ==========================================================

def crear_centro_control(list_id, parent, proyecto):

    nodo = crear(
        list_id,
        "🖥️ Centro de Control",
        parent
    )

    crear(list_id, "🗄️ Rack Principal", nodo)
    crear(list_id, "🔀 Switch Core", nodo)
    crear(list_id, "🌐 Router", nodo)
    crear(list_id, "🔋 UPS", nodo)
    crear(list_id, "💻 PC Operador", nodo)
    crear(list_id, "🖥️ Monitores", nodo)
    crear(list_id, "🌍 Internet", nodo)

    if proyecto["vms"] == "IVMS":
        crear(list_id, "📹 iVMS-4200", nodo)
    else:
        crear(list_id, "📹 HikCentral", nodo)


# ==========================================================
# BACKBONE
# ==========================================================

def crear_backbone(list_id, parent, proyecto):

    backbone = crear(
        list_id,
        "🔗 Backbone",
        parent
    )

    for sector in proyecto["sectores"]:

        nodo_sector = crear(
            list_id,
            f"🏘️ {sector['nombre']}",
            backbone
        )

        # Backbone hacia las torres

        for torre in sector["torres"]:

            crear(
                list_id,
                f"🌐 Fibra → {torre['nombre']}",
                nodo_sector
            )

        # Backbone hacia SUM

        for i in range(sector["cantidad_sum"]):

            crear(
                list_id,
                f"🌐 Fibra → SUM {i+1}",
                nodo_sector
            )

        # Backbone hacia Gimnasios

        for i in range(sector["cantidad_gimnasios"]):

            crear(
                list_id,
                f"🌐 Fibra → Gimnasio {i+1}",
                nodo_sector
            )