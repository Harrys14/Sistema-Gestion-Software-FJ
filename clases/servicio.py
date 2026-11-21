from abc import abstractmethod
from clases.entidad import Entidad
from excepciones.errores import ErrorValidacion


class Servicio(Entidad):
    def __init__(self, identificador, nombre, precio, disponible=True):
        super().__init__(identificador)

        self._nombre = nombre
        self._precio = precio
        self._disponible = disponible

        self.validar_parametros()

    @property
    def nombre(self):
        return self._nombre

    @property
    def precio(self):
        return self._precio

    @property
    def disponible(self):
        return self._disponible

    def validar_parametros(self):
        if not self._nombre or not self._nombre.strip():
            raise ErrorValidacion("El nombre del servicio es obligatorio.")

        if not isinstance(self._precio, (int, float)) or isinstance(self._precio, bool) or self._precio <= 0:
            raise ErrorValidacion("El precio debe ser un número positivo.")

        if not isinstance(self._disponible, bool):
            raise ErrorValidacion("La disponibilidad debe ser verdadera o falsa.")

    def cambiar_disponibilidad(self, estado):
        if not isinstance(estado, bool):
            raise ErrorValidacion("El estado debe ser booleano.")

        self._disponible = estado

    @abstractmethod
    def calcular_costo(self, duracion, impuesto=0, descuento=0):
        pass

    @abstractmethod
    def describir(self):
        pass