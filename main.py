import logging
from pathlib import Path

from clases.cliente import Cliente
from clases.servicios_especializados import (
    ReservaSala,
    AlquilerEquipo,
    AsesoriaEspecializada
)
from clases.reserva import Reserva


# CONFIGURACIÓN DEL SISTEMA DE LOGS

RUTA_LOGS = Path(__file__).parent / "logs"
RUTA_LOGS.mkdir(exist_ok=True)

logging.basicConfig(
    filename=RUTA_LOGS / "eventos.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    encoding="utf-8",
    force=True
)

logger = logging.getLogger(__name__)

clientes = []
servicios = []
reservas = []


def ejecutar_operacion(descripcion, funcion):
    print(f"\n--- {descripcion} ---")
    logger.info("Iniciando operación: %s", descripcion)

    try:
        resultado = funcion()

    except Exception as error:
        print(f"ERROR: {error}")
        logger.exception("Error en la operación: %s", descripcion)

    else:
        print(f"RESULTADO: {resultado}")
        logger.info("Operación completada: %s", descripcion)

    finally:
        print("Operación finalizada.")
        logger.info("Finalización: %s", descripcion)


# FUNCIONES DE PRUEBA

def registrar_cliente():
    cliente = Cliente(
        "C001",
        "Carlos Ramirez",
        "carlos@gmail.com",
        "3001234567"
    )
    clientes.append(cliente)
    return cliente.describir()


def registrar_cliente_dos():
    cliente = Cliente(
        "C002",
        "Maria Torres",
        "maria@gmail.com",
        "3101234567"
    )
    clientes.append(cliente)
    return cliente.describir()


def registrar_cliente_invalido():
    cliente = Cliente(
        "C003",
        "Ana",
        "correoincorrecto",
        "123"
    )
    clientes.append(cliente)
    return cliente.describir()


def crear_sala():
    servicio = ReservaSala("S001", "Sala de reuniones", 50000)
    servicios.append(servicio)
    return servicio.describir()


def crear_equipo():
    servicio = AlquilerEquipo("S002", "Proyector", 30000)
    servicios.append(servicio)
    return servicio.describir()


def crear_asesoria():
    servicio = AsesoriaEspecializada("S003", "Asesoria tecnica", 80000)
    servicios.append(servicio)
    return servicio.describir()


def crear_servicio_invalido():
    servicio = ReservaSala("S004", "Sala incorrecta", -5000)
    servicios.append(servicio)
    return servicio.describir()


def crear_reserva_sala():
    reserva = Reserva("R001", clientes[0], servicios[0], 2)
    reservas.append(reserva)
    costo = reserva.confirmar()
    return f"{reserva.describir()} | Total: ${costo:.2f}"


def crear_reserva_equipo():
    reserva = Reserva("R002", clientes[1], servicios[1], 3)
    reservas.append(reserva)
    costo = reserva.confirmar(impuesto=19, descuento=10)
    return f"{reserva.describir()} | Total: ${costo:.2f}"


def crear_reserva_asesoria():
    reserva = Reserva("R003", clientes[0], servicios[2], 1)
    reservas.append(reserva)
    costo = reserva.confirmar(impuesto=19, descuento=5)
    return f"{reserva.describir()} | Total: ${costo:.2f}"


def crear_reserva_invalida():
    reserva = Reserva("R004", clientes[0], servicios[0], -2)
    reservas.append(reserva)
    return reserva.describir()


def intentar_reserva_no_disponible():
    servicio = ReservaSala(
        "S005",
        "Sala ocupada",
        60000,
        disponible=False
    )
    servicios.append(servicio)

    reserva = Reserva("R005", clientes[0], servicio, 2)
    reservas.append(reserva)

    return reserva.confirmar()


def cancelar_reserva():
    reservas[0].cancelar()
    return f"Reserva {reservas[0].identificador} cancelada."


def completar_reserva():
    reservas[1].completar()
    return f"Reserva {reservas[1].identificador} completada."


def intentar_confirmar_reserva_cancelada():
    return reservas[0].confirmar()


def calcular_costo_alternativo():
    # Ejemplo de cálculo con diferentes parámetros.
    return servicios[0].calcular_costo(
        duracion=3,
        impuesto=19,
        descuento=15
    )


def mostrar_sistema():
    print("\n========== RESUMEN DEL SISTEMA ==========")

    print("\nCLIENTES:")
    for cliente in clientes:
        print(cliente.describir())

    print("\nSERVICIOS:")
    for servicio in servicios:
        print(servicio.describir())

    print("\nRESERVAS:")
    for reserva in reservas:
        print(reserva.describir())

    print("\n=========================================")


def ejecutar_sistema():
    print("=" * 55)
    print(" SISTEMA INTEGRAL DE GESTION - SOFTWARE FJ")
    print("=" * 55)

    operaciones = [
        ("1. Registrar cliente válido", registrar_cliente),
        ("2. Registrar segundo cliente", registrar_cliente_dos),
        ("3. Intentar registrar cliente inválido", registrar_cliente_invalido),
        ("4. Crear servicio de reserva de salas", crear_sala),
        ("5. Crear servicio de alquiler de equipos", crear_equipo),
        ("6. Crear servicio de asesoría", crear_asesoria),
        ("7. Intentar crear servicio con precio negativo", crear_servicio_invalido),
        ("8. Crear reserva de sala", crear_reserva_sala),
        ("9. Crear reserva de equipo", crear_reserva_equipo),
        ("10. Crear reserva de asesoría", crear_reserva_asesoria),
        ("11. Intentar crear reserva con duración negativa", crear_reserva_invalida),
        ("12. Intentar reservar un servicio no disponible", intentar_reserva_no_disponible),
        ("13. Calcular costo con descuento", calcular_costo_alternativo),
        ("14. Cancelar una reserva", cancelar_reserva),
        ("15. Completar una reserva", completar_reserva),
        ("16. Intentar confirmar una reserva cancelada", intentar_confirmar_reserva_cancelada)
    ]

    for descripcion, funcion in operaciones:
        ejecutar_operacion(descripcion, funcion)

    mostrar_sistema()

    print("\nSistema ejecutado correctamente.")
    print("Los eventos y errores fueron registrados en logs/eventos.log.")


if __name__ == "__main__":
    ejecutar_sistema()