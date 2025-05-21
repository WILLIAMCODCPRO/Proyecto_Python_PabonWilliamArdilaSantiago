from funciones.funcionesJson import *

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