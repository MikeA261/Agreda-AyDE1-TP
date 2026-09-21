def devolver_vuelto(total: int, abonado: int)->list[int]:
    """Se reciben dos parametros y se calcula el vuelto a deber

        Pre: Se ingresan dos numeros enteros no negativos
    
        Post: Se retorna un numero entero (resultado de la operacion). 
    """

    billetes= [5_000,1_000,500,200,100,50,20,10]
    diferencia = abonado - total
    vuelto= []


    for billete in billetes:
        devolver = diferencia // billete
        diferencia %= billete
        vuelto.append(devolver)

    return vuelto


def main():
    total = int(input(f'Ingrese el monto a pagar: '))
    abonado = int(input(f'Ingrese el monto dado: '))
    vuelto= devolver_vuelto(total,abonado)
    print(f'El vuelto a dar es {vuelto}')


if __name__ == '__main__':
    main()