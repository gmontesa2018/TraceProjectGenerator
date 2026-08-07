# ==========================================================
# TRACE PROJECT GENERATOR
# Builder - Seguridad Perimetral
# ==========================================================

from builders.helpers import crear


def crear_seguridad_perimetral(list_id, proyecto):

    perimetral = crear(
        list_id,
        "🛡️ Seguridad Perimetral"
    )

    if proyecto["cerco"]:
        crear_cerco(
            list_id,
            perimetral,
            proyecto
        )

    if proyecto["barreras_ir"] > 0:
        crear_barreras(
            list_id,
            perimetral,
            proyecto
        )

    if proyecto["camaras_perimetrales"] > 0:
        crear_cctv_perimetral(
            list_id,
            perimetral,
            proyecto
        )


# ==========================================================
# CERCO
# ==========================================================

def crear_cerco(list_id, parent, proyecto):

    crear(
        list_id,
        f"⚡ Cerco Eléctrico ({proyecto['metros_cerco']} m)",
        parent
    )


# ==========================================================
# BARRERAS IR
# ==========================================================

def crear_barreras(list_id, parent, proyecto):

    crear(
        list_id,
        f"📡 Barreras IR ({proyecto['barreras_ir']})",
        parent
    )


# ==========================================================
# CCTV PERIMETRAL
# ==========================================================

def crear_cctv_perimetral(list_id, parent, proyecto):

    crear(
        list_id,
        f"📷 CCTV Perimetral ({proyecto['camaras_perimetrales']})",
        parent
    )