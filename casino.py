import multiprocessing
import time
import random
class Casino:


    def jugar_numero(cuenta, cantidad, numero):
        cuenta.value -= cantidad
        print('Se han apostado', cantidad,
            '€ al número', numero)
        time.sleep(random.random())
