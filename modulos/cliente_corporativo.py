from .cliente import Cliente
class ClienteCorporativo(Cliente):
    def __init__(self, id_cliente, nombre, email):
        # Inicializamos la base
        super().__init__(id_cliente, nombre, email)
        # Atributos específicos de corporativo
        self.descuento = 15  # Descuento corporativo fijo


    def mostrar_info(self):
        # Polimorfismo: implementamos la versión para empresas
        return f"[CORPORATIVO] {self._Cliente__nombre} (ID:{self.id_cliente}) - Beneficio: {self.descuento}% de descuento + {self.beneficio_exclusivo()}"

    def beneficio_exclusivo(self):
        # Método específico requerido para clientes corporativos
        return "Facturación con cuenta corriente a 30 días."