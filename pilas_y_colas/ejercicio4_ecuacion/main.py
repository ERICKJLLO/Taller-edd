import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))

from postfija import evaluar_postfija


print("ESCENARIO 1")
print()

expresion = "43+"

print("Expresión:", expresion)
print("Resultado:", evaluar_postfija(expresion))


print()
print("ESCENARIO 2")
print()

expresion = "35x83+-"

print("Expresión:", expresion)
print("Resultado:", evaluar_postfija(expresion))