#  Proyecto de Simulación Gestión de Gastos Personales

Este proyecto es una aplicación en Python que permite a los usuarios registrar sus gastos y generar reportes diarios, semanales y mensuales y generar reportes. El sistema también ofrece la opción de visualizar estos reportes en pantalla o guardarlos en un archivo JSON.

## 📑 Tabla de Contenidos

- [Instalación](#instalación)
- [Uso del Proyecto](#uso-del-proyecto)
- [Estructura del Proyecto](#estructura-del-proyecto)
- [Ejemplos](#ejemplos)

## ⚙️ Instalación

Se abre la terminal en la carpeta donde se encuentra el archivo del proyecto y ejecuta:

```bash
python3 main.py
```
## ▶️ Uso del Proyecto

- **Registro de nuevos gastos** con fecha, categoría y monto.
- **Listado de gastos** por categoría o por rango de fechas.
- **Cálculo del total de gastos** diario, semanal y mensual.
- **Generación de reportes** en formato JSON.


## 📂 Estructura del Proyecto
```bash
Proyecto_Python_PabonWilliamArdilaSantiago/
│
├── main.py                           
├── data/
│   └── data.json                      
├── funciones/
│   ├── funcionesJson.py              
│   ├── funcionesLoginSingUp.py       
│   ├── funcionesRegistarNuevosGastos.py 
│   ├── funcionesListarGastos.py     
│   ├── funcionesCalcularTotalGastos.py 
│   └── funcionesGenerarReportesGastos.py 
└── README.md                    
```
## ¿Como usar el proyecto?

Después de ejecutar main.py, el programa te mostrará un menú donde puedes:

1. Crear una cuenta

- Ingresa un nombre de usuario y contraseña para registrarte.

2. Iniciar sesión

- Usa tu nombre de usuario y contraseña para acceder.

3. Registrar un gasto

- Ingresa la cantidad, la categoría (por ejemplo: comida, transporte) y la fecha del gasto se agrega automáticamente.

4. Listar gastos

- Puedes ver tus gastos totales y filtrarlos por categoría o por fecha.

5. Calcular totales

- Puedes obtener el total gastado diario, semanal o mensual.

6. Generar reportes

- El programa crea un archivo JSON con un resumen de tus gastos o si lo prefieres puedes hacer que te muestre los reportes en la terminal.
```bash
=============================================
         Simulador de Gasto Diario           
=============================================
Seleccione una opción:

1. Registrar nuevo gasto
2. Listar gastos
3. Calcular total de gastos
4. Generar reporte de gastos
5. Salir
=============================================
Que acción deseas realizar 
> 1

=============================================
            Registrar Nuevo Gasto            
=============================================
Ingrese la información del gasto:

- Monto del gasto: 50
- Categoría (1. comida, 2. transporte, 3. entretenimiento, 4. otros): 1
- ¿Deseas agregar una descripción? (S/N): s
- Por favor escribe tu descripción: Almuerzo con amigos
Ingrese 'S' para guardar o 'C' para cancelar: s
Gasto registrado con éxito
=============================================

=============================================
         Simulador de Gasto Diario           
=============================================
Seleccione una opción:

1. Registrar nuevo gasto
2. Listar gastos
3. Calcular total de gastos
4. Generar reporte de gastos
5. Salir
=============================================
Que acción deseas realizar 
> 2

=============================================
                Listar Gastos                
=============================================
Seleccione una opción para filtrar los gastos:

1. Ver todos los gastos
2. Filtrar por categoría
3. Filtrar por rango de fechas
4. Regresar al menú principal
=============================================
Que acción deseas realizar 
> 1

[Gastos del usuario mostrados aquí...]
```

## ▶️ Link del video del proyecto
https://youtu.be/g04lMhPmQxA