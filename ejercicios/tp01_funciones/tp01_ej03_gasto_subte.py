def descuento_subte(viajes = int)->float:
    """ La funcion devuelve el precio final de la cantidad de viajes
        con los descuentos aplicados.

        Pre: la funcion recibe un entero como parametro de viajes.

        Post: Se retorna un int (el total del precio).
    """

    descuentos = [40, 30, 20]
    aplicable= [41,31,21]
    precio = 1000
    final= 0

    if viajes <= 20:
        final= viajes * precio
        return final

    for aplica,desc in zip(aplicable,descuentos):
        if aplica <= viajes:
            diferencia = viajes - (aplica - 1)
            final += diferencia * precio * (1 - desc / 100)
            viajes -= diferencia

    final += viajes * precio

    return final






   
    

viajes = int(input("Ingrese la cantidad de viajes que realizo: "))
gastos= descuento_subte(viajes)
print(f'El monto total gastado es de ${gastos}')