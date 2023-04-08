'''
17. Faça um Programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. Considere que a cobertura da tinta é de 1 litro para cada 6 metros quadrados e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00 ou em galões de 3,6 litros, que custam R$ 25,00.

Informe ao usuário as quantidades de tinta a serem compradas e os respectivos preços em 3 situações:
    comprar apenas latas de 18 litros;
    comprar apenas galões de 3,6 litros;
    misturar latas e galões, de forma que o desperdício de tinta seja menor. 
    
Acrescente 10% de folga e sempre arredonde os valores para cima, isto é, considere latas cheias.

'''
import math

area_a_pintar = float(input("Favor, informe o total em m² de área a ser pintada: \n")) * 1.1

area_por_lata = 108 # 18 litros * 6 metros (p/litro)
area_por_galao = 21.6 # 3.6 litros * 6 metros (p/litro)

qtdadeLatas = math.ceil(area_a_pintar / area_por_lata)
qtdadeGaloes = math.ceil(area_a_pintar / area_por_galao)
   
valorTotal_latas = qtdadeLatas * 80
valorTotal_galoes = qtdadeGaloes * 25

print (f'A quantidade total de latas de tinta que serão necessárias para pintar com folga {area_a_pintar:.1f}m², é {qtdadeLatas} latas. Isto custa R${valorTotal_latas:.2f}.')

print (f'Ou você pode comprar um total de {qtdadeGaloes} galões de tinta, no valor de R${valorTotal_galoes:.2f}.')

# Agora calcula da mistura entre latas e galoes

qtdadeLatas_mistura = int(area_a_pintar / area_por_lata)
qtdadeGaloes_mistura = int ((((area_a_pintar / area_por_lata) - qtdadeLatas_mistura) * 18) / 3.6) # O que sobra da qtdade de latas max, dá quantos galoes? 

# ajustando qtdade excedente de galoes
if (((((area_a_pintar / area_por_lata) - qtdadeLatas_mistura) * 18) % 3.6) != 0):
    qtdadeGaloes_mistura += 1
    
valorTotal_mistura = (qtdadeLatas_mistura * 80) + (qtdadeGaloes_mistura * 25)

print (f'Você pode também misturar as tintas. Comprando {qtdadeLatas_mistura} latas e {qtdadeGaloes_mistura} galões, com valor total de R${valorTotal_mistura:.2f}.')


  