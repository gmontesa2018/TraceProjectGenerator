# ==========================================================
# TRACE PROJECT GENERATOR
# Configurador - Resumen
# ==========================================================

from configurador.preguntas import pedir_opcion


def mostrar_resumen(proyecto):

    print()
    print("=" * 70)
    print("RESUMEN DEL PROYECTO")
    print("=" * 70)

    print()
    print(f"Proyecto : {proyecto['nombre']}")
    print(f"Cliente  : {proyecto['cliente']}")

    total_torres = 0
    total_uf = 0
    total_sum = 0
    total_gimnasios = 0

    print()
    print("=" * 70)
    print("SECTORES")
    print("=" * 70)

    for sector in proyecto["sectores"]:

        print()
        print("-" * 70)
        print(sector["nombre"])
        print("-" * 70)

        cantidad_torres = len(sector["torres"])

        cantidad_uf_sector = 0

        for torre in sector["torres"]:

            uf_torre = len(torre["ufs"])

            cantidad_uf_sector += uf_torre

            print()
            print(f"  {torre['nombre']}")

            for piso, cantidad in enumerate(torre["plantas"]):

                if piso == 0:
                    print(f"     PB : {cantidad}")
                else:
                    print(f"     P{piso} : {cantidad}")

            print(f"     Total UF : {uf_torre}")

        print()
        print(f"  Torres............. {cantidad_torres}")
        print(f"  UF................. {cantidad_uf_sector}")
        print(f"  SUM................ {sector['cantidad_sum']}")
        print(f"  Gimnasios.......... {sector['cantidad_gimnasios']}")

        total_torres += cantidad_torres
        total_uf += cantidad_uf_sector
        total_sum += sector["cantidad_sum"]
        total_gimnasios += sector["cantidad_gimnasios"]

    print()
    print("=" * 70)
    print("TOTALES")
    print("=" * 70)

    print(f"Torres..................... {total_torres}")
    print(f"UF......................... {total_uf}")
    print(f"SUM........................ {total_sum}")
    print(f"Gimnasios.................. {total_gimnasios}")

    print()
    print("=" * 70)
    print("ACCESIBILIDAD")
    print("=" * 70)

    print(f"Portones................... {proyecto['portones']}")
    print(f"Frentes de Portero......... {proyecto['cantidad_frentes_portero']}")
    print(f"Porteros Interiores........ {'SI' if proyecto['porteros_interiores'] else 'NO'}")
    print(f"Cerraduras Biométricas..... {'SI' if proyecto['cerraduras'] else 'NO'}")

    print()
    print("=" * 70)
    print("SEGURIDAD")
    print("=" * 70)

    print(f"Cerco...................... {'SI' if proyecto['cerco'] else 'NO'}")

    if proyecto["cerco"]:
        print(f"Metros..................... {proyecto['metros_cerco']}")

    print(f"Barreras IR................ {proyecto['barreras_ir']}")
    print(f"CCTV Perimetral............ {proyecto['camaras_perimetrales']}")
    print(f"CCTV Subsuelo.............. {proyecto['camaras_subsuelo']}")

    print()
    print("=" * 70)
    print(f"VMS........................ {proyecto['vms']}")

    print()
    print("=" * 70)

    opcion = pedir_opcion(
        "Confirmación",
        [
            "Crear Proyecto",
            "Modificar Datos",
            "Cancelar"
        ]
    )

    return opcion