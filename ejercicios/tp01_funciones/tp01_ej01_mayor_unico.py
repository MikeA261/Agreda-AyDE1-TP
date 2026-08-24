def mayor_unico (a = int,b = int,c= int):
    """Se busca el mayor unico estricto de los tres valores ingresados

        Pre: Todos los numeros deben ser enteros

        Pos: Debe retornar el mayor unico, si no existe retornar un -1
    """
    if a > b:
        if a > c:
            mayor= a
    if b > a:
        if b > c:
            mayor= b
    if c > a:
        if c > b:
            mayor= c

    if a == c:
        return -1
    if a == b:
        return -1
    if b == c:
        return -1

    return mayor


a = int(input("Elija un numero: "))
b = int(input("Elija un numero: "))
c = int(input("Elija un numero: "))

print(mayor_unico(a,b,c))