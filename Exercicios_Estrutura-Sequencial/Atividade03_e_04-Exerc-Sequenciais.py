''' 
03. Faça um Programa que peça dois números e imprima a soma.
04. Faça um Programa que peça as 4 notas bimestrais e mostre a média.
'''

nota1 = float(input("Favor, informe a primeira nota: "))
nota2 = float(input("Agora, informe a segunda nota: "))
nota3 = float(input("Favor, informe a terceira nota: "))
nota4 = float(input("Por último, informe a quarta nota: "))

totalNotas = nota1 + nota2 + nota3 + nota4

mediaNotas = totalNotas / 4

print(f'\nO total de pontuação foi {totalNotas:.2f}, e a média foi {mediaNotas}.')