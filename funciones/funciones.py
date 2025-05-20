import json

def abrirJSON():
    dicFinal=[]
    with open("./data/data.json",'r') as openFile:
        dicFinal=json.load(openFile)
    return dicFinal

def guardarJSON(dic):
    with open("./data/data.json",'w') as outFile:
        json.dump(dic,outFile)


def crearCuenta():
    datos = abrirJSON()

    print("===== CREAR CUENTA =====")
    nombreUsuario = input("Crea tu nombre de usuario: ")
    contrasena = input("Crea tu contraseña: ")
    nuevoUsuario = {"nombre":nombreUsuario,
                    "contrasena": contrasena,
                    "gastos":[]
                    
                    
                    
                    
                    
                    }
    datos[0]["listaUsuarios"].append(nuevoUsuario)
    guardarJSON(datos)
    print("Usuario creado con exito \n")





def iniciarSesion():
    datos = abrirJSON()
   
    
    print("===== INICIO DE SESIÓN =====")
    nombreUsuario = input("Nombre de usuario: ")
    contrasena = input("Contraseña: ")

    for usuario in datos[0]["listaUsuarios"]:
      if usuario["nombre"] == nombreUsuario and usuario["contrasena"] == contrasena:
            print(f"¡Bienvenido, {nombreUsuario}!\n")
            return usuario["nombre"]

    print("Usuario o contraseña incorrectos.\n")
    

def registarNuevoGasto(guardar, usuarioActivo, montoDelGasto, categoria, descripcion, fechaRegistro):
    if (categoria == 1):
        categoria = "Comida"
    elif(categoria == 2):
        categoria = "Transporte"
    elif (categoria == 3):
        categoria = "Entretenimiento"
    elif (categoria == 4):
        categoria = "Otros"
    if guardar == "s":
        datos = abrirJSON()
        for usuario in datos[0]["listaUsuarios"]:
            if usuario["nombre"] == usuarioActivo:
                nuevoGasto = {
                    "monto": montoDelGasto,
                    "categoria": categoria,
                    "descripcion": descripcion,
                    "fecha": fechaRegistro
                }
                usuario["gastos"].append(nuevoGasto)
                guardarJSON(datos)
                print(" Gasto guardado correctamente.")
                
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
