from random import choice, choices

gente: list[str] = ['Tom', 'Claudio', 'Martin', 'Diana', 'Inka' , 'Daphne']

#retorna un solo elemento
print(f'choice() = {choice(gente)}')

#retorna un solo elemento de firna oredeternubada pero se peude indicar cuantos elelentos se quiere imprimir de la lista original
print("=" * 40)
print(f'choices() = {choices(gente, k=3)}')


#retorna un solo elemento de firna oredeternubada pero se peude indicar cuantos elelentos se quiere imprimir de la lista original
#aquí se da pesoso de aparición a los elementos en base a al tupla
print("=" * 40)
pesos: tuple = (.15, .20, .35, .30, .12, .18)
print(f'choices() = {choices(gente, k=3, weights=pesos)}')