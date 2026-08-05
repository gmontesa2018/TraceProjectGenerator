# ==========================================================
# TRACE PROJECT GENERATOR
# Biblioteca de Procedimientos
# ==========================================================


class Procedimiento:

    def __init__(
        self,
        codigo,
        nombre,
        categoria,
        especialidad,
        tiempo_estimado=0,
        version="1.0"
    ):

        self.codigo = codigo
        self.nombre = nombre
        self.categoria = categoria
        self.especialidad = especialidad
        self.tiempo_estimado = tiempo_estimado
        self.version = version

        self.descripcion = ""

        self.materiales = []

        self.herramientas = []

        self.checklist = []

        self.qa = []

        self.observaciones = []

        self.predecesoras = []


    # =======================================================
    # DESCRIPCIÓN
    # =======================================================

    def set_descripcion(self, texto):

        self.descripcion = texto


    # =======================================================
    # MATERIALES
    # =======================================================

    def agregar_material(self, material):

        self.materiales.append(material)


    # =======================================================
    # HERRAMIENTAS
    # =======================================================

    def agregar_herramienta(self, herramienta):

        self.herramientas.append(herramienta)


    # =======================================================
    # CHECKLIST
    # =======================================================

    def agregar_check(self, texto):

        self.checklist.append(texto)


    # =======================================================
    # QA
    # =======================================================

    def agregar_qa(self, texto):

        self.qa.append(texto)


    # =======================================================
    # OBSERVACIONES
    # =======================================================

    def agregar_observacion(self, texto):

        self.observaciones.append(texto)


    # =======================================================
    # PREDECESORAS
    # =======================================================

    def agregar_predecesora(self, codigo):

        self.predecesoras.append(codigo)


    # =======================================================
    # RESUMEN
    # =======================================================

    def resumen(self):

        print("=" * 60)

        print(self.codigo)

        print(self.nombre)

        print()

        print("Categoría:", self.categoria)

        print("Especialidad:", self.especialidad)

        print("Tiempo:", self.tiempo_estimado, "min")

        print()

        print("Materiales")

        for x in self.materiales:
            print("  •", x)

        print()

        print("Herramientas")

        for x in self.herramientas:
            print("  •", x)

        print()

        print("Checklist")

        for x in self.checklist:
            print("  □", x)

        print()

        print("QA")

        for x in self.qa:
            print("  □", x)

        print("=" * 60)