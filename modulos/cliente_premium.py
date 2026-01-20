from .cliente import Cliente
class ClientePremium(Cliente):
    def __init__(self, id_cliente, nombre, email, descuento):
        super().__init__(id_cliente, nombre, email)
        self.descuento = 40  # Descuento premium fijo

    def mostrar_info(self):
        # Implementación específica (Polimorfismo)
        return f"[PREMIUM] {self._Cliente__nombre}(ID:{self.id_cliente})- Beneficio: {self.descuento}% de descuento + {self.beneficio_exclusivo()}"

    def beneficio_exclusivo(self):
        return "Acceso a sala VIP activado."