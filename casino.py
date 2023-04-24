import multiprocessing
import time
import random
from introducir.numero import introducir_numero


class Casino:
    def jugar_numero(cuenta, cantidad, numero):
        cuenta.value -= cantidad
        print('Se han apostado', cantidad,
              '€ al número', numero)
        time.sleep(3)

    def jugar_par_impar(cuenta, cantidad, par_impar):
        cuenta.value -= cantidad
        print('Se han apostado', cantidad,
              '€ a', par_impar)
        time.sleep(3)

    def jugar_martingala(cuenta, cantidad, numero):
        cuenta.value -= cantidad
        print('Se han apostado', cantidad,
              '€ a', numero)
        time.sleep(3)

    def main():
        jugadas = introducir_numero('Introduce el número de jugadas: ')
        pool = multiprocessing.Pool(processes=4)
        dinero_hilos =[1000, 1000, 1000, 1000]
        cuenta = multiprocessing.Value('i', 5000)
        numero = random.randint(1, 36)
        if sum(dinero_hilos) <= 0:
            print('El jugador', i, 'se ha quedado sin dinero')
        else:
            for i in range(jugadas):
                for j in range(len(dinero_hilos)):
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
                for j in range(len(dinero_hilos)):
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
                for j in range(len(dinero_hilos)):
                    pool.apply_async(Casino.jugar_martingala, (cuenta, 10, random.randint(1, 36)))
                    print('Se han apostado', 10, '€ a', random.randint(1, 36))
                    if numero == random.randint(1, 36):
                        dinero_hilos[j] += 360
                        cuenta.value -= 360
                        print('Se han ganado 360 €')
                    else:
                        dinero_hilos[j] -= 10
                        cuenta.value += 10
                        print('Se han perdido 10 €')
            pool.close()
            pool.join()
            print(f'El saldo de la cuenta final es de {cuenta.value} €')
            print(f"El saldo final de los jugadores es de {dinero_hilos} €")

def iniciar_ej2():
    Casino.main()