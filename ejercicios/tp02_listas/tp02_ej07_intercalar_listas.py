def intercalar_listas(lista1: list,lista2: list)->list:
  """
  """
  for j in range(len(lista2)):
    lista1[(j*2+1):(j*2+1)] = lista2[j:j+1]
  return print(lista1)


def main():
    lista1= [1,1,1,1,1,1]
    lista2= [2,2,2,2,2,2]
    intercalar_listas(lista1,lista2)


if __name__ == '__main__':
  main()
