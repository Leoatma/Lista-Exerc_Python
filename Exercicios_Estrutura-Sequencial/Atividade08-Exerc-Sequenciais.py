'''
08. Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês.
'''

remuneracaoHora = float(input('Favor informe o valor por hora de sua remuneração: U$'))

horasTrabalhadaspMes = float(input('Agora, quantas horas foram contabilizadas este mês? '))

salarioMensal = remuneracaoHora * horasTrabalhadaspMes

print(f'O salário este mês será de U${salarioMensal:.2f}.')