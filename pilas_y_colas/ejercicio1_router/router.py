from queue import Queue
from paquete import Paquete


class Router:

    def __init__(self, memoryLimit):
        self.memoryLimit = memoryLimit
        self.paquetes = Queue()