import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))

from slinkedlist import slinkedlist


def fusionar_segmentos(lista):
    actual = lista.head

    while actual is not None and actual.next is not None:

        if actual.next.value == 0:
            actual = actual.next
            continue

        suma = 0
        nodo = actual.next

        while nodo is not None and nodo.value != 0:
            suma += nodo.value
            nodo = nodo.next

        if nodo is None:
            break

        actual.next.value = suma
        actual.next.next = nodo.next

        if actual.next.next is None:
            lista.tail = actual.next

        lista.size -= 1

        actual = actual.next

    lista.head = lista.head.next
    lista.size -= 1

    return lista.head


def mostrar_desde_cabeza(cabeza):
    actual = cabeza

    while actual is not None:
        print(actual.value, end="")

        if actual.next is not None:
            print(" --> ", end="")

        actual = actual.next

    print()


lista = slinkedlist()

lista.append(0)
lista.append(3)
lista.append(1)
lista.append(0)
lista.append(4)
lista.append(5)
lista.append(2)
lista.append(0)
lista.append(7)
lista.append(8)
lista.append(0)

print("Lista original:")
print(lista)

cabeza = fusionar_segmentos(lista)

print("Lista resultante:")
mostrar_desde_cabeza(cabeza)