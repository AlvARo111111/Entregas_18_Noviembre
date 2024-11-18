import threading

class SesionUsuario:
    def __init__(self):
        self.nombreUsuario = None

#Almacana el usuario en una variable
    def iniciarSesion(self, nombreUsuario):
        self.nombreUsuario = nombreUsuario

    def mostrarSesion(self):
        print(f"Sesion iniciada para el usuario: {self.nombreUsuario}")

# Objeto threading.local() para almacenar info
datosSesion = threading.local()

def sesion(nombreUsuario):

    datosSesion.sesion = SesionUsuario()

    # Iniciar sesión con el nombre de usuario
    datosSesion.sesion.iniciarSesion(nombreUsuario)

    # Mostrar sesión del hilo actual
    datosSesion.sesion.mostrarSesion()

usuarios = ["Alvaro", "Rodrigo", "Victor", "Saul", "Daniel"]

# Crear hilos
hilos = []
for nombre in usuarios:
    hilo = threading.Thread(target=sesion, args=(nombre,))
    hilos.append(hilo)
    hilo.start()

# Esperar a que todos los hilos terminen
for hilo in hilos:
    hilo.join()

