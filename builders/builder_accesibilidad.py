# ==========================================================
# TRACE PROJECT GENERATOR
# Builder - Accesibilidad
# ==========================================================

from builders.helpers import crear


def crear_accesibilidad(list_id, proyecto):

    accesibilidad = crear(
        list_id,
        "🚪 Accesibilidad"
    )

    crear_accesos_vehiculares(
        list_id,
        accesibilidad,
        proyecto
    )

    crear_accesos_peatonales(
        list_id,
        accesibilidad,
        proyecto
    )


# ==========================================================
# ACCESOS VEHICULARES
# ==========================================================

def crear_accesos_vehiculares(list_id, parent, proyecto):

    vehicular = crear(
        list_id,
        "🚗 Accesos Vehiculares",
        parent
    )

    for i in range(1, proyecto["portones"] + 1):

        porton = crear(
            list_id,
            f"🚗 Portón {i:02}",
            vehicular
        )

        crear(list_id, "🚪 Automatismo", porton)
        crear(list_id, "📷 Lector LPR", porton)
        crear(list_id, "🚦 Semáforo", porton)
        crear(list_id, "🔄 Lazo Magnético", porton)
        crear(list_id, "⚡ Alimentación", porton)
        crear(list_id, "🌐 Red", porton)
        crear(list_id, "✅ QA", porton)


# ==========================================================
# ACCESOS PEATONALES
# ==========================================================

def crear_accesos_peatonales(list_id, parent, proyecto):

    peatonal = crear(
        list_id,
        "🚶 Accesos Peatonales",
        parent
    )

    # ------------------------------------------------------
    # Frentes de Portero
    # ------------------------------------------------------

    for i in range(1, proyecto["cantidad_frentes_portero"] + 1):

        frente = crear(
            list_id,
            f"📞 Frente de Portero {i:02}",
            peatonal
        )

        crear(list_id, "📷 Cámara", frente)
        crear(list_id, "🎤 Audio", frente)
        crear(list_id, "🔒 Cerradura Eléctrica", frente)
        crear(list_id, "🌐 Red", frente)
        crear(list_id, "⚡ Alimentación", frente)
        crear(list_id, "✅ QA", frente)

    # ------------------------------------------------------
    # Control de Accesos
    # ------------------------------------------------------

    acceso = crear(
        list_id,
        "🚪 Control de Accesos",
        peatonal
    )

    crear(list_id, "Lector", acceso)
    crear(list_id, "Controladora", acceso)
    crear(list_id, "Botón de Salida", acceso)
    crear(list_id, "Fuente", acceso)
    crear(list_id, "QA", acceso)

    # ------------------------------------------------------
    # Cerraduras Biométricas
    # ------------------------------------------------------

    if proyecto["cerraduras"]:

        crear(
            list_id,
            "🔐 Cerraduras Biométricas",
            peatonal
        )