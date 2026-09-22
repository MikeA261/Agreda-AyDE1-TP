import random as rm

def cargar_matriz(c: int)->list:
    """ Se encarga de crear una matriz aleatorea

        Pre: Recibe como parametro un numero entero qeu dicta
             la cantidad de filas y columnas

        Post: La funcion devuelve una matriz simétrica
    """
    matriz = [[]for _ in range(c)]
    for _ in range(c):
        for i in range(c):
            matriz[i].append(rm.randint(1,20))
    return matriz
  
  
def ordenar_filas(m: list)-> list:
    """ Esta funcion se encarga de ordenar de forma ascendente
        los elementos de las filas

        Pre: recive como parámetro la matriz creada

        Post: devuelve una matriz
    """
    for j in m:
        j.sort()
    return m

def cambiar_filas(m: list,f1: int,f2: int)->list:
    """ Esta funcion intercambia filas entre si

        Pre: recive una matriz,y recive dos numeros enteros
             siendo estos las filas a intercambiar 

        Post: se retorna una matriz
    """
    m[f1-1], m[f2-1] = m[f2-1], m[f1-1]
    return m


def cambiar_columnas(m: list,c1: int,c2: int)->list:
    """ Esta funcion intercambia columnas entre si

        Pre: recive una matriz,y recive dos numeros enteros
             siendo estos las columnas a intercambiar.

        Post: se retorna una matriz
    """
    for i in range(len(m[0])):
        m[i][c1-1], m[i][c2-1] = m[i][c2-1], m[i][c1-1]
    return m
        

def transponer(m: list)->list:
    """ Traspone la matriz sobre si misma.

        Pre: recibe como parámetro una matriz.

        Post: retorna una matriz. 
    """
    colum= len(m[0])
    filas= len(m)
    for j in range(filas):
        for i in range(j+1, colum):
            m[j][i], m[i][j] = m[i][j], m[j][i]
    return m

def promedio_fila(m: list, f: int)-> float:
    """
    """
    return (sum(m[f-1]) / len(m[f-1]))


def porcentaje_impar(m: list, c: int)->int:
  """
  """
  largo = len(m[0])
  cantidad= 0
  for j in range(largo):
    if m[j][c-1] % 2 == 1:
      cantidad += 1
  cantidad = (cantidad / largo) * 100
  return cantidad


def imprimir_matriz(m: list)->list:
    """
    """
    print('-'*16)
    for f in range(len(m)):
        print(f"",end='|')
        for c in range(len(m[f])):
            print(f'{m[f][c]:>2}',end='|')
        print()
    print('-'*16)
    print()   
    
    
def main():
    
    while True:
        print("-" * 30)
        print(f' 1 para generar una matriz nueva')
        print(f' 2 para ordenar las filas')
        print(f' 3 para intercambiar filas')
        print(f' 4 para intercambiar columnas')
        print(f' 5 para trasponer la matriz')
        print(f' 6 para calcular el promedio por fila')
        print(f' 7 para calcular el porcentaje de numeros impares por columnas')
        print(f' -1 para salir')
        opcion = int(input())
        if opcion == 1:
            columnas = int(input(f'Ingrese el numero de columnas:  '))
            print('matriz original')
            matriz= cargar_matriz(columnas)
            imprimir_matriz(matriz)
        elif opcion == 2:
            print(f'Filas ordenadas')
            ordenar = ordenar_filas(matriz)
            imprimir_matriz(ordenar)
        elif opcion == 3:
            print(f'Filas cambiadas')
            cambiar_fi = cambiar_filas(matriz,1,2)
            imprimir_matriz(cambiar_fi)
        elif opcion == 4:
            print(f'Columnas cambiadas')
            cambiar= cambiar_columnas(matriz,1,2)
            imprimir_matriz(cambiar)
        elif opcion == 5:
            print(f'Matriz transpuesta')
            transpo= transponer(matriz)
            imprimir_matriz(transpo)
        elif opcion == 6:
            fila = int(input(f'Ingrese la fila a calcular: '))
            promedio= promedio_fila(matriz,fila)
            print(f'El promedio de las filas uno es {promedio}')
        elif opcion == 7:
            columna = int(input(f'Ingrese la columna a calcular: '))
            porcentaje= porcentaje_impar(matriz, columna)
            print(f'El porcentaje de numeros imapares es: {porcentaje}')
        elif opcion == -1:
            break
    

    
if __name__ == '__main__':
    main()