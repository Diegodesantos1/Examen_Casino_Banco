from banco import iniciar_ej1
from casino import iniciar_ej2

def lanzador():
    eleccion = int(input("Seleccione el ejercicio a ejecutar: "))
    if eleccion == 1:
        iniciar_ej1()
    elif eleccion == 2:
        iniciar_ej2()
