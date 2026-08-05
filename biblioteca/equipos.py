# ==========================================================
# TRACE PROJECT GENERATOR
# Biblioteca de Equipos
# ==========================================================


class Equipo:

    def __init__(
        self,
        categoria,
        marca,
        modelo,
        descripcion=""
    ):

        self.categoria = categoria

        self.marca = marca

        self.modelo = modelo

        self.descripcion = descripcion

        self.manual = ""

        self.firmware = ""

        self.observaciones = ""

        self.procedimientos = []

        self.materiales = []

        self.accesorios = []

        self.compatibles = []


    # ======================================================
    # DOCUMENTACIÓN
    # ======================================================

    def set_manual(self, archivo):

        self.manual = archivo


    def set_firmware(self, version):

        self.firmware = version


    def set_observaciones(self, texto):

        self.observaciones = texto


    # ======================================================
    # PROCEDIMIENTOS
    # ======================================================

    def agregar_procedimiento(self, codigo):

        self.procedimientos.append(codigo)


    # ======================================================
    # MATERIALES
    # ======================================================

    def agregar_material(self, material):

        self.materiales.append(material)


    # ======================================================
    # ACCESORIOS
    # ======================================================

    def agregar_accesorio(self, accesorio):

        self.accesorios.append(accesorio)


    # ======================================================
    # COMPATIBILIDAD
    # ======================================================

    def agregar_compatible(self, modelo):

        self.compatibles.append(modelo)


    # ======================================================
    # RESUMEN
    # ======================================================

    def resumen(self):

        print("=" * 60)

        print(self.marca, self.modelo)

        print()

        print("Categoría :", self.categoria)

        if self.descripcion:
            print("Descripción :", self.descripcion)

        if self.firmware:
            print("Firmware :", self.firmware)

        if self.manual:
            print("Manual :", self.manual)

        print()

        print("Procedimientos")

        for x in self.procedimientos:
            print("   •", x)

        print()

        print("Materiales")

        for x in self.materiales:
            print("   •", x)

        print()

        print("Accesorios")

        for x in self.accesorios:
            print("   •", x)

        print()

        print("Compatibles")

        for x in self.compatibles:
            print("   •", x)

        print("=" * 60)