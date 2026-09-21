def normalizar_lista(lista: list)->list:
    """
    """
    total = sum(lista)
    lista2= []
    for numero in lista:
        num= numero/total
        lista2.append(num)

    suma= 0
    for j in range(len(lista2)):
        suma += lista[j]

    return print(lista2)


def main():
    lista= [1,1,2,3,4]
    normalizar_lista(lista)



if __name__ == '__main__':
  main()

    
