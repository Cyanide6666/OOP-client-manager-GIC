## Client Manager (GIC)
El proyecto GIC implementa una arquitectura orientada a objetos donde se destaca el uso de polimorfismo para gestionar distintos tipos de beneficios por cliente. Se priorizó la persistencia de datos mediante un archivo CSV que actúa como base de datos dinámica y la generación de reportes TXT con marca temporal para auditoría. Además, se incluyeron bloques de manejo de excepciones para garantizar la estabilidad del sistema ante ingresos de datos inválidos.

## Estructura de proyecto
main.py: Punto de entrada con menú interactivo en consola

modulos/: Contiene la lógica de negocio, herencia de clases (Regular, Premium, Corporativo) y manejo de excepciones

datos/: Almacenamiento persistente en formato CSV

reportes/: Generación de informes detallados en formato TXT con marca temporal

logs/: Registro de todas las operaciones realizadas

## Características
Polimorfismo: Cada tipo de cliente muestra sus beneficios específicos mediante el método mostrar_info()

Formato Visual: Los clientes se listan con el formato solicitado: Nombre [ID]

Persistencia: Cualquier cambio se sincroniza automáticamente con el archivo clientes.csv

Validaciones: Uso de expresiones regulares para validar correos electrónicos y bloques try-except para prevenir caídas del sistema

## Instrucciones de uso
1.- Abrir una terminal en la carpeta raíz del proyecto.

2.- Ejecutar el comando: python main.py.

2.- Utilizar las opciones del menú para interactuar con la base de datos.






