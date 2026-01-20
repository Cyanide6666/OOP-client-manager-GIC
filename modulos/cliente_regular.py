from .cliente import Cliente

class ClienteRegular(Cliente):
    def __init__(self, id_cliente, nombre, email):
        super().__init__(id_cliente, nombre, email)
        self.descuento = 0  # Descuento regular fijo

    def mostrar_info(self):
        # Polimorfismo: cada clase muestra su info
        return f"[REGULAR] {self._Cliente__nombre} (ID:{self.id_cliente}) - Beneficio: {self.descuento}% de descuento"