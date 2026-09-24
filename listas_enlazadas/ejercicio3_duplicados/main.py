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