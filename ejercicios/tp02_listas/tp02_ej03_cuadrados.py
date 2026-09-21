import random as rm

def lista_nueva(a: int,n: int)->list:
  listanueva= []
  for j in range(n):
    listanueva.append(rm.randint(a,n))
  print(listanueva)
  return listanueva

def devolver(lista: list)->list:

   return



def main():
    lista= lista_nueva(1,20)

    mi_lista= list(map(lambda x : x ** 2, lista))
    print(mi_lista)
    aceptar= input(f'¿Desea imprimir los ultimos valores? SI/NO:  ')
    if aceptar.upper == "Si":
        devolver(mi_lista)
    else:
        pass

if __name__ == '__main__':
   main()