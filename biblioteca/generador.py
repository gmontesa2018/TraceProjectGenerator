from clickup import create_task


def generar_categoria(list_id, parent_id, nombre_categoria, procedimientos):
    """
    Crea una categoría y todos los procedimientos de la biblioteca.
    """

    print(f"Creando: {nombre_categoria}")

    categoria = create_task(
        list_id=list_id,
        name=nombre_categoria,
        parent=parent_id
    )

    if categoria is None:
        raise Exception(f"No se pudo crear la categoría: {nombre_categoria}")

    for proc in procedimientos:

        nombre = f"{proc.codigo} - {proc.nombre}"

        print(f"Creando: {nombre}")

        tarea = create_task(
            list_id=list_id,
            name=nombre,
            parent=categoria["id"]
        )

        if tarea is None:
            raise Exception(f"No se pudo crear el procedimiento: {nombre}")

    return categoria