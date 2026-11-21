class ErrorSistema(Exception):
    """Excepción base del sistema."""
    pass


class ErrorValidacion(ErrorSistema):
    """Error cuando los datos ingresados no son válidos."""
    pass


class ErrorServicio(ErrorSistema):
    """Error relacionado con los servicios."""
    pass


class ErrorReserva(ErrorSistema):
    """Error durante la gestión de reservas."""
    pass


class ErrorCliente(ErrorSistema):
    """Error durante el registro o gestión de clientes."""
    pass


class ServicioNoDisponible(ErrorServicio):
    """Error cuando un servicio no está disponible."""
    pass