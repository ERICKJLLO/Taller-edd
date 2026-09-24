from queue import Queue
from stack import Stack


class Estudiante:

    def __init__(self, preferencia):
        self.preferencia = preferencia
        self.reintentos = 2


class Cafeteria:

    def __init__(self):
        self.estudiantes = Queue()
        self.sandwiches = Stack()

    def procesar(self, estudiantes, sandwiches):

        for estudiante in estudiantes:
            self.estudiantes.enqueue(Estudiante(estudiante))

        for sandwich in sandwiches:
            self.sandwiches.push(sandwich)

        no_comieron = 0

        while not self.estudiantes.is_empty() and not self.sandwiches.is_empty():

            estudiante = self.estudiantes.dequeue()

            if estudiante.preferencia == self.sandwiches.top():
                self.sandwiches.pop()
            else:
                estudiante.reintentos -= 1

                if estudiante.reintentos > 0:
                    self.estudiantes.enqueue(estudiante)
                else:
                    no_comieron += 1

        return no_comieron, self.sandwiches.len()