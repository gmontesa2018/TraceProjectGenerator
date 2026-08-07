# ==========================================================
# TRACE PROJECT GENERATOR
# Builder - Sectores
# ==========================================================

from builders.helpers import crear
from builders.builder_torres import crear_torres
from builders.builder_areas_comunes import crear_areas_comunes


def crear_sectores(list_id, proyecto):

    raiz = crear(
        list_id,
        "🏘️ Sectores"
    )

    for sector in proyecto["sectores"]:

        nodo_sector = crear(
            list_id,
            f"🏘️ {sector['nombre']}",
            raiz
        )

        nodo_torres = crear(
            list_id,
            "🏢 Torres",
            nodo_sector
        )

        nodo_areas = crear(
            list_id,
            "🏢 Áreas Comunes",
            nodo_sector
        )

        crear_torres(
            list_id,
            nodo_torres,
            sector,
            proyecto
        )

        crear_areas_comunes(
            list_id,
            nodo_areas,
            sector,
            proyecto
        )