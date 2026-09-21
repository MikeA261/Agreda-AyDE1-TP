def diasiguiente(d: int,m: int,a: int)-> int :
  """
  
  """
  if True:
    d += 1
    if d > 31:
      d = 1
      m += 1
      if m > 12:
        m= 1
        a += 1
  return d,m,a

def sumar_dias(d,m,a,n):
  if True:
    d += n
    if d > 31:
      mes= d // 31
      d = d % 31
      m += mes
      if m > 12:
        año= m // 12
        m = m % 12
        a += año
  return d,m,a

def main():
    print(diasiguiente(25,8,2022))

    while True:
        accion= int(input('Presione 1 para sumar dias o 2 para calcular los dias de diferencia entre fechas: '))
        if accion == 1:
            sumar=int(input('Dias a sumar: '))
            print(sumar_dias(10,10,2022,sumar))
            break


if __name__ == '__main__':
   main() 