
from funciones.funciones import *
from datetime import datetime
hola=39393
continuar = True
while(continuar):
 print("Bienvenido a mi programa para calcular gastos\n")
 print("1. Crear cuenta")
 print("2. Iniciar sesion")
 iniciarCrear = int(input())

 if (iniciarCrear == 1):
    crearCuenta()
    continuar = True
 

 if (iniciarCrear == 2):
   continuar = False
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
  
  opcionListarGastos = int(input("Que accion deseas realizar \n"))
  if (opcionListarGastos == 1):
      todosLosGastos(usuarioActivo)
  elif (opcionListarGastos == 2):
        buscarCategoria = int((input("Por cua tipo de categoria deseas filtar (1. comida, 2. transporte, 3. entretenimiento, 4. otros):")))
        filtarCategoria(usuarioActivo,buscarCategoria)
  elif (opcionListarGastos == 3):
        filtrarPorRangoFechas(usuarioActivo)
  
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
  
  opcionCalcularTotalDeGastos = int(input("Que accion deseas realizar \n"))
  if (opcionCalcularTotalDeGastos == 1):
      calcularTotalDiario(usuarioActivo)
  elif (opcionCalcularTotalDeGastos == 2):
       calcularTotalSemanal(usuarioActivo)
  elif (opcionCalcularTotalDeGastos == 3):
       calcularTotalMensual(usuarioActivo)

  
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
  
  opcionGenerarReporteGastos = int(input("Que accion deseas realizar \n"))
  
  if (opcionGenerarReporteGastos == 1):
      calcularTotalDiario(usuarioActivo)
  elif (opcionGenerarReporteGastos== 2):
       calcularTotalSemanal(usuarioActivo)
  elif ( opcionGenerarReporteGastos == 3):
       calcularTotalMensual(usuarioActivo)
  
 if opcion == 5:
    cerrarPrograma = input("¿Desea salir del programa? (S/N): ").lower()
    if (cerrarPrograma == "s"):
        print("Gracias por usar mi programa, hasta luego.")
        boolianito = False
        
    elif (cerrarPrograma == "n"):
        boolianito = True