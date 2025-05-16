from tabulate import tabulate

table = [["1. Registrar nuevo gasto"],["2. Listar gastos"],["3. Calcular total de gastos"],["4. Generar reporte de gastos"],["5. Salir"]]
print(tabulate(table, headers= [" Simulador de Gasto Diario"]))