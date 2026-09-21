import random as rm


def cant_naranjas():
  cantidad = rm.randint(10000,30000)
  return cantidad


def clasif_naranjas(cant):
  paracaj=0
  pesocaj=0
  parajugo=0
  for j in range(cantidad):
    peso= rm.randint(150,350)
    if peso <= 300:
      paracaj += 1
      pesocaj += peso
    elif peso >= 300:
      parajugo += 1
  return paracaj,parajugo,pesocaj

def numero_cajas(cantidad,peso):
  cajas = cantidad // 100
  return cajas

def cajas_camion(cajas,peso):
  pesok = peso // 1000
  camiones = pesok // 500 
  sobrante = pesok % 500
  if sobrante >= (500*0.8):
    camiones += 1
    sobrante = 0
  return camiones, sobrante


cantidad= (cant_naranjas())
print(f'Cantidad total de naranjas cosechadas: {cantidad}')

clasificacion= clasif_naranjas(cantidad)
print(f'Cantidad de naramjas para envio: {clasificacion[0]}, cantidad de naranjas para jugo: {clasificacion[1]}')

cajas= numero_cajas(clasificacion[0],clasificacion[2])
print(f'Numero de cajas a enviar: {cajas}')

camion= cajas_camion(cajas,clasificacion[2])
print(f'Camiones necesarios para el envio : {camion[0]}. Sobrante de naranjas para el proximo envio {camion[1]}Kg ')