import csv
import logging
from .archivos import ManejadorArchivos
from .cliente_regular import ClienteRegular
from .cliente_premium import ClientePremium
from .cliente_corporativo import ClienteCorporativo

class GestorClientes:
    def __init__(self):
        self.clientes = [] #
        self.ruta_csv = "datos/clientes.csv" #
        # Cargamos los datos apenas se crea el cliente para no perder los datos del CSV existente 
        self.cargar_clientes_desde_csv() #

    def cargar_clientes_desde_csv(self):
        try:
            with open(self.ruta_csv, mode='r', encoding='utf-8') as archivo: #
                lector = csv.DictReader(archivo) #
                for fila in lector: #
                    nuevo = None #
                    tipo = fila['tipo']
                    
                    # Coincidimos con los nombres exactos del CSV
                    if tipo == 'ClientePremium':
                        nuevo = ClientePremium(fila['id'], fila['nombre'], fila['email'], 40)
                    elif tipo == 'ClienteRegular':
                        nuevo = ClienteRegular(fila['id'], fila['nombre'], fila['email'])
                    elif tipo == 'ClienteCorporativo':
                        nuevo = ClienteCorporativo(fila['id'], fila['nombre'], fila['email'])
                    if nuevo: 
                        self.clientes.append(nuevo) 
        except FileNotFoundError: 
            logging.warning("No se encontró el archivo de datos.") 

    def listar_clientes(self):
        return self.clientes

    def agregar_cliente(self, nuevo):
        # Evitamos duplicados para no corromper el CSV
        if any(str(c.id_cliente) == str(nuevo.id_cliente) for c in self.clientes):
            print(f" El ID {nuevo.id_cliente} ya existe.")
            return False
            
        self.clientes.append(nuevo) 
        # Guardamos la lista completa 
        ManejadorArchivos.guardar_clientes_csv(self.ruta_csv, self.clientes) #
        return True

    def eliminar_cliente(self, id_borrar):
        original_count = len(self.clientes)
        self.clientes = [c for c in self.clientes if str(c.id_cliente) != str(id_borrar)]
        
        if len(self.clientes) < original_count:
            # Sobrescribimos el CSV con la lista actualizada 
            ManejadorArchivos.guardar_clientes_csv(self.ruta_csv, self.clientes)
            return True
        return False

    def exportar_reporte(self):
        ruta = "reportes/resumen_clientes.txt"
        # Llamamos al método estático para generar el reporte
        ManejadorArchivos.generar_reporte_txt(ruta, self.clientes)