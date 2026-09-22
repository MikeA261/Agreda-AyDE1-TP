import random as rm

def rellenar_matriz(n: int)->list:
    """ Esta función crea una matriz N x N con números enteros al
        azar comprendidos en el intervalo [0,N2)

        Pre: recibe como parámetro un numero entero que determina
            el tamaño de la matriz

        Post: retorna una matriz
    """
    m = [[] for i in range(n)]
    limite = n ** 2 - 1
    for i in range(n):
        for j in range(n):
            while True:
                num = rm.randint(0, limite)
                if not any(num in lista for lista in m):
                    m[i].append(num)
                    break
    return m


def print_matriz(m: list)->list:
    for fila in m:
        print('|', end = '')
        for elem in fila:
            print(f'{elem:>3}', end=' ')
        print('|', end = '')
        print()
    print()

def main():
    matriz = rellenar_matriz(4)
    print_matriz(matriz)

if __name__ == '__main__':
    main()
