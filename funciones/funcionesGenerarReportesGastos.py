from funciones.funcionesJson import *

def reporteDiario(usuarioActivo):
    datos = abrirJSON()
    totalPorFecha = {}
    totalPorCategoria = {}

    for usuario in datos[0]["listaUsuarios"]:
        if usuario["nombre"] == usuarioActivo:
            for gasto in usuario["gastos"]:
                fecha = gasto["fecha"]
                monto = gasto["monto"]
                categoria = gasto["categoria"]

               
                if fecha in totalPorFecha:
                    totalPorFecha[fecha] += monto
                else:
                    totalPorFecha[fecha] = monto

                if categoria in totalPorCategoria:
                    totalPorCategoria[categoria] += monto
                else:
                    totalPorCategoria[categoria] = monto

    print("REPORTE DIARIO DE GASTOS")
    print("========================\n")

    print("Totales por Fecha:")
    for fecha, monto in totalPorFecha.items():
        print(f"- El día {fecha} se gastó un total de ${monto}")

    print("\nTotales por Categoría:")
    for categoria, monto in totalPorCategoria.items():
        print(f"- En la categoría '{categoria}' se gastó un total de ${monto}")
    
def reporteSemanal(usuarioActivo):
    from datetime import datetime
    datos = abrirJSON()
    totalPorSemana = {}
    totalPorCategoria = {}

    for usuario in datos[0]["listaUsuarios"]:
        if usuario["nombre"] == usuarioActivo:
            for gasto in usuario["gastos"]:
                fechaTexto = gasto["fecha"]
                fecha = datetime.strptime(fechaTexto, "%Y-%m-%d")
                
               
                primerDiaMes = fecha.replace(day=1)
                diaSemanaPrimero = primerDiaMes.weekday()
                semanaDelMes = ((fecha.day + diaSemanaPrimero - 1) // 7) + 1
                
                claveSemana = f"{fecha.strftime('%B %Y')} - Semana {semanaDelMes}"

                monto = gasto["monto"]
                categoria = gasto["categoria"]

                if claveSemana in totalPorSemana:
                    totalPorSemana[claveSemana] += monto
                else:
                    totalPorSemana[claveSemana] = monto

                if categoria in totalPorCategoria:
                    totalPorCategoria[categoria] += monto
                else:
                    totalPorCategoria[categoria] = monto

    print("REPORTE SEMANAL DE GASTOS")
    print("==========================\n")

    print("Totales por Semana del Mes:")
    for semana, monto in sorted(totalPorSemana.items()):
        print(f"- En {semana} se gastó un total de ${monto}")

    print("\nTotales por Categoría:")
    for categoria, monto in totalPorCategoria.items():
        print(f"- En la categoría '{categoria}' se gastó un total de ${monto}")

def reporteMensual(usuarioActivo):
    from datetime import datetime
    datos = abrirJSON()
    totalPorMes = {}
    totalPorCategoria = {}

    for usuario in datos[0]["listaUsuarios"]:
        if usuario["nombre"] == usuarioActivo:
            for gasto in usuario["gastos"]:
                fechaTexto = gasto["fecha"]
                fecha = datetime.strptime(fechaTexto, "%Y-%m-%d")
                
                claveMes = fecha.strftime("%B %Y") 
                monto = gasto["monto"]
                categoria = gasto["categoria"]

                if claveMes in totalPorMes:
                    totalPorMes[claveMes] += monto
                else:
                    totalPorMes[claveMes] = monto

                if categoria in totalPorCategoria:
                    totalPorCategoria[categoria] += monto
                else:
                    totalPorCategoria[categoria] = monto

    print("REPORTE MENSUAL DE GASTOS")
    print("==========================\n")

    print("Totales por Mes:")
    for mes, monto in sorted(totalPorMes.items()):
        print(f"- En {mes} se gastó un total de ${monto}")

    print("\nTotales por Categoría:")
    for categoria, monto in totalPorCategoria.items():
        print(f"- En la categoría '{categoria}' se gastó un total de ${monto}")