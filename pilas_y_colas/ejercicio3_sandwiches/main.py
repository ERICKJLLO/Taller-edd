import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))

from cafeteria import Cafeteria


print("ESCENARIO 1")
print()

estudiantes = [1, 1, 0, 0]
sandwiches = [0, 1, 0, 1]

cafeteria = Cafeteria()

no_comieron, sobraron = cafeteria.procesar(estudiantes, sandwiches)

print("Estudiantes:", estudiantes)
print("Sandwiches:", sandwiches)
print("Estudiantes que no pudieron comer:", no_comieron)
print("Sandwiches que quedaron:", sobraron)


print()
print("ESCENARIO 2")
print()

estudiantes = [0, 0, 1, 1]
sandwiches = [1, 1, 0, 0]

cafeteria = Cafeteria()

no_comieron, sobraron = cafeteria.procesar(estudiantes, sandwiches)

print()
print("ESCENARIO 3")
print()

estudiantes = [0, 0, 0, 1]
sandwiches = [1, 1, 1, 1]

cafeteria = Cafeteria()

no_comieron, sobraron = cafeteria.procesar(estudiantes, sandwiches)

print("Estudiantes:", estudiantes)
print("Sandwiches:", sandwiches)
print("Estudiantes que no pudieron comer:", no_comieron)
print("Sandwiches que quedaron:", sobraron)