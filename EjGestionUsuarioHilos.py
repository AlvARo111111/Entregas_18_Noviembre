import threading
import time
import random

def procesar_usuario(idUsuario, **kwargs):
    nombre = kwargs.get('nombre', 'Desconocido')
    edad = kwargs.get('edad', 'N/A')

    # Pausa aleatoria
    time.sleep(random.uniform(0.5, 2.0))

    print(f"Usuario ID: {idUsuario}, Nombre: {nombre}, Edad: {edad}")


# Lista usuarios
usuarios = [
    {'id': 1, 'nombre': 'Alvaro', 'edad': 22},
    {'id': 2, 'nombre': 'Rodrigo', 'edad': 20},
    {'id': 3, 'nombre': 'Victor', 'edad': 21},
    {'id': 4, 'nombre': 'Saul', 'edad': 22},
    {'id': 5, 'nombre': 'Daniel', 'edad': 20}
]

hilos = []

# Crear un hilo para cada usuario en la lista
for usuario in usuarios:

    hilo = threading.Thread(target=procesar_usuario, args=(usuario['id'],), kwargs={'nombre': usuario['nombre'], 'edad': usuario['edad']})
    hilos.append(hilo)
    hilo.start()

# Esperar a que todos los hilos terminen
for hilo in hilos:
    hilo.join()

print("\nTodos los usuarios han sido procesados.")
