import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))

from slinkedlist import slinkedlist


def fusionar_segmentos(lista):
    cero = lista.head
    nueva_cabeza = None
    nueva_cola = None
    nuevo_tamano = 0

    while cero is not None and cero.next is not None:

        primer_nodo = cero.next

        if primer_nodo.value == 0:
            break

        suma = 0
        actual = primer_nodo

        while actual is not None and actual.value != 0:
            suma += actual.value
            actual = actual.next

        primer_nodo.value = suma

        if nueva_cabeza is None:
            nueva_cabeza = primer_nodo
        else:
            nueva_cola.next = primer_nodo

        nueva_cola = primer_nodo
        nuevo_tamano += 1

        if actual is None:
            break

        cero.next = actual.next
        primer_nodo.next = actual.next

        cero = actual

    if nueva_cola is not None:
        nueva_cola.next = None

    lista.head = nueva_cabeza
    lista.tail = nueva_cola
    lista.size = nuevo_tamano

    return lista.head


def mostrar_lista(cabeza):
    actual = cabeza

    while actual is not None:
        print(actual.value, end="")

        if actual.next is not None:
            print(" --> ", end="")

        actual = actual.next

    print()


print("ESCENARIO 1")

lista = slinkedlist()

lista.append(0)
lista.append(5)
lista.append(2)
lista.append(0)
lista.append(8)
lista.append(1)
lista.append(3)
lista.append(0)
lista.append(6)
lista.append(0)

print("Lista original:")
print(lista)

cabeza = fusionar_segmentos(lista)

print("Lista resultante:")
mostrar_lista(cabeza)


print()
print("ESCENARIO 2")

lista = slinkedlist()

lista.append(0)
lista.append(10)
lista.append(0)
lista.append(2)
lista.append(3)
lista.append(4)
lista.append(0)
lista.append(7)
lista.append(1)
lista.append(0)

print("Lista original:")
print(lista)

cabeza = fusionar_segmentos(lista)

print("Lista resultante:")
mostrar_lista(cabeza)