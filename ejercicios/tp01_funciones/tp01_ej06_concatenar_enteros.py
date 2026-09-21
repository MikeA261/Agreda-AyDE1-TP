def concatenar(valor1:int, valor2: int)->int:
    """La función debe concatenar dos números 
        que se reciben como parametros

        Pre: Se reciben dos numeros enteros como parámetros 

        Post: Se retorna un solo numero entero.
    """

    numero1= str(valor1)
    numero2= str(valor2)
    concatenado= []
    final= str

    if valor1 >= 0:
        for n in numero1:
            concatenado.append(n)

    if valor2 >= 0:
        for n in numero2:
            concatenado.append(n)

    final =int(''.join(map(str, concatenado)))
    
    return final



def main():
    print(concatenar(525,111))


if __name__ == '__main__':
    main()   