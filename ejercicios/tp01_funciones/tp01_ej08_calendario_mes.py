def diadelasemana(dia,mes,año):
    if True:
      mes = mes - 2
      siglo= año // 100
      año2= año % 100
      diasem= (((26*mes-2)//10)+ dia + año2 + (año2 // 4) + (siglo // 4) - (2 * siglo))% 7
      if diasem < 0:
        diasem = diasem + 7
    return diasem

def main():
    for j in range(1,31):
        fecha= diadelasemana(j,9,2022)
        if fecha == 0:
            print(f'Domingo   {j}')
        if fecha == 1:
            print(f'Lunes     {j}')
        if fecha == 2:
            print(f'Martes    {j}')
        if fecha == 3:
            print(f'Miercoles {j}')
        if fecha == 4:
            print(f'Jueves    {j}')
        if fecha == 5:
            print(f'Viernes   {j}')
        if fecha == 6:
            print(f'Sabado    {j}')


if __name__ == '__main__':
    main()