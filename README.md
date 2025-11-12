Readme Country management system:

Descripción del Programa
El Country Management System es una aplicación de consola desarrollada en Python que permite gestionar información sobre países de manera eficiente. El sistema ofrece funcionalidades completas para administrar datos demográficos y geográficos de diferentes naciones, incluyendo operaciones CRUD (Crear, Leer, Actualizar, Eliminar virtualmente mediante filtros), filtrado avanzado, ordenamiento y análisis estadístico.
El programa utiliza estructuras de datos fundamentales como listas y diccionarios, implementando un diseño modular que facilita el mantenimiento y la escalabilidad. Los datos se almacenan persistentemente en un archivo CSV, garantizando la preservación de la información entre sesiones.
Características Principales
•	Gestión Completa de Datos: Añadir, actualizar y buscar países
•	Sistema de Filtrado Avanzado: Por continente, rango de población y superficie
•	Múltiples Criterios de Ordenamiento: Nombre, población y superficie
•	Análisis Estadístico: Cálculo de promedios, valores extremos y distribución por continentes
•	Validación Robusta: Verificación de entradas para prevenir errores
•	Almacenamiento Persistente: Guardado automático en archivo CSV
Estructura de Datos
Cada país se almacena con la siguiente información:
•	Nombre (string): Nombre del país
•	Población (int): Número de habitantes
•	Superficie (int): Área en kilómetros cuadrados
•	Continente (string): Continente al que pertenece
Instrucciones de Uso
Requisitos del Sistema
•	Python 3.x instalado
•	Permisos de lectura/escritura en el directorio de trabajo
Instalación y Ejecución
1.	Buscar el archivo dentro de la carpeta
2.	Inicializarlo con su IDE de preferencia / terminal
3.	Ejecutar el código.
Flujo de Operaciones
1.	Inicialización: El programa carga automáticamente los datos existentes del archivo countries.csv
2.	Menú Principal: Se presenta un menú interactivo con 7 opciones
3.	Navegación: Seleccionar opciones numéricas para acceder a diferentes funcionalidades
4.	Persistencia: Los cambios se guardan automáticamente al modificar datos
Opciones del Menú
1.	Add Country: Añadir nuevo país con validación de datos
2.	Update Country: Modificar población y superficie de países existentes
3.	Search Country: Buscar países por nombre (coincidencia parcial)
4.	Filter Countries: Filtrar por continente, población o superficie
5.	Sort Countries: Ordenar por nombre, población o superficie
6.	Show Statistics: Mostrar análisis estadístico de los datos
7.	Exit: Salir del programa
Ejemplos de Entradas y Salidas
Tambien puede visualizarse el video explicativo en youtube: https://www.youtube.com/watch?v=FDp4JU8BAGM
Ejemplo 1: Añadir un Nuevo País
=== COUNTRY MANAGEMENT SYSTEM ===
1. Add country
2. Update country
3. Search country
4. Filter countries
5. Sort countries
6. Show statistics
7. Exit
Select option: 1

--- ADD NEW COUNTRY ---
Country name: Spain
Population: 47420000
Area (km²): 505990
Continent: Europe
Country added successfully
Ejemplo 2: Buscar un País
Select option: 3

--- SEARCH COUNTRY ---
Enter country name: arg

Found countries:
Name: Argentina, Population: 45376763, Area: 2780400 km², Continent: América
Ejemplo 3: Filtrar por Población
Select option: 4

--- FILTER OPTIONS ---
1. By continent
2. By population range
3. By area range
Select filter option: 2
Enter population range:
Minimum population: 100000000
Maximum population: 300000000

Countries with population between 100000000 and 300000000:
Name: Japan, Population: 125800000, Area: 377975 km², Continent: Asia
Name: Brazil, Population: 213993437, Area: 8515767 km², Continent: América
Ejemplo 4: Mostrar Estadísticas
Select option: 6

--- STATISTICS ---
Country with highest population: Brazil (213993437)
Country with lowest population: Germany (83149300)
Average population: 118429875.00
Average area: 2932291.00 km²

Countries by continent:
América: 2 countries
Asia: 1 countries
Europe: 1 countries
Ejemplo 5: Ordenar por Superficie
Select option: 5

--- SORT OPTIONS ---
1. By name
2. By population
3. By area
Select sort option: 3

Countries sorted by area:
Name: Japan, Population: 125800000, Area: 377975 km², Continent: Asia
Name: Germany, Population: 83149300, Area: 357022 km², Continent: Europe
Name: Argentina, Population: 45376763, Area: 2780400 km², Continent: América
Name: Brazil, Population: 213993437, Area: 8515767 km², Continent: América
Formato del Archivo CSV
El archivo countries.csv almacena los datos en formato plano sin encabezados:
text
Argentina,45376763,2780400,América
Japan,125800000,377975,Asia
Brazil,213993437,8515767,América
Germany,83149300,357022,Europe
Validaciones Implementadas
•	Campos Obligatorios: Ningún campo puede estar vacío
•	Números Positivos: Población y superficie deben ser valores ≥ 0
•	Existencia de País: No se permiten países duplicados
•	Rangos Válidos: En filtros por población y superficie
•	Manejo de Archivos: Creación automática si no existe
Notas Técnicas
•	El programa es case-insensitive en búsquedas y filtros
•	Los ordenamientos son ascendentes por defecto
•	No se requieren librerías externas, solo módulos estándar de Python
•	El encoding del archivo es UTF-8 para soportar caracteres internacionales
Estructura del Código
El programa sigue principios de modularidad con funciones especializadas:
•	load_countries() / save_countries(): Manejo de persistencia
•	validate_*(): Funciones de validación reutilizables
•	Funciones específicas para cada operación del menú
•	Separación clara entre lógica de negocio y interfaz de usuario

