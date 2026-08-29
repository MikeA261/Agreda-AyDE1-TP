def descuento_subte(viajes = int)->float:

    if viajes:
        viajes -= 20
        precio = 20 * 1_000
        preciototal = precio
        if viajes > 10:
            viajes -= 10
            precio2 = 10 * 800
            preciototal = precio + precio2
            if viajes > 10:
                viajes -= 10
                if viajes < 10:
                    precio3 = viajes * 700
                    preciototal = precio + precio2 + precio3
                    if viajes > 10:
                        viajes -= 10
                        precio4 = viajes * 600
                    else:
                        precio4 = viajes * 600
                        preciototal= precio + precio2 + precio3 + precio4
            else:
                precio3= viajes * 700
                preciototal = precio + precio2 + precio3
        else:
            precio2 = viajes * 800
            preciototal = precio + precio2
   
    return float(preciototal)

viajes = int(input("Ingrese la cantidad de viajes que realizo: "))

print(descuento_subte(viajes))