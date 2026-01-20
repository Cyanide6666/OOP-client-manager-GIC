class Cliente:
    def __init__(self, id_cliente, nombre, email):
        self.__id_cliente = id_cliente
        self.__nombre = nombre
        self.__email = email

    @property
    def nombre(self): return self.__nombre
    @property
    def email(self): return self.__email
    @property
    def id_cliente(self): return self.__id_cliente

    def mostrar_info(self):
        return f"ID: {self.__id_cliente} | Nombre: {self.__nombre} | Email: {self.__email}"