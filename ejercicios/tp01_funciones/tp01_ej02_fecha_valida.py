
def validar_fecha(d = int,m = int,a = int)->bool:
    """Esta funcion busca validar la fecha ingresada por el usuario
       
       Pre: se deben de ingresar numeros enteros validos

       Pos: en caso de ser valida retornar True, de lo contratario False
    """
    meses_pares = [4,6,9,11]
    meses = [1,2,3,4,5,6,7,8,9,10,11,12]

    if d >= 1 and d <= 31:
        if m >= 1 and m <= 12:
            if a >= 1:
                validacion = True
            else:
                validacion = False
        else:
            validacion = False
    else:
        validacion = False

    for i in range(len(meses)):
        if m != meses[i]:
            for j in range(len(meses_pares)):
                if m == meses_pares[j]:
                    if d <= 30:
                        mescorrecto = True
                    else:
                        mescorrecto = False
        else:
            mescorrecto = True
    
    if validacion:
        if mescorrecto:
            fecha = True
            a = a % 4
            if a != 0:
               print("Es año no biciesto")
            else:
               print("Es año biciesto")
        else:
            fecha= False
    else:
        fecha= False
    return fecha

d = int(input("Ingrese un Dia: "))
m = int(input("Ingrese Mes: "))
a = int(input("Ingrese un Año: "))

print(validar_fecha(d,m,a))