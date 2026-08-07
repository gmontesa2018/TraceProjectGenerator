# ==========================================================
# TRACE PROJECT GENERATOR
# Builder - Seguridad Interna
# ==========================================================

from builders.helpers import crear


def crear_seguridad_interna(list_id, proyecto):

    seguridad = crear(
        list_id,
        "📷 Seguridad Interna"
    )

    # ------------------------------------------------------
    # Hall de Torres
    # ------------------------------------------------------

    crear_hall_torres(
        list_id,
        seguridad
    )

    # ------------------------------------------------------
    # Subsuelo
    # ------------------------------------------------------

    if proyecto["camaras_subsuelo"] > 0:

        crear_subsuelo(
            list_id,
            seguridad,
            proyecto
        )

    # ------------------------------------------------------
    # Sectores
    # ------------------------------------------------------

    for sector in proyecto["sectores"]:

        nodo_sector = crear(
            list_id,
            f"🏘️ {sector['nombre']}",
            seguridad
        )

        # ----------------------------------------------
        # CCTV SUM
        # ----------------------------------------------

        for i in range(sector["cantidad_sum"]):

            crear(
                list_id,
                f"🎉 CCTV SUM {i + 1}",
                nodo_sector
            )

        # ----------------------------------------------
        # CCTV Gimnasios
        # ----------------------------------------------

        for i in range(sector["cantidad_gimnasios"]):

            crear(
                list_id,
                f"💪 CCTV Gimnasio {i + 1}",
                nodo_sector
            )


# ==========================================================
# HALL TORRES
# ==========================================================

def crear_hall_torres(list_id, parent):

    crear(
        list_id,
        "🏢 CCTV Hall Torres",
        parent
    )


# ==========================================================
# SUBSUELOS
# ==========================================================

def crear_subsuelo(list_id, parent, proyecto):

    crear(
        list_id,
        f"🅿️ CCTV Subsuelo ({proyecto['camaras_subsuelo']} cámaras)",
        parent
    )