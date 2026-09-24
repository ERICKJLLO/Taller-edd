from stack import Stack


class Editor:

    def __init__(self):
        self.texto = ""
        self.historial = Stack()

    def append(self, texto):
        self.historial.push(self.texto)
        self.texto += texto

    def delete(self, cantidad):
        self.historial.push(self.texto)
        self.texto = self.texto[:-cantidad]

    def imprimir(self, posicion):
        print(self.texto[posicion - 1])

    def undo(self):
        if not self.historial.is_empty():
            self.texto = self.historial.pop()
        else:
            print("No hay operaciones para deshacer.")

    def mostrar(self):
        print('Texto actual: "' + self.texto + '"')