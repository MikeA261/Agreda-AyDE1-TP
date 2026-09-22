import random as rn

lista1 = [x for x in range(rn.randint(1,101))]
print(lista1)
lista2 = list(filter(lambda x : x % 2, lista1))
print(lista2)