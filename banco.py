import multiprocessing
import time
import random

class Banco:

    def ingresar(cuenta, cantidad):
        cuenta.value += cantidad
        print('Se han ingresado', cantidad, '€ en la cuenta')
        time.sleep(random.random())

    def retirar(cuenta, cantidad):
        cuenta.value -= cantidad
        print('Se ha retirado', cantidad, '€ de la cuenta')
        time.sleep(random.random())

    def main():
        cuenta = multiprocessing.Value('i', 100)
        procesos = []
        for i in range(40):
            p = multiprocessing.Process(target=Banco.ingresar, args=(cuenta, 100))
            procesos.append(p)
            p.start()
        for i in range(20):
            p = multiprocessing.Process(target=Banco.ingresar, args=(cuenta, 50))
            procesos.append(p)
            p.start()
        for i in range(60):
            p = multiprocessing.Process(target=Banco.ingresar, args=(cuenta, 20))
            procesos.append(p)
            p.start()
        for i in range(40):
            p = multiprocessing.Process(target=Banco.retirar, args=(cuenta, 100))
            procesos.append(p)
            p.start()
        for i in range(20):
            p = multiprocessing.Process(target=Banco.retirar, args=(cuenta, 50))
            procesos.append(p)
            p.start()
        for i in range(60):
            p = multiprocessing.Process(target=Banco.retirar, args=(cuenta, 20))
            procesos.append(p)
            p.start()
        for p in procesos:
            p.join()
        print(f'El saldo de la cuenta final es de {cuenta.value} €')

if __name__ == '__main__':
    Banco.main()

