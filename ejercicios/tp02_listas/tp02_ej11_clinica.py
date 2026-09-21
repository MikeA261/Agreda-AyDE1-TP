
def tipo_atencion(pacientes: list,tipo: list)->tuple:
  """
  """
  urgencia= []
  turno= []
  for p,t in zip(pacientes,tipo):
    if t == 0:
        urgencia.append(p)
    else:
        turno.append(p)
  return urgencia,turno

'def busca_socio(socios):'

def main():
    listasocio= []
    atencion = []
    while True:
        numsocio = int(input('Ingrese numero de socio (4 digitos): '))
        if numsocio == 0 or numsocio == -1:
            break
        elif numsocio >= 1000 and numsocio <= 9999:
            listasocio.append(numsocio)
            tipo= int(input('Ingreso por urgencia(0) o por turno(1). Finalizar -1: '))
            atencion.append(tipo)
        else:
            print('Error numero incorrecto')

    print(listasocio)
    print(atencion)

    urgencia= tipo_atencion(listasocio,atencion)



    print(f'Socios atendidos por urgencia: {urgencia[0]}')
    print(f'Socios atendidos por turno: {urgencia[1]}')


if __name__ == '__main__':
  main()

