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