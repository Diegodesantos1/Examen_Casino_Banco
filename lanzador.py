from banco import iniciar_ej1
from casino import iniciar_ej2
from introducir.numero import introducir_numero

def lanzador():
    eleccion = introducir_numero("Seleccione el ejercicio a ejecutar: ")
    if eleccion == 1:
        iniciar_ej1()
    elif eleccion == 2:
        iniciar_ej2()
