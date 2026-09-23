from slinkedlist import slinkedlist
from node import Node
from vagon import Vagon


class Tren:

    def __init__(self, numero_inicial):
        self.vagones = slinkedlist()
        self.vagones.append(Vagon(numero_inicial))
        self.actual = self.vagones.head

    def mostrar_tren(self):
        if self.vagones.size == 0:
            print("El tren está vacío.")
            return

        nodo = self.vagones.head

        while nodo is not None:
            if nodo == self.actual:
                print("[" + str(nodo.value) + "]", end="")
            else:
                print(str(nodo.value), end="")

            if nodo.next is not None:
                print(" --> ", end="")

            nodo = nodo.next

        print()

    def siguiente(self):
        if self.actual is None:
            print("El tren está vacío.")
            return

        if self.actual.next is not None:
            self.actual = self.actual.next
        else:
            print("Ya está en el último vagón.")
    
    def anterior(self):
        if self.actual is None:
            print("El tren está vacío.")
            return

        if self.actual == self.vagones.head:
            print("Ya está en el primer vagón.")
            return

        nodo = self.vagones.head

        while nodo.next != self.actual:
            nodo = nodo.next

        self.actual = nodo