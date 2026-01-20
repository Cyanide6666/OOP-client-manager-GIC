class EmailInvalidoError(Exception):
    """Lanzada cuando el formato del email no es válido."""
    pass

class ClienteExistenteError(Exception):
    """Lanzada cuando se intenta duplicar un cliente."""
    pass

class ClienteNoEncontradoError(Exception):
    """Lanzada cuando un cliente no se encuentra en la base de datos."""
    pass