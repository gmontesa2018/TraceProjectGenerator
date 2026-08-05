# ==========================================================
# TRACE PROJECT GENERATOR
# Biblioteca - Infraestructura
# ==========================================================

from .procedimientos import Procedimiento


PROCEDIMIENTOS_INFRAESTRUCTURA = []


def agregar(procedimiento):
    PROCEDIMIENTOS_INFRAESTRUCTURA.append(procedimiento)


# ==========================================================
# INF-001
# ==========================================================

p = Procedimiento(
    codigo="INF-001",
    nombre="Instalación de Rack",
    categoria="Infraestructura",
    especialidad="Infraestructura",
    tiempo_estimado=120
)

agregar(p)


# ==========================================================
# INF-002
# ==========================================================

p = Procedimiento(
    codigo="INF-002",
    nombre="Instalación de Patch Panel",
    categoria="Infraestructura",
    especialidad="Infraestructura",
    tiempo_estimado=60
)

agregar(p)


# ==========================================================
# INF-003
# ==========================================================

p = Procedimiento(
    codigo="INF-003",
    nombre="Instalación de Bandejas",
    categoria="Infraestructura",
    especialidad="Infraestructura",
    tiempo_estimado=90
)

agregar(p)


# ==========================================================
# INF-004
# ==========================================================

p = Procedimiento(
    codigo="INF-004",
    nombre="Instalación de Switch",
    categoria="Infraestructura",
    especialidad="Infraestructura",
    tiempo_estimado=45
)

agregar(p)


# ==========================================================
# INF-005
# ==========================================================

p = Procedimiento(
    codigo="INF-005",
    nombre="Instalación de UPS",
    categoria="Infraestructura",
    especialidad="Infraestructura",
    tiempo_estimado=45
)

agregar(p)


# ==========================================================
# INF-006
# ==========================================================

p = Procedimiento(
    codigo="INF-006",
    nombre="Organización de Cableado",
    categoria="Infraestructura",
    especialidad="Infraestructura",
    tiempo_estimado=90
)

agregar(p)


# ==========================================================
# INF-007
# ==========================================================

p = Procedimiento(
    codigo="INF-007",
    nombre="Rotulado",
    categoria="Infraestructura",
    especialidad="Infraestructura",
    tiempo_estimado=30
)

agregar(p)


# ==========================================================
# INF-008
# ==========================================================

p = Procedimiento(
    codigo="INF-008",
    nombre="Control de Calidad (QA)",
    categoria="Infraestructura",
    especialidad="Infraestructura",
    tiempo_estimado=30
)

agregar(p)