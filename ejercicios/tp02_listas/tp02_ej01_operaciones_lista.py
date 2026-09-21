import random as rm


def lista_nueva(a: int,b: int,n1: int,n2: int)->list:
  """
  """
  listanueva= []
  for j in range(rm.randint(n1,n2)):
    listanueva.append(rm.randint(a,b))
  return listanueva

def sumar_elementos(lista):
  suma= 0
  for j in range(len(lista)):
    suma += lista[j]
  return suma

def eliminar_valor(valor,lista):
  lista.remove(valor)
  return lista

def funcion_capi():
    return



print('Ingrese 1 para generar un lista')
while True:
  generar= int(input(''))
  if generar == 1:
    lista=lista_nueva(1000,9999,10,99)
    print(lista)
    break



while True:
  print(f'Ingrese 2 para sumar los valores o 3 para eliminar uno')
  print(f'Ingrese 1 para generar otra lista o 4 para determinar si es capicua')
  funcion= int(input(''))
  if funcion == 2:
    suma= sumar_elementos(lista)
    print(f'Valor total {suma}')
  elif funcion == 3:
    eliminar= int(input(f'Ingrese el valor a eliminar: '))
    lista=eliminar_valor(eliminar,lista)
    print(lista)
  elif funcion == 4:
    funcion_capi(lista)


     