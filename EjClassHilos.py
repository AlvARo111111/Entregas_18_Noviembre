import threading

#Clase que hereda de thread
class ProcesadorArchivo(threading.Thread):
    def __init__(self, nombre):
        super().__init__()
        self.nombre = nombre

    def run(self):
        try:
            with open(self.nombre, 'r') as archivo:
                num_linea = 1
                for linea in archivo:
                    print(f"Procesando {self.nombre} - Línea {num_linea}: {linea.strip()}")
                    num_linea += 1
        except FileNotFoundError:
            print(f"Error: No se encontró el archivo {self.nombre}")

# archivos
archivos = ["Recursos/archivo1.txt", "Recursos/archivo2.txt", "Recursos/archivo3.txt"]

# Crear e iniciar hilos
hilos = []
for nombre in archivos:
    hilo = ProcesadorArchivo(nombre)
    hilos.append(hilo)
    hilo.start()

# Esperar a que todos los hilos terminen
for hilo in hilos:
    hilo.join()

print("\nTodos los archivos han sido procesados.")
