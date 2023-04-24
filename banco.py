import multiprocessing
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
        cuenta = multiprocessing.Value('i', 100)
        procesos = []
        for i in range(40):
            p = multiprocessing.Process(
                target=Banco.ingresar, args=(cuenta, 100))
            procesos.append(p)
            p.start()
        for i in range(20):
            p = multiprocessing.Process(
                target=Banco.ingresar, args=(cuenta, 50))
            procesos.append(p)
            p.start()
        for i in range(60):
            p = multiprocessing.Process(
                target=Banco.ingresar, args=(cuenta, 20))
            procesos.append(p)
            p.start()
        for i in range(40):
            p = multiprocessing.Process(
                target=Banco.retirar, args=(cuenta, 100))
            procesos.append(p)
            p.start()
        for i in range(20):
            p = multiprocessing.Process(
                target=Banco.retirar, args=(cuenta, 50))
            procesos.append(p)
            p.start()
        for i in range(60):
            p = multiprocessing.Process(
                target=Banco.retirar, args=(cuenta, 20))
            procesos.append(p)
            p.start()
        for p in procesos:
            p.join()
        print(
            Fore.BLUE + f'El saldo de la cuenta final es de {cuenta.value} €' + Style.RESET_ALL)


if __name__ == '__main__':
    Banco.main()
