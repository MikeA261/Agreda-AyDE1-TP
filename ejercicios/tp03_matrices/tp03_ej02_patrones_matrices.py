import random as rm

def matrizA(c):
    matriz = [[]for _ in range(c)]
    for j in range(c):
        for i in range(c):
            matriz[i].append(0) 
    
    num = 1 

    for i in range(c):
        num += 2
        for j in matriz:
            matriz[i].pop(i)
            matriz[i].insert(i, num - 2)
    
    return matriz

def matrizB(c):
    matriz = [[]for _ in range(c)]
    for j in range(c):
        for i in range(c):
            matriz[i].append(0) 
    
    num = 4 
    multi = 3 ** c
    divi = 1
    for i in range(c):
        num -= 1
        numero = multi // 3
        multi = numero
        for j in matriz:
            matriz[i].pop(num)
            matriz[i].insert(num, multi)
    return matriz

def matrizC(c):
    matriz = [[]for _ in range(c)]
    for j in range(c):
        for i in range(c):
            matriz[i].append(0) 
    
    
    num = 4 
    for i in range(c):
        num -= 1
        for j in range(i + 1):
            matriz[i][j] = num + 1
    
    return matriz

def matrizD(c):

    matriz = [[]for _ in range(c)] 
    num = 16
    for i in range(c):
        valor = num // 2
        for j in matriz:
            matriz[i].append(valor)


            
    return matriz



def imprimir_matriz(m: list)->list:
    """
    """
    print('-'*17)
    for f in range(len(m)):
        print(f"",end='|')
        for c in range(len(m[f])):
            print(f'{m[f][c]:>2}',end=' |')
        print()
    print('-'*17)
    print()   
    
    
def main():
    ma= matrizA(4)
    imprimir_matriz(ma)
    mb= matrizB(4)
    imprimir_matriz(mb)
    mc= matrizC(4)
    imprimir_matriz(mc)
    md= matrizD(4)
    imprimir_matriz(md)

if __name__ == '__main__':
    main()