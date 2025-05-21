from funciones.funcionesJson import *

def todosLosGastos(usuarioActivo):
    from tabulate import tabulate
    datos = abrirJSON()
   
    for usuario in datos[0]["listaUsuarios"]:
          if usuario["nombre"] == usuarioActivo:
              tablaGastos = []
              for gasto in usuario["gastos"]:
                    monto = gasto["monto"]
                    categoria = gasto["categoria"]
                    descripcion = gasto["descripcion"]
                    fecha = gasto["fecha"]
                    tablaGastos.append([monto, categoria, descripcion, fecha])
                
    print(tabulate(tablaGastos, headers=["Monto", "Categoría", "Descripción", "Fecha"], tablefmt="grid"))
             
def filtarCategoria(usuarioActivo,buscarCategoria): 
    from tabulate import tabulate
    datos = abrirJSON()
    tablaCategoria = []

    for usuario in datos[0]["listaUsuarios"]:
        if usuario["nombre"] == usuarioActivo:
         if (buscarCategoria == 1):
             buscarCategoria = "Comida"
             for gasto in usuario["gastos"]:
                 if gasto["categoria"] == buscarCategoria:
                    monto = gasto["monto"]
                    categoria = gasto["categoria"]
                    descripcion = gasto["descripcion"]
                    fecha = gasto["fecha"]
                    tablaCategoria.append([monto, categoria, descripcion, fecha])
                    
         elif (buscarCategoria == 2):
               
               buscarCategoria = "Transporte"
               for gasto in usuario["gastos"]:
                 if gasto["categoria"] == buscarCategoria:
                    monto = gasto["monto"]
                    categoria = gasto["categoria"]
                    descripcion = gasto["descripcion"]
                    fecha = gasto["fecha"]
                    tablaCategoria.append([monto, categoria, descripcion, fecha])
                    
         elif (buscarCategoria == 3):
             
               buscarCategoria = "Entretenimiento"
               for gasto in usuario["gastos"]:
                 if gasto["categoria"] == buscarCategoria:
                    monto = gasto["monto"]
                    categoria = gasto["categoria"]
                    descripcion = gasto["descripcion"]
                    fecha = gasto["fecha"]
                    tablaCategoria.append([monto, categoria, descripcion, fecha])
                    
         elif (buscarCategoria == 4):
             
               buscarCategoria = "Otros"
               for gasto in usuario["gastos"]:
                 if gasto["categoria"] == buscarCategoria:
                    monto = gasto["monto"]
                    categoria = gasto["categoria"]
                    descripcion = gasto["descripcion"]
                    fecha = gasto["fecha"]
                    tablaCategoria.append([monto, categoria, descripcion, fecha])
    
    print(tabulate(tablaCategoria, headers=["Monto", "Categoría", "Descripción", "Fecha"], tablefmt="grid"))
    
def filtrarPorRangoFechas(usuarioActivo):
    
    from datetime import datetime
    from tabulate import tabulate
    datos = abrirJSON()
    tablaFechas = []

    fechaInicio = input("Ingrese la fecha inicial (YYYY-MM-DD): ")
    fechaFin = input("Ingrese la fecha final (YYYY-MM-DD): ")

   
    fechaInicio = datetime.strptime(fechaInicio, "%Y-%m-%d").date()
    fechaFin = datetime.strptime(fechaFin, "%Y-%m-%d").date()

    for usuario in datos[0]["listaUsuarios"]:
        if usuario["nombre"] == usuarioActivo:
            for gasto in usuario["gastos"]:
                fechaGasto = datetime.strptime(gasto["fecha"], "%Y-%m-%d").date()
                if fechaInicio <= fechaGasto <= fechaFin:
                    monto = gasto["monto"]
                    categoria = gasto["categoria"]
                    descripcion = gasto["descripcion"]
                    fecha = gasto["fecha"]
                    tablaFechas.append([monto, categoria, descripcion, fecha])                    
                
    print(tabulate(tablaFechas, headers=["Monto", "Categoría", "Descripción", "Fecha"], tablefmt="grid"))   