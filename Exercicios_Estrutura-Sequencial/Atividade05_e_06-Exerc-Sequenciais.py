'''
05. Faça um Programa que converta metros para centímetros.
06. Faça um Programa que peça o raio de um círculo, calcule e mostre sua área.
'''
from math import pi

raioMetros = float(input('Informe o raio da circunferência em metros: '))

raioCentimetros = raioMetros * 100

areaCirculo = pi * (raioCentimetros ** 2)

print(f'Com raio de {raioCentimetros:.1f}cm, o círculo tem {areaCirculo:.2f}cm² de área.')