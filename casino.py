import multiprocessing
import time
import random


class Casino:
    def jugar_numero(cuenta, cantidad, numero):
        cuenta.value -= cantidad
        print('Se han apostado', cantidad,
              '€ al número', numero)
        time.sleep(random.random())

    def jugar_par_impar(cuenta, cantidad, par_impar):
        cuenta.value -= cantidad
        print('Se han apostado', cantidad,
              '€ a', par_impar)
        time.sleep(random.random())

    def jugar_martingala(cuenta, cantidad, numero):
        cuenta.value -= cantidad
        print('Se han apostado', cantidad,
              '€ a', numero)
        time.sleep(random.random())