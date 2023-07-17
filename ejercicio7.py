import time

class Vehiculo:
    def __init__(self, id_vehiculo, velocidad):
        self.id_vehiculo = id_vehiculo
        self.velocidad = velocidad

    def avanzar(self):
        print(f"El vehículo {self.id_vehiculo} está avanzando a una velocidad de {self.velocidad} km/h.")

    def detenerse(self):
        print(f"El vehículo {self.id_vehiculo} se ha detenido.")

class Semaforo:
    def __init__(self, id_semaforo, estado):
        self.id_semaforo = id_semaforo
        self.estado = estado

    def cambiar_estado(self):
        if self.estado == "verde":
            self.estado = "rojo"
        else:
            self.estado = "verde"

        print(f"El semáforo {self.id_semaforo} ha cambiado a {self.estado}.")

class Cruce:
    def __init__(self, id_cruce, semaforos):
        self.id_cruce = id_cruce
        self.semaforos = semaforos

    def simular_trafico(self):
        print(f"Iniciando simulación en el cruce {self.id_cruce}...\n")

        for semaforo in self.semaforos:
            semaforo.cambiar_estado()

        vehiculo1 = Vehiculo(1, 50)
        vehiculo2 = Vehiculo(2, 40)

        vehiculo1.avanzar()
        vehiculo2.avanzar()

        time.sleep(2)

        vehiculo1.detenerse()
        vehiculo2.detenerse()

        print("\nFin de la simulación.")

# Ejemplo de uso
semaforo1 = Semaforo(1, "verde")
semaforo2 = Semaforo(2, "rojo")

cruce1 = Cruce(1, [semaforo1, semaforo2])
cruce1.simular_trafico()
