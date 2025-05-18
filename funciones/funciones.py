import json

def abrirJSON():
    dicFinal=[]
    with open("./data/data.json",'r') as openFile:
        dicFinal=json.load(openFile)
    return dicFinal

def guardarJSON(dic):
    with open("./data/data.json",'w') as outFile:
        json.dump(dic,outFile)
        
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