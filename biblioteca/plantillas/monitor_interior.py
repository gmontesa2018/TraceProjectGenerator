from builders.helpers import crear
from biblioteca.plantillas.comun import tareas_basicas


def aplicar(list_id, parent):

    tareas_basicas(
        list_id,
        parent
    )

    crear(
        list_id,
        "📱 Vinculación App Hik-Connect",
        parent
    )

    crear(
        list_id,
        "🎥 Prueba Audio y Video",
        parent
    )