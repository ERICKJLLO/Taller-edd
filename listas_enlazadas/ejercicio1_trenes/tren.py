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