<h1 align = "center">Examen Banco/Casino</h1>

En este [repositorio](https://github.com/Diegodesantos1/Examen_Casino_Banco) quedan resuelto examen.

<h2 align = "center">Ejercicio 1: Banco</h2>

El código empleado para resolverlo es el siguiente:

```python
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
```

<h2 align = "center">Ejercicio 2: Banco</h2>

El código empleado para resolverlo es el siguiente:

```python
import multiprocessing
import time
import random
from introducir.numero import solicitar_introducir_numero


class Casino:
    def jugar_numero(cuenta, cantidad, numero):
        cuenta.value -= cantidad
        print('Se han apostado', cantidad,
              '€ al número', numero)
        time.sleep(3)

    def jugar_par_impar(cuenta, cantidad, par_impar):
        cuenta.value -= cantidad
        print('Se han apostado a par/impar', cantidad,
              '€ a', par_impar)
        time.sleep(3)

    def jugar_martingala(cuenta, cantidad, numero):
        cuenta.value -= cantidad
        print('Se han apostado con martingala', cantidad,
              '€ a', numero)
        time.sleep(3)
    def comprobar_dinero(dinero_hilos):
        for k in range(len(dinero_hilos)):
            if dinero_hilos[k] <= 0:
                print('El jugador', k + 1, 'se ha quedado sin dinero')
                exit()
    def main():
        jugadas = solicitar_introducir_numero('Introduce el número de jugadas: ')
        pool = multiprocessing.Pool(processes=4)
        dinero_hilos =[1000, 1000, 1000, 1000]
        cuenta = multiprocessing.Value('i', 5000)
        numero = random.randint(1, 36)
        for i in range(jugadas):
            Casino.comprobar_dinero(dinero_hilos)
            for j in range(len(dinero_hilos)):
                Casino.comprobar_dinero(dinero_hilos)
                pool.apply_async(Casino.jugar_numero, (cuenta, 10, random.randint(1, 36)))
                print('Se han apostado', 10, '€ a', random.randint(1, 36))
                if numero == random.randint(1, 36):
                    dinero_hilos[j] += 360
                    cuenta.value -= 360
                    print('Se han ganado 360 €')
                else:
                    dinero_hilos[j] -= 10
                    cuenta.value += 10
                    print('Se han perdido 10 €')
        for i in range(jugadas):
            Casino.comprobar_dinero(dinero_hilos)
            for j in range(len(dinero_hilos)):
                Casino.comprobar_dinero(dinero_hilos)
                pool.apply_async(Casino.jugar_par_impar, (cuenta, 10, random.choice(['par', 'impar'])))
                print('Se han apostado', 10, '€ a', random.choice(['par', 'impar']))
                if numero % 2 == 0 and numero != 0 and random.choice(['par', 'impar']) == 'par':
                    dinero_hilos[j]+= 20
                    cuenta.value -= 20
                    print('Se han ganado 20 €')
                else:
                    dinero_hilos[j] -= 10
                    cuenta.value += 10
                    print('Se han perdido 10 €')
        for i in range(jugadas):
            Casino.comprobar_dinero(dinero_hilos)
            for j in range(len(dinero_hilos)):
                Casino.comprobar_dinero(dinero_hilos)
                dinero_martingala = 10
                pool.apply_async(Casino.jugar_martingala, (cuenta, dinero_martingala, random.randint(1, 36)))
                print('Se han apostado', 10, '€ a', random.randint(1, 36))
                if numero == random.randint(1, 36):
                    dinero_hilos[j] += 360
                    cuenta.value -= 360
                    print('Se han ganado 360 €')
                else:
                    dinero_hilos[j] -= 10
                    cuenta.value += 10
                    print('Se han perdido 10 €')
                    dinero_martingala *= 2
                    pool.apply_async(Casino.jugar_martingala, (cuenta, dinero_martingala, random.randint(1, 36)))
        pool.close()
        pool.join()
        print(f'El saldo de la cuenta final es de {cuenta.value} €')
        print(f"El saldo final de los jugadores es de {dinero_hilos} €")

def iniciar_ej2():
    Casino.main()
```

<h2 align = "center">UML</h2>

![image](https://user-images.githubusercontent.com/91721855/234058890-0cd1de4f-7d34-4b7a-8d93-9db73db00bfc.png)

![image](https://user-images.githubusercontent.com/91721855/234058137-8aee413c-bd8a-4fdb-b909-623e89b610c9.png)

