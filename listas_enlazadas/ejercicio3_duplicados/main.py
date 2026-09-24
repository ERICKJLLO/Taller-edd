import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))

from dlinkedlist import dlinkedlist


def eliminar_duplicados(lista):
    actual = lista.head

    while actual is not None:
        siguiente = actual.next

        while siguiente is not None:
            siguiente_nodo = siguiente.next

            if siguiente.value == actual.value:
                anterior = siguiente.prev
                posterior = siguiente.next

                if anterior is not None:
                    anterior.next = posterior

                if posterior is not None:
                    posterior.prev = anterior

                if siguiente == lista.tail:
                    lista.tail = anterior

                lista.size -= 1

            siguiente = siguiente_nodo

        actual = actual.next

    if lista.head is not None:
        lista.head.prev = None

    if lista.tail is not None:
        lista.tail.next = None


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
lista.append(10)
lista.append(30)
lista.append(20)
lista.append(10)

print("Lista original:")
mostrar_lista(lista)

eliminar_duplicados(lista)

print("Lista resultante:")
mostrar_lista(lista)


print()
print("ESCENARIO 2")

lista = dlinkedlist()

lista.append(5)
lista.append(8)
lista.append(5)
lista.append(12)
lista.append(8)
lista.append(15)
lista.append(12)

print("Lista original:")
mostrar_lista(lista)

eliminar_duplicados(lista)

print("Lista resultante:")
mostrar_lista(lista)