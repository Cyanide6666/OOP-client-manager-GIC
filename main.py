import os
import logging

# Importaciones de tus módulos
from modulos.gestor_clientes import GestorClientes
from modulos.cliente_regular import ClienteRegular
from modulos.cliente_premium import ClientePremium
from modulos.excepciones import EmailInvalidoError
from modulos.validaciones import validar_email

# Configuración de Logs 
if not os.path.exists('logs'):
    os.makedirs('logs')

logging.basicConfig(
    filename='logs/app.log', 
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

# Función para Listar en Consola
def mostrar_lista_consola(gestor):
    clientes = gestor.listar_clientes()
    
    print("\n" + "="*60)
    print("           LISTADO GENERAL DE CLIENTES (GIC)")
    print("="*60)
    
    if not clientes:
        print("   [!] No hay clientes registrados en la base de datos.")
    else:
        # Polimorfismo: cada objeto se muestra según su clase
        for c in clientes:
            print(f" • {c.mostrar_info()}")
            
    print("="*60 + "\n")

# 3. Menú Principal
def menu_principal():
    # El gestor carga los datos del CSV al iniciarse
    gestor = GestorClientes()
    
    while True:
        print("--- GESTOR INTELIGENTE DE CLIENTES ---")
        print("1. Agregar Cliente")
        print("2. Listar Clientes En Terminal")
        print("3. Generar Reporte (.txt)")
        print("4. Eliminar Cliente por ID")
        print("5. Salir")
        
        opcion = input("\nSeleccione una opción: ")

        if opcion == "1":
            try:
                # Bloque de riesgo para estabilidad
                id_c = input("ID: ")
                nombre = input("Nombre: ")
                email = input("Email: ")
                
                # Validación de email)
                validar_email(email)
                
                tipo = input("¿Es Premium? (si/no): ").lower()
                if tipo == 'si':
                    nuevo = ClientePremium(id_c, nombre, email, 40)
                else:
                    nuevo = ClienteRegular(id_c, nombre, email)

                # El gestor guarda automáticamente en CSV 
                if gestor.agregar_cliente(nuevo):
                    logging.info(f"ALTA: Cliente {email} guardado.")
                    print(" Cliente guardado con éxito.")

            except EmailInvalidoError as e:
                print(f" ERROR DE DATOS: {e}")
                logging.error(f"ERROR: Email inválido - {email}")
            except Exception as e:
                print(f" ERROR INESPERADO: {e}")

        elif opcion == "2":
            mostrar_lista_consola(gestor)

        elif opcion == "3":
            gestor.exportar_reporte()
            print("Reporte generado con éxito en 'reportes/resumen_clientes.txt'")

        elif opcion == "4":
            id_borrar = input("Ingrese el ID a eliminar: ")
            if gestor.eliminar_cliente(id_borrar):
                print(f" Cliente {id_borrar} eliminado correctamente.")
                logging.info(f"BAJA: ID {id_borrar} eliminado.")
            else:
                print(f" No se encontró ningún cliente con el ID: {id_borrar}")

        elif opcion == "5":
            print("Cerrando sistema. CHAU PAPU LINCE :V")
            break

if __name__ == "__main__":
    # Asegurar que existan las carpetas necesarias 
    for carpeta in ['datos', 'reportes', 'logs']:
        if not os.path.exists(carpeta):
            os.makedirs(carpeta)
    menu_principal()