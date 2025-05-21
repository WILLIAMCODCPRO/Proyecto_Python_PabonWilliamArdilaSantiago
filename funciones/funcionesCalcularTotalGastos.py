from funciones.funcionesJson import *

def calcularTotalDiario(usuarioActivo):
    from tabulate import tabulate
    datos = abrirJSON()
    tablaDiario = {}  
    
    for usuario in datos[0]["listaUsuarios"]:
        if usuario["nombre"] == usuarioActivo:
             for gasto in usuario["gastos"]:
                fecha = gasto["fecha"]
                monto = gasto["monto"]
                if fecha in tablaDiario:
                    tablaDiario[fecha] += monto
                else:
                    tablaDiario[fecha] = monto

    
    tabla = [[fecha, monto] for fecha, monto in tablaDiario.items()]
    print(tabulate(tabla, headers=["Fecha", "Total Gastado"], tablefmt="grid"))
    
    totalCategoria = {}
    for gasto in usuario["gastos"]:
     categoria = gasto["categoria"]
     monto = gasto["monto"]
     if categoria in totalCategoria:
        totalCategoria[categoria] += monto
     else:
        totalCategoria[categoria] = monto

    tablaCategoria = [[categoria, monto] for categoria, monto in totalCategoria.items()]
    print("\nGastos acumulados por categoría:")
    print(tabulate(tablaCategoria, headers=["Categoría", "Total"], tablefmt="grid"))
    
def calcularTotalSemanal(usuarioActivo):
    from datetime import datetime
    from tabulate import tabulate
    datos = abrirJSON()
    tablaSemanal = {}

    for usuario in datos[0]["listaUsuarios"]:
        if usuario["nombre"] == usuarioActivo:
            for gasto in usuario["gastos"]:
                fechaGasto = gasto["fecha"]
                montoGasto = gasto["monto"]

                fechaDateTime = datetime.strptime(fechaGasto, "%Y-%m-%d")
                año = fechaDateTime.year
                mesNumero = fechaDateTime.month

                primerDiaMes = datetime(año, mesNumero, 1)
                diasDesdePrimerDia = (fechaDateTime - primerDiaMes).days

                semanaDelMes = (diasDesdePrimerDia // 7) + 1

                claveSemana = (año, mesNumero, semanaDelMes)

                if claveSemana in tablaSemanal:
                    tablaSemanal[claveSemana] += montoGasto
                else:
                    tablaSemanal[claveSemana] = montoGasto

            totalCategoria = {}
            for gasto in usuario["gastos"]:
                categoriaGasto = gasto["categoria"]
                montoCategoria = gasto["monto"]
                if categoriaGasto in totalCategoria:
                    totalCategoria[categoriaGasto] += montoCategoria
                else:
                    totalCategoria[categoriaGasto] = montoCategoria

    clavesOrdenadas = sorted(tablaSemanal.keys())

    tablaFormateada = []
    for (año, mesNumero, semanaDelMes) in clavesOrdenadas:
        nombreMes = datetime(año, mesNumero, 1).strftime("%B")
        textoSemana = f"{año} {nombreMes} - Semana {semanaDelMes}"
        montoTotalSemana = tablaSemanal[(año, mesNumero, semanaDelMes)]
        tablaFormateada.append([textoSemana, montoTotalSemana])

    print(tabulate(tablaFormateada, headers=["Semana", "Total Gastado"], tablefmt="grid"))

    tablaCategoria = [[categoria, monto] for categoria, monto in totalCategoria.items()]
    print("\nGastos acumulados por categoría:")
    print(tabulate(tablaCategoria, headers=["Categoría", "Total"], tablefmt="grid"))

def calcularTotalMensual(usuarioActivo):
    from tabulate import tabulate
    from datetime import datetime
    datos = abrirJSON()
    tablaMensual = {}

    for usuario in datos[0]["listaUsuarios"]:
        if usuario["nombre"] == usuarioActivo:
            for gasto in usuario["gastos"]:
                fecha = gasto["fecha"]
                monto = gasto["monto"]
                fechaObjeto = datetime.strptime(fecha, "%Y-%m-%d")
                claveMes = fechaObjeto.strftime("%Y-%m")
                if claveMes in tablaMensual:
                    tablaMensual[claveMes] += monto
                else:
                    tablaMensual[claveMes] = monto

    tabla = [[mes, monto] for mes, monto in tablaMensual.items()]
    print(tabulate(tabla, headers=["Mes", "Total Gastado"], tablefmt="grid"))

    totalCategoria = {}
    for gasto in usuario["gastos"]:
        categoria = gasto["categoria"]
        monto = gasto["monto"]
        if categoria in totalCategoria:
            totalCategoria[categoria] += monto
        else:
            totalCategoria[categoria] = monto

    tablaCategoria = [[categoria, monto] for categoria, monto in totalCategoria.items()]
    print("\nGastos acumulados por categoría:")
    print(tabulate(tablaCategoria, headers=["Categoría", "Total"], tablefmt="grid"))