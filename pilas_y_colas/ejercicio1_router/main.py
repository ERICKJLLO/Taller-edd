import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))

from router import Router


print("ESCENARIO 1")
print()

router = Router(3)

print("Agregando paquete 1:")
print(router.addPacket(1, 10, 100))
router.mostrar()

print("Agregando paquete 2:")
print(router.addPacket(2, 20, 200))
router.mostrar()

print("Agregando paquete 3:")
print(router.addPacket(3, 10, 300))
router.mostrar()

print("Intentando agregar paquete duplicado:")
print(router.addPacket(2, 20, 200))
router.mostrar()

print("Agregando un cuarto paquete:")
print(router.addPacket(4, 30, 400))
router.mostrar()

print("Cantidad destino 10 entre 50 y 350:")
print(router.getCount(10, 50, 350))

print("Procesando paquete más antiguo:")
print(router.forwardPacket())
router.mostrar()


print()