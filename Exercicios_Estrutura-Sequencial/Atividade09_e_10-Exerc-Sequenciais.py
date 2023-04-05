'''
09. Faça um Programa que peça a temperatura em graus Fahrenheit, transforme e mostre a temperatura em graus Celsius.
C = 5 * ((F-32) / 9).

10. Faça um Programa que peça a temperatura em graus Celsius, transforme e mostre em graus Fahrenheit.
'''

temperatura_A_Celsius = float(input('Qual a temperatura A em graus Celsius? '))

temperatura_B_Fahrenheit = float(input('Informe uma temperatura B em graus Fahrenheit: '))

temperatura_A_Fahrenheit = ((9 * temperatura_A_Celsius) / 5) + 32

temperatura_B_Celsius = 5 * ((temperatura_B_Fahrenheit - 32) / 9)

print(f'A temperatura A corresponde a {temperatura_A_Fahrenheit:.1f}ºF, e a temperatura B em {temperatura_B_Celsius:.1f}ºC.')