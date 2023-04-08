'''
15. Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês, sabendo-se que são descontados 11% para o Imposto de Renda, 8% para o INSS e 5% para o sindicato, faça um programa que nos dê:
  - salário bruto.
  - quanto pagou ao INSS.
  - quanto pagou ao sindicato.
  - o salário líquido.
  - calcule os descontos e o salário líquido, conforme a tabela abaixo:
    + Salário Bruto : R$
    - IR (11%) : R$
    - INSS (8%) : R$
    - Sindicato ( 5%) : R$
    = Salário Liquido : R$

Obs.: Salário Bruto - Descontos = Salário Líquido.
'''

salario_por_hora = float(input("Favor, informe o quanto você recebe por hora trabalhada: \n"))

numero_horas_trabalhadas = float(input("Quantas horas você trabalhou este mês? \n"))

salarioBruto = numero_horas_trabalhadas * salario_por_hora

descontoIR = salarioBruto * 0.11

descontoINSS = salarioBruto * 0.08

descontoSindicato = salarioBruto * 0.05

salarioLiquido = salarioBruto - descontoIR - descontoINSS - descontoSindicato

print(f'Este mês o seu salário foi de R${salarioLiquido:.2f}. O que corresponde ao salário bruto ({salarioBruto:.2f} reais) menos os descontos de IR, INSS e Sindicato.')