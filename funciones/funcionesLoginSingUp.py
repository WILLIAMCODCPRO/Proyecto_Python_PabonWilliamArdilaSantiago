from funciones.funcionesJson import *

def crearCuenta():
    datos = abrirJSON()

    print("===== CREAR CUENTA =====")
    nombreUsuario = input("Crea tu nombre de usuario: ")
    contrasena = input("Crea tu contraseña: ")
    nuevoUsuario = {"nombre":nombreUsuario,
                    "contrasena": contrasena,
                    "reportes" : [],
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

