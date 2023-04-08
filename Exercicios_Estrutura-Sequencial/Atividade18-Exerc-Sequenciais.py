'''
18. Faça um programa que peça o tamanho de um arquivo para download (em MB) e a velocidade de um link de Internet (em Mbps), calcule e informe o tempo aproximado de download do arquivo usando este link (em minutos).
'''

tamanho_arquivo = float(input('Favor informar o tamanho do arquivo, em MB: '))

velocidadeLink_Mbps = float(input('Agora informe a velocidade de download do link, em Mbps: '))

tempoDownload_segundos = tamanho_arquivo / velocidadeLink_Mbps


tempoDownload_Minutos = tempoDownload_segundos / 60

print(f'O download deste arquivo leva {tempoDownload_Minutos:.3f} minutos')