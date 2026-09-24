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


