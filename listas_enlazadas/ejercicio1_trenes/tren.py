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
        
    def acoplar(self, numero):
        nuevo_vagon = Vagon(numero)
        nuevo_nodo = Node(nuevo_vagon)

        if self.actual is None:
            self.vagones.head = nuevo_nodo
            self.vagones.tail = nuevo_nodo
            self.vagones.size = 1
            self.actual = nuevo_nodo
            return

        nuevo_nodo.next = self.actual.next
        self.actual.next = nuevo_nodo

        if self.vagones.tail == self.actual:
            self.vagones.tail = nuevo_nodo

        self.vagones.size += 1
        
    def desacoplar_actual(self):
        if self.actual is None:
            print("El tren está vacío.")
            return

        if self.vagones.size == 1:
            self.vagones.head = None
            self.vagones.tail = None
            self.vagones.size = 0
            self.actual = None
            return

        nodo_eliminado = self.actual

        if self.actual == self.vagones.head:
            self.vagones.head = self.actual.next
            self.actual = self.vagones.head
            nodo_eliminado.next = None
            self.vagones.size -= 1
            return

        anterior = self.vagones.head

        while anterior.next != self.actual:
            anterior = anterior.next

        siguiente = self.actual.next
        anterior.next = siguiente

        if siguiente is not None:
            self.actual = siguiente
        else:
            self.actual = anterior
            self.vagones.tail = anterior

        nodo_eliminado.next = None
        self.vagones.size -= 1