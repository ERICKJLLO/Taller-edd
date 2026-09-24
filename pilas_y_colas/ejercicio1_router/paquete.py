class Paquete:

    def __init__(self, source, destination, timestamp):
        self.source = source
        self.destination = destination
        self.timestamp = timestamp

    def __str__(self):
        return "[" + str(self.source) + ", " + str(self.destination) + ", " + str(self.timestamp) + "]"