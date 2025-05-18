from tabulate import tabulate
from funciones.funciones import *
from datetime import datetime

usuarioActivo = iniciarSesion()
if not usuarioActivo:
    exit()

boolianito = True

while(boolianito):

 print("=============================================")
 print("         Simulador de Gasto Diario           ")
 print("=============================================")
 print("Seleccione una opción:\n")
 print("1. Registrar nuevo gasto")
 print("2. Listar gastos")
 print("3. Calcular total de gastos")
 print("4. Generar reporte de gastos")
 print("5. Salir")
 print("=============================================")
 
 opcion = int(input("Que accion deseas realizar \n"))

 if (opcion == 1):
     
  print("=============================================")
  print("            Registrar Nuevo Gasto            ")
  print("=============================================")
  print("Ingrese la información del gasto:\n")
  montoDelGasto = int(input("- Monto del gasto:"))
  categoria = int(input("- Categoría (1. comida, 2. transporte, 3. entretenimiento, 4. otros):"))
  descripcion = input("- ¿Deseas agregar una descripcion? (S/N):").lower()
  if (descripcion == "s"):
      descripcion = input("- Porfavor escribe tu descripcion:")
  elif(descripcion == "n"):
      descripcion = "Sin ninguna descripcion"
  fechaRegistro = datetime.now().strftime("%Y-%m-%d")
  guardar = input("Ingrese 'S' para guardar o 'C' para cancelar:").lower()
  registarNuevoGasto(guardar, usuarioActivo, montoDelGasto, categoria, descripcion, fechaRegistro)
  print("=============================================")
  
 if (opcion == 2):
     
  print("=============================================")
  print("                Listar Gastos                ")
  print("=============================================")
  print("Seleccione una opción para filtrar los gastos:\n")
  print("1. Ver todos los gastos")
  print("2. Filtrar por categoría")
  print("3. Filtrar por rango de fechas")
  print("4. Regresar al menú principal")
  print("=============================================")
  
 if (opcion == 3):
     
  print("=============================================")
  print("          Calcular Total de Gastos           ")
  print("=============================================")
  print("Seleccione el periodo de cálculo:\n")
  print("1. Calcular total diario")
  print("2. Calcular total semanal")
  print("3. Calcular total mensual")
  print("4. Regresar al menú principal")
  print("=============================================")
  
 if (opcion == 4):
     
  print("=============================================")
  print("           Generar Reporte de Gastos         ")
  print("=============================================")
  print("Seleccione el tipo de reporte:\n")
  print("1. Reporte diario")
  print("2. Reporte semanal")
  print("3. Reporte mensual")
  print("4. Regresar al menú principal")
  print("=============================================")
  
 if opcion == 5:
    cerrarPrograma = input("¿Desea salir del programa? (S/N): ").lower()
    if (cerrarPrograma == "s"):
        print("Gracias por usar mi programa, hasta luego.")
        boolianito = False
        
    elif (cerrarPrograma == "n"):
        boolianito = True