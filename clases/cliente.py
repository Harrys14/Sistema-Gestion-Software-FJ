
from clases.entidad import Entidad
from excepciones.errores import ErrorCliente, ErrorValidacion


class Cliente(Entidad):
    def __init__(self, identificador, nombre, correo, telefono):
        super().__init__(identificador)

        self._nombre = nombre
        self._correo = correo
        self._telefono = telefono

        self.validar_datos()

    def validar_datos(self):
        if not isinstance(self._nombre, str) or len(self._nombre.strip()) < 3:
            raise ErrorCliente(
                "El nombre debe tener al menos 3 caracteres."
            )

        if not isinstance(self._correo, str) or "@" not in self._correo or "." not in self._correo:
            raise ErrorValidacion("El correo electrónico no es válido.")

        if not str(self._telefono).isdigit() or len(str(self._telefono)) < 7:
            raise ErrorValidacion(
                "El teléfono debe contener al menos 7 dígitos."
            )

    @property
    def nombre(self):
        return self._nombre

    @property
    def correo(self):
        return self._correo

    @property
    def telefono(self):
        return self._telefono

    def describir(self):
        return (
            f"Cliente: {self._nombre} | "
            f"Correo: {self._correo} | "
            f"Teléfono: {self._telefono}"
        )

    def __str__(self):
        return self.describir()
