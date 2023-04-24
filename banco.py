import multiprocessing
import time
import random

class Banco:

    def ingreso(cuenta, cantidad):
        cuenta.value += cantidad
        print('Se han ingresado', cantidad, '€ en la cuenta')
        time.sleep(random.random())

    def retirar(cuenta, cantidad):
        cuenta.value -= cantidad
        print('Se ha retirado', cantidad, '€ de la cuenta')
        time.sleep(random.random())
