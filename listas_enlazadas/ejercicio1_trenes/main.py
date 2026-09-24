import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))

from tren import Tren


tren = Tren(1)

while True:

    print()
    print("GESTOR DE TRENES Y VAGONES")
    print()
    print("1. Mostrar tren")
    print("2. Ir al siguiente vagón")
    print("3. Ir al vagón anterior")
    print("4. Acoplar vagón")
    print("5. Desacoplar vagón actual")
    print("6. Mover vagón actual al inicio")
    print("7. Mover vagón actual al final")
    print("8. Salir")
    print()

    opcion = input("Seleccione una opción: ")

    if opcion == "1":

        tren.mostrar_tren()

    elif opcion == "2":

        tren.siguiente()
        tren.mostrar_tren()

    elif opcion == "3":

        tren.anterior()
        tren.mostrar_tren()

    elif opcion == "4":

        numero = input("Número del nuevo vagón: ")
        tren.acoplar(numero)
        tren.mostrar_tren()

    elif opcion == "5":

        tren.desacoplar_actual()
        tren.mostrar_tren()

    elif opcion == "6":

        tren.mover_actual_inicio()
        tren.mostrar_tren()

    elif opcion == "7":

        tren.mover_actual_final()
        tren.mostrar_tren()

    elif opcion == "8":

        print("Programa finalizado.")
        break

    else:

        print("Opción no válida.")