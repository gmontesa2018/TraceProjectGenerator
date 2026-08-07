from clickup import create_task


def crear(list_id, nombre, parent=None):

    tarea = create_task(
        list_id,
        nombre,
        parent
    )

    if tarea is None:
        return None

    return tarea["id"]