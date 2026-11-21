from clases.entidad import Entidad
from excepciones.errores import (
    ErrorReserva,
    ServicioNoDisponible
)


class Reserva(Entidad):
    def __init__(self, identificador, cliente, servicio, duracion):
        super().__init__(identificador)

        if cliente is None or servicio is None:
            raise ErrorReserva("La reserva requiere un cliente y un servicio.")

        if not isinstance(duracion, (int, float)) or isinstance(duracion, bool) or duracion <= 0:
            raise ErrorReserva("La duración debe ser un número positivo.")

        self._cliente = cliente
        self._servicio = servicio
        self._duracion = duracion
        self._estado = "Pendiente"
        self._costo = 0

    @property
    def estado(self):
        return self._estado

    @property
    def costo(self):
        return self._costo

    @property
    def cliente(self):
        return self._cliente

    @property
    def servicio(self):
        return self._servicio

    def confirmar(self, impuesto=19, descuento=0):
        if self._estado != "Pendiente":
            raise ErrorReserva("Solo se pueden confirmar reservas pendientes.")

        if not self._servicio.disponible:
            raise ServicioNoDisponible(
                f"El servicio {self._servicio.nombre} no está disponible."
            )

        try:
            self._costo = self._servicio.calcular_costo(
                self._duracion, impuesto, descuento
            )
        except Exception as error:
            raise ErrorReserva("No fue posible procesar el costo de la reserva.") from error

        self._estado = "Confirmada"
        return self._costo

    def cancelar(self):
        if self._estado == "Cancelada":
            raise ErrorReserva("La reserva ya está cancelada.")

        if self._estado == "Completada":
            raise ErrorReserva("No se puede cancelar una reserva completada.")

        self._estado = "Cancelada"

    def completar(self):
        if self._estado != "Confirmada":
            raise ErrorReserva("Solo se pueden completar reservas confirmadas.")

        self._estado = "Completada"

    def procesar(self):
        return self.confirmar()

    def describir(self):
        return (
            f"Reserva: {self.identificador} | "
            f"Cliente: {self.cliente.nombre} | "
            f"Servicio: {self.servicio.nombre} | "
            f"Duración: {self._duracion} | "
            f"Estado: {self.estado} | "
            f"Costo: ${self.costo:.2f}"
        )

    def __str__(self):
        return self.describir()