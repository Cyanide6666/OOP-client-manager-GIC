import csv
from datetime import datetime
class ManejadorArchivos:
    @staticmethod
    def guardar_clientes_csv(ruta, lista_clientes):
        try:
            with open(ruta, mode='w', newline='', encoding='utf-8') as archivo:
                # Definimos las columnas (campos)
                campos = ['id', 'nombre', 'email', 'tipo']
                writer = csv.DictWriter(archivo, fieldnames=campos)
                writer.writeheader()
                
                for c in lista_clientes:
                    # Aquí usamos los getters que definistese define en la clase Cliente
                    writer.writerow({
                        'id': c.id_cliente, 
                        'nombre': c.nombre, 
                        'email': c.email,
                        'tipo': type(c).__name__
                    })
            print("Datos guardados en CSV correctamente.")
        except Exception as e:
            print(f" Error al guardar CSV: {e}")

    @staticmethod
    def generar_reporte_txt(ruta, lista_clientes):
        try:
            # Obtenemos la fecha y hora actual formateada
            ahora = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
            
            with open(ruta, mode='w', encoding='utf-8') as archivo:
                archivo.write("============================================================\n")
                archivo.write("                RESUMEN GENERAL DE CLIENTES\n")
                archivo.write(f"                Generado el: {ahora}\n") # Fecha añadida
                archivo.write("============================================================\n\n")
                
                if not lista_clientes:
                    archivo.write("No hay clientes registrados en el sistema.\n")
                else:
                    for c in lista_clientes:
                        # Polimorfismo: usamos el formato Nombre [ID] que creamos
                        archivo.write(f" • {c.mostrar_info()}\n")
                
                archivo.write("\n" + "-"*60 + "\n")
                archivo.write(f"TOTAL DE REGISTROS: {len(lista_clientes)}\n")
                archivo.write("============================================================\n")
        except Exception as e:
            print(f"Error al generar el archivo .txt: {e}")