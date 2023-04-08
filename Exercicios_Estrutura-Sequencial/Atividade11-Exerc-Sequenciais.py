'''
11. Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:
    a. o produto do dobro do primeiro com metade do segundo .
    b. a soma do triplo do primeiro com o terceiro.
    c. o terceiro elevado ao cubo.
'''

number1 = int(input("Favor informa 1 número inteiro: "))
number2 = int(input('Agora informe outro número inteiro: '))
number3 = float(input("Forneça agora um número decimal (Exemplo:'x,y'):  "))

resultado_a = (2 * number1) * (number2 / 2)

resultado_b = (3 * number1) + number3

resultado_c = number3 ** 3

print(f'Os resultados são a = {resultado_a}, b = {resultado_b} e c = {resultado_c:.2f}.')
