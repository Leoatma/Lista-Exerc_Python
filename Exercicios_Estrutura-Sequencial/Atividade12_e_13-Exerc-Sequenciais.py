'''
13. Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo que calcule seu peso ideal, utilizando as seguintes fórmulas:
Para homens: (72.7*h) - 58
Para mulheres: (62.1*h) - 44.7
'''

user_height = float(input("Favor informe a sua altura: "))

user_gender = (input("Qual o seu sexo? \n'H' - Homem \n'M' - Mulher \n").upper())

idealWeight_Man = (72.7 * user_height) - 58

idealWeight_Woman = (62.1 * user_height) - 44.7

if (user_gender == 'H'):
    idealWeight = idealWeight_Man
    print(f"O seu peso ideal é {idealWeight:.1f} kg.")
elif (user_gender == 'M'):
    idealWeight = idealWeight_Woman
    print(f"O seu peso ideal é {idealWeight:.1f} kg.")
else:
    print('Favor informe o sexo corretamente.')
  
  
  
  