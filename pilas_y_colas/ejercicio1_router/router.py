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