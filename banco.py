import multiprocessing
from multiprocessing import pool
import time
import random
from colorama import Fore, Style

class Banco:

    def ingresar(cuenta, cantidad):
        cuenta.value += cantidad
        print(Fore.GREEN + 'Se han ingresado', cantidad,
              '€ en la cuenta' + Style.RESET_ALL)
        time.sleep(random.random())

    def retirar(cuenta, cantidad):
        cuenta.value -= cantidad
        print(Fore.RED + 'Se ha retirado', cantidad,
              '€ de la cuenta' + Style.RESET_ALL)
        time.sleep(random.random())

    def main():
        pool = multiprocessing.Pool(processes=4)
        cuenta = multiprocessing.Value('i', 100)
        for i in range(40):
            pool.apply_async(Banco.ingresar, (cuenta, 100))
            print(Fore.GREEN + 'Se han ingresado', 100,)

        for i in range(20):
            pool.apply_async(Banco.ingresar, (cuenta, 50))
            print(Fore.GREEN + 'Se han ingresado', 50,)

        for i in range(60):
            pool.apply_async(Banco.ingresar, (cuenta, 20))
            print(Fore.GREEN + 'Se han ingresado', 20,)

        for i in range(40):
            pool.apply_async(Banco.retirar, (cuenta, 100))
            print(Fore.RED + 'Se han retirado', 100,)

        for i in range(20):
            pool.apply_async(Banco.retirar, (cuenta, 50))
            print(Fore.RED + 'Se han retirado', 50,)

        for i in range(60):
            pool.apply_async(Banco.retirar, (cuenta, 20))
            print(Fore.RED + 'Se han retirado', 20,)

        pool.close()
        pool.join()
        print(Fore.BLUE +'El saldo final es', cuenta.value, '€' + Style.RESET_ALL)


def iniciar_ej1():
    Banco.main()
