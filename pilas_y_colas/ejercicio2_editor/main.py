import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))

from editor import Editor


print("ESCENARIO 1")
print()

editor = Editor()

print('append "abc"')
editor.append("abc")
editor.mostrar()

print('append "xy"')
editor.append("xy")
editor.mostrar()

print("print 4")
editor.imprimir(4)

print("delete 3")
editor.delete(3)
editor.mostrar()

print("print 2")
editor.imprimir(2)

print("undo")
editor.undo()
editor.mostrar()

print("print 5")
editor.imprimir(5)

print("undo")
editor.undo()
editor.mostrar()
