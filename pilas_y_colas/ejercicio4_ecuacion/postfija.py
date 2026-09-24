from stack import Stack


def evaluar_postfija(expresion):
    pila = Stack()

    for caracter in expresion:
        if caracter.isdigit():
            pila.push(int(caracter))
        else:
            segundo = pila.pop()
            primero = pila.pop()

            if caracter == "+":
                resultado = primero + segundo
            elif caracter == "-":
                resultado = primero - segundo
            elif caracter == "x":
                resultado = primero * segundo
            elif caracter == "/":
                resultado = primero / segundo

            pila.push(resultado)

    return pila.pop()