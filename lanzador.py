from banco import iniciar_ej1
from casino import iniciar_ej2
from introducir.numero import solicitar_introducir_numero
from colorama import init, Fore, Back, Style

def lanzador():
    eleccion = solicitar_introducir_numero(Fore.BLUE + "Seleccione el ejercicio a ejecutar:\n1 Banca\n2 Casino\n3 Salir\n" + Style.RESET_ALL)
    if eleccion == 1:
        iniciar_ej1()
        lanzador()
    elif eleccion == 2:
        iniciar_ej2()
        lanzador()
    elif eleccion == 3:
        exit()
