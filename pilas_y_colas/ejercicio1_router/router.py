from queue import Queue
from paquete import Paquete


class Router:

    def __init__(self, memoryLimit):
        self.memoryLimit = memoryLimit
        self.paquetes = Queue()
        
    def addPacket(self, source, destination, timestamp):
        cantidad = self.paquetes.len()

        for i in range(cantidad):
            paquete = self.paquetes.dequeue()

            if paquete.source == source and paquete.destination == destination and paquete.timestamp == timestamp:
                self.paquetes.enqueue(paquete)

                for j in range(i + 1, cantidad):
                    paquete = self.paquetes.dequeue()
                    self.paquetes.enqueue(paquete)

                return False

            self.paquetes.enqueue(paquete)

        if self.paquetes.len() == self.memoryLimit:
            self.paquetes.dequeue()

        nuevo_paquete = Paquete(source, destination, timestamp)
        self.paquetes.enqueue(nuevo_paquete)

        return True
    
    def forwardPacket(self):
        if self.paquetes.is_empty():
            return []

        paquete = self.paquetes.dequeue()

        return [paquete.source, paquete.destination, paquete.timestamp]
    
    def getCount(self, destination, startTime, endTime):
        cantidad = self.paquetes.len()
        contador = 0

        for i in range(cantidad):
            paquete = self.paquetes.dequeue()

            if paquete.destination == destination and startTime <= paquete.timestamp <= endTime:
                contador += 1

            self.paquetes.enqueue(paquete)

        return contador
    
    def mostrar(self):
        if self.paquetes.is_empty():
            print("Router vacío.")
            return

        cantidad = self.paquetes.len()

        for i in range(cantidad):
            paquete = self.paquetes.dequeue()
            print(paquete, end="")

            if i < cantidad - 1:
                print(" -- ", end="")

            self.paquetes.enqueue(paquete)

        print()