from random import shuffle

Iteraciones = 5

gente: list[str] = ['Tom', 'Claudio', 'Martin', 'Diana', 'Inka' , 'Daphne']

for G in range(Iteraciones):
    shuffle(gente)
    print(gente)
    G += 1