'''
16. Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00. Informe ao usuário a quantidades de latas de tinta a serem compradas e o preço total.
'''

area_a_pintar = float(input("Favor, informe o total em m² de área a ser pintada: \n"))

area_por_lata = 54

qtdadeLatas = int(area_a_pintar / area_por_lata)

if (qtdadeLatas < (area_a_pintar / area_por_lata)):
    qtdadeLatas += 1
    
valorTotal = qtdadeLatas * 80
  
print (f'A quantidade total de latas de tinta que serão necessárias para pintar {area_a_pintar}m², é {qtdadeLatas} latas. Isto custa R${valorTotal:.2f}.')