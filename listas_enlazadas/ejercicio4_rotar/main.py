import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))

from dlinkedlist import dlinkedlist


def rotar_hasta_maximo(lista):
    if lista.head is None:
        return

    maximo = lista.head
    actual = lista.head.next

    while actual is not None:
        if actual.value > maximo.value:
            maximo = actual
        actual = actual.next

    if maximo == lista.head:
        return

    while lista.head != maximo:
        ultimo = lista.tail
        anterior = ultimo.prev

        anterior.next = None
        lista.tail = anterior

        ultimo.prev = None
        ultimo.next = lista.head
        lista.head.prev = ultimo
        lista.head = ultimo


def mostrar_lista(lista):
    actual = lista.head

    while actual is not None:
        print(actual.value, end="")

        if actual.next is not None:
            print(" <--> ", end="")

        actual = actual.next

    print()


print("ESCENARIO 1")

lista = dlinkedlist()

lista.append(10)
lista.append(20)
lista.append(30)
lista.append(40)
lista.append(50)

print("Lista original:")
mostrar_lista(lista)

rotar_hasta_maximo(lista)

print("Lista resultante:")
mostrar_lista(lista)


print()
print("ESCENARIO 2")

lista = dlinkedlist()

lista.append(15)
lista.append(8)
lista.append(25)
lista.append(12)
lista.append(40)
lista.append(6)

print("Lista original:")
mostrar_lista(lista)

rotar_hasta_maximo(lista)

print("Lista resultante:")
mostrar_lista(lista)