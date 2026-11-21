from clases.servicio import Servicio
from excepciones.errores import ErrorValidacion


class ReservaSala(Servicio):
    def calcular_costo(self, duracion, impuesto=0, descuento=0):
        self._validar_calculo(duracion, impuesto, descuento)

        subtotal = self.precio * duracion
        return round(subtotal * (1 + impuesto / 100) * (1 - descuento / 100), 2)

    def _validar_calculo(self, duracion, impuesto, descuento):
        if not isinstance(duracion, (int, float)) or isinstance(duracion, bool) or duracion <= 0:
            raise ErrorValidacion("La duración debe ser positiva.")

        if not 0 <= impuesto <= 100 or not 0 <= descuento <= 100:
            raise ErrorValidacion("Impuesto y descuento deben estar entre 0 y 100.")

    def describir(self):
        return f"Sala: {self.nombre} | Precio por hora: ${self.precio:.2f}"


class AlquilerEquipo(Servicio):
    def calcular_costo(self, duracion, impuesto=0, descuento=0):
        self._validar_calculo(duracion, impuesto, descuento)

        subtotal = self.precio * duracion
        return round(subtotal * (1 + impuesto / 100) * (1 - descuento / 100), 2)

    def _validar_calculo(self, duracion, impuesto, descuento):
        if not isinstance(duracion, (int, float)) or isinstance(duracion, bool) or duracion <= 0:
            raise ErrorValidacion("La duración debe ser positiva.")

        if not 0 <= impuesto <= 100 or not 0 <= descuento <= 100:
            raise ErrorValidacion("Impuesto y descuento deben estar entre 0 y 100.")

    def describir(self):
        return f"Equipo: {self.nombre} | Precio por unidad de tiempo: ${self.precio:.2f}"


class AsesoriaEspecializada(Servicio):
    def calcular_costo(self, duracion, impuesto=0, descuento=0):
        self._validar_calculo(duracion, impuesto, descuento)

        subtotal = self.precio * duracion
        return round(subtotal * (1 + impuesto / 100) * (1 - descuento / 100), 2)

    def _validar_calculo(self, duracion, impuesto, descuento):
        if not isinstance(duracion, (int, float)) or isinstance(duracion, bool) or duracion <= 0:
            raise ErrorValidacion("La duración debe ser positiva.")

        if not 0 <= impuesto <= 100 or not 0 <= descuento <= 100:
            raise ErrorValidacion("Impuesto y descuento deben estar entre 0 y 100.")

    def describir(self):
        return f"Asesoría: {self.nombre} | Precio por hora: ${self.precio:.2f}"