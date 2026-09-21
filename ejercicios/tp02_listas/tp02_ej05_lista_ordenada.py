def lista_ordenada(lista: list)->list:
  """
  """

  ordenada= sorted(lista)
  for j in lista:
    for i in ordenada:
      if i != j:
        orden=False
      else:
        orden=True
  return print(orden)


def main():
    lista= [4,8,6,1]
    lista_ordenada(lista)
  

if __name__ == '__main__':
  main()

