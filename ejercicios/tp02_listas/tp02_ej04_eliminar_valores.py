def eliminar_valores(lista1: list, lista2: list)-> list:
  """
  """
  lista3=[]
  for i in lista1:
    if i not in lista2:
        lista3.append(i)
  return lista3


def main():
  
    lista1= [20,30,40,50,60]
    print(lista1)
    lista2=[20,60]
    print(lista2)

    lista1 = eliminar_valores(lista1,lista2)
    print(lista1)

if __name__ == '__main__':
  main()