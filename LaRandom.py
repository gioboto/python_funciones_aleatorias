from random import random, randint, randrange

valor: float = random()
# imprime un valor entre cero y uno
print (f'random() = {valor}')

print("="*30)
valores: list[int] = [randint(10, 20) for _ in range(5)]
print(f'randit() = {valores}')

print("="*30)
# el valor de 1o no va a ser impreso no importa cuatnas veces se haga se ejecute el codigo, y se puede establecer saltos ejem 2
valores2: list[int] = [randrange(0, 10, 2) for _ in range(5)]
print(f'randrange() = {valores2}')