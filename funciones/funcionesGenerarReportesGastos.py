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

            reporte = "REPORTE DIARIO DE GASTOS\n========================\n\n"
            reporte += "Totales por Fecha:\n"
            for fecha, monto in totalPorFecha.items():
                reporte += f"- El día {fecha} se gastó un total de ${monto}\n"

            reporte += "\nTotales por Categoría:\n"
            for categoria, monto in totalPorCategoria.items():
                reporte += f"- En la categoría '{categoria}' se gastó un total de ${monto}\n"

            eleccion = input("¿Deseas mostrar el reporte en pantalla (1) o guardarlo en JSON (2)? ")
            if eleccion == "1":
                print(reporte)
            elif eleccion == "2":
                if "reportes" not in usuario:
                    usuario["reportes"] = []
                usuario["reportes"].append({
                    "tipo": "Diario",
                    "contenido": reporte
                })
                guardarJSON(datos)
                print("Reporte diario guardado correctamente.")

            

    
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

            reporte = "REPORTE SEMANAL DE GASTOS\n==========================\n\n"
            reporte += "Totales por Semana del Mes:\n"
            for semana, monto in totalPorSemana.items():
                reporte += f"- En {semana} se gastó un total de ${monto}\n"

            reporte += "\nTotales por Categoría:\n"
            for categoria, monto in totalPorCategoria.items():
                reporte += f"- En la categoría '{categoria}' se gastó un total de ${monto}\n"

            eleccion = input("¿Deseas mostrar el reporte en pantalla (1) o guardarlo en JSON (2)? ")
            if eleccion == "1":
                print(reporte)
            elif eleccion == "2":
                if "reportes" not in usuario:
                    usuario["reportes"] = []
                usuario["reportes"].append({
                    "tipo": "Semanal",
                    "contenido": reporte
                })
                guardarJSON(datos)
                print("Reporte semanal guardado correctamente.")

            


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

            reporte = "REPORTE MENSUAL DE GASTOS\n==========================\n\n"
            reporte += "Totales por Mes:\n"
            for mes, monto in totalPorMes.items():
                reporte += f"- En {mes} se gastó un total de ${monto}\n"

            reporte += "\nTotales por Categoría:\n"
            for categoria, monto in totalPorCategoria.items():
                reporte += f"- En la categoría '{categoria}' se gastó un total de ${monto}\n"

            eleccion = input("¿Deseas mostrar el reporte en pantalla (1) o guardarlo en JSON (2)? ")
            if eleccion == "1":
                print(reporte)
            elif eleccion == "2":
                if "reportes" not in usuario:
                    usuario["reportes"] = []
                usuario["reportes"].append({
                    "tipo": "Mensual",
                    "contenido": reporte
                })
                guardarJSON(datos)
                print("Reporte mensual guardado correctamente.")

            