from builders.builder_comunicaciones import crear_comunicaciones
from builders.builder_sectores import crear_sectores
from builders.builder_accesibilidad import crear_accesibilidad
from builders.builder_perimetral import crear_seguridad_perimetral
from builders.builder_seguridad import crear_seguridad_interna
from builders.builder_gestion import crear_gestion
from builders.builder_cierre import crear_cierre


def generar_proyecto(list_id, proyecto):

    # ------------------------------------------------------
    # Gestión
    # ------------------------------------------------------

    crear_gestion(list_id)

    # ------------------------------------------------------
    # Comunicaciones
    # ------------------------------------------------------

    crear_comunicaciones(
        list_id,
        proyecto
    )

    # ------------------------------------------------------
    # Accesibilidad
    # ------------------------------------------------------

    crear_accesibilidad(
        list_id,
        proyecto
    )

    # ------------------------------------------------------
    # Seguridad
    # ------------------------------------------------------

    crear_seguridad_perimetral(
        list_id,
        proyecto
    )

    crear_seguridad_interna(
        list_id,
        proyecto
    )

    # ------------------------------------------------------
    # Sectores
    # ------------------------------------------------------

    crear_sectores(
        list_id,
        proyecto
    )

    # ------------------------------------------------------
    # Cierre
    # ------------------------------------------------------

    crear_cierre(list_id)