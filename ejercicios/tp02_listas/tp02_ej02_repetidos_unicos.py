import random as rm

def lista_nueva(a: int,b: int,n1: int)->list:
  """
  """
  listanueva= []
  for j in range(n1):
    listanueva.append(rm.randint(a,b))
  return listanueva

def valor_repetido(lista: list)->list:
  """
  """
  for j in range(len(lista)):
    if lista [j] == lista[j]:
      duplicado = True
  return duplicado

def valores_unicos(lista: list)-> list:
  """
  """
  if True:
    listan=list(set(lista))
  return listan




def main():
    cantidad = int(input(f'Ingrese la cantidad de elementos de la lista: '))
    lista = lista_nueva(1,100,cantidad)
    print(lista)

    print(valor_repetido(lista))

    listan= valores_unicos(lista)
    print(listan)


if __name__ == '__main__':
  main()