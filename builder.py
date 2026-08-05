from clickup import create_task


# ==========================================================
# FUNCION AUXILIAR
# ==========================================================

def crear(list_id, nombre, parent=None):

    print("Creando:", nombre)

    tarea = create_task(
        list_id=list_id,
        name=nombre,
        parent=parent
    )

    if tarea is None:
        raise Exception(f"No se pudo crear la tarea: {nombre}")

    return tarea


# ==========================================================
# PROYECTO
# ==========================================================

def generar_proyecto(list_id, proyecto):

    # ======================================================
    # GESTION
    # ======================================================

    crear(list_id, "📋 Gestión")

    # ======================================================
    # COMUNICACIONES
    # ======================================================

    comunicaciones = crear(
        list_id,
        "🌐 Comunicaciones"
    )

    crear_centro_control(
        list_id,
        comunicaciones["id"],
        proyecto
    )

    crear_backbone(
        list_id,
        comunicaciones["id"],
        proyecto
    )

    for torre in range(1, proyecto["torres"] + 1):

        crear_torre(
            list_id,
            comunicaciones["id"],
            torre,
            proyecto
        )

    if proyecto["sum"]:
        crear_sum(
            list_id,
            comunicaciones["id"]
        )

    if proyecto["gimnasio"]:
        crear_gimnasio(
            list_id,
            comunicaciones["id"]
        )

    # ======================================================
    # ACCESIBILIDAD
    # ======================================================

    crear_accesibilidad(
        list_id,
        proyecto
    )

    # ======================================================
    # SEGURIDAD PERIMETRAL
    # ======================================================

    crear_seguridad_perimetral(
        list_id,
        proyecto
    )

    # ======================================================
    # SEGURIDAD INTERNA
    # ======================================================

    crear_seguridad_interna(
        list_id,
        proyecto
    )

    # ======================================================
    # CIERRE
    # ======================================================

    crear(list_id, "⚙️ Puesta en Marcha")

    crear(list_id, "🎓 Capacitación")

    crear(list_id, "📦 Entrega")


# ==========================================================
# CENTRO DE CONTROL
# ==========================================================

def crear_centro_control(list_id, parent, proyecto):

    nodo = crear(list_id, "🖥️ Centro de Control", parent)

    crear(list_id, "Rack Principal", nodo["id"])
    crear(list_id, "Switch Core", nodo["id"])
    crear(list_id, "Router", nodo["id"])
    crear(list_id, "UPS", nodo["id"])
    crear(list_id, "PC Operador", nodo["id"])
    crear(list_id, "Monitor", nodo["id"])
    crear(list_id, "Internet", nodo["id"])

    if proyecto["vms"] == "IVMS":
        crear(list_id, "iVMS-4200", nodo["id"])

    else:
        crear(list_id, "HikCentral", nodo["id"])


# ==========================================================
# BACKBONE
# ==========================================================

def crear_backbone(list_id, parent, proyecto):

    nodo = crear(
        list_id,
        "🔗 Backbone de Fibra",
        parent
    )

    for torre in range(1, proyecto["torres"] + 1):

        crear(
            list_id,
            f"Guardia → Torre {torre}",
            nodo["id"]
        )

    if proyecto["sum"]:
        crear(
            list_id,
            "Guardia → SUM",
            nodo["id"]
        )

    if proyecto["gimnasio"]:
        crear(
            list_id,
            "Guardia → Gimnasio",
            nodo["id"]
        )


# ==========================================================
# TORRE
# ==========================================================

def crear_torre(list_id, parent, numero, proyecto):

    torre = crear(
        list_id,
        f"🏢 Torre {numero}",
        parent
    )

    crear(list_id, "🏗️ Infraestructura", torre["id"])
    crear(list_id, "🌐 Red", torre["id"])
    crear(list_id, "⚙️ Servicios", torre["id"])
    crear(list_id, "🚪 Control de Accesos", torre["id"])

    if proyecto["porteros_interiores"]:
        crear(list_id, "📞 Portero Interior", torre["id"])

    crear(list_id, "📷 Cámara Hall", torre["id"])

    crear(
        list_id,
        f"🔐 Cerraduras Biométricas ({proyecto['cerraduras']})",
        torre["id"]
    )

    crear(list_id, "✅ QA", torre["id"])


# ==========================================================
# SUM
# ==========================================================

def crear_sum(list_id, parent):

    nodo = crear(list_id, "🎉 SUM", parent)

    crear(list_id, "🏗️ Infraestructura", nodo["id"])
    crear(list_id, "🌐 Red", nodo["id"])
    crear(list_id, "📷 Cámara", nodo["id"])
    crear(list_id, "🚪 Control de Acceso", nodo["id"])
    crear(list_id, "✅ QA", nodo["id"])


# ==========================================================
# GIMNASIO
# ==========================================================

def crear_gimnasio(list_id, parent):

    nodo = crear(list_id, "💪 Gimnasio", parent)

    crear(list_id, "🏗️ Infraestructura", nodo["id"])
    crear(list_id, "🌐 Red", nodo["id"])
    crear(list_id, "📷 Cámara", nodo["id"])
    crear(list_id, "🚪 Control de Acceso", nodo["id"])
    crear(list_id, "✅ QA", nodo["id"])


# ==========================================================
# ACCESIBILIDAD
# ==========================================================

def crear_accesibilidad(list_id, proyecto):

    nodo = crear(list_id, "🚪 Accesibilidad")

    crear(
        list_id,
        f"🚗 Acceso Vehicular ({proyecto['portones']})",
        nodo["id"]
    )

    if proyecto["frente_portero"]:
        crear(
            list_id,
            "📞 Frente de Portero",
            nodo["id"]
        )

    crear(
        list_id,
        "🚶 Acceso Peatonal",
        nodo["id"]
    )


# ==========================================================
# SEGURIDAD PERIMETRAL
# ==========================================================

def crear_seguridad_perimetral(list_id, proyecto):

    nodo = crear(
        list_id,
        "🛡️ Seguridad Perimetral"
    )

    if proyecto["cerco"]:
        crear(
            list_id,
            f"⚡ Cerco Eléctrico ({proyecto['metros_cerco']} m)",
            nodo["id"]
        )

    if proyecto["barreras_ir"] > 0:
        crear(
            list_id,
            f"📡 Barreras IR ({proyecto['barreras_ir']})",
            nodo["id"]
        )

    if proyecto["camaras_perimetrales"] > 0:
        crear(
            list_id,
            f"📷 CCTV Perimetral ({proyecto['camaras_perimetrales']})",
            nodo["id"]
        )


# ==========================================================
# SEGURIDAD INTERNA
# ==========================================================

def crear_seguridad_interna(list_id, proyecto):

    nodo = crear(
        list_id,
        "📷 Seguridad Interna"
    )

    crear(
        list_id,
        "🏢 CCTV Hall Torres",
        nodo["id"]
    )

    if proyecto["camaras_subsuelo"] > 0:
        crear(
            list_id,
            f"🅿️ CCTV Subsuelo ({proyecto['camaras_subsuelo']})",
            nodo["id"]
        )

    if proyecto["sum"]:
        crear(
            list_id,
            "🎉 CCTV SUM",
            nodo["id"]
        )

    if proyecto["gimnasio"]:
        crear(
            list_id,
            "💪 CCTV Gimnasio",
            nodo["id"]
        )