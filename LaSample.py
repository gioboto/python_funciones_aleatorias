from random import sample

# retorna elemento sunicos de un rango en este caso
print(sample(range(100), k=10))

print("=" * 40)

# retorna elemento sunicos de un rango pero en este caso la lista cada elemento se lo toma como unico 
print(sample([1,1,3,4,5], k=2))


print("=" * 40)
colores: list[str] =['amarillo', 'azul', 'rojo']
print(sample(colores, k=5, counts=(10, 20, 15)))