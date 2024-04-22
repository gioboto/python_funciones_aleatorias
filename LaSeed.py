from random import seed, random, randint, sample

# seed(1)  # misma semilla para generar
seed(200) # misma semilla para generar

print(f'{random() = }')
print(f'{randint(1, 5) = }')
print(f'{sample(range(1000), k=5) = }')

print("=" * 40)

# para ver como  crush el program, probar limites 

