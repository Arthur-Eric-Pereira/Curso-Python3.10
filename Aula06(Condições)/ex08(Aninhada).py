#   Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade, se ele ainda
#   vai se alistar ao serviço militar, se é a hora exata de se alistar ou se já passou do tempo do alistamento.
#   Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.

from datetime import date
ano_atual = date.today().year
nasc = int(input('Ano de seu nascimento: '))
idade = ano_atual - nasc
print('Você nasceu em {} e tem {} anos em {}.'.format(nasc, idade, ano_atual))
if idade == 18:
    print('> \033[31mVOCÊ DEVE SE ALISTAR IMEDIATAMENTE\033[m !')
elif idade < 18:
    print("> \033[34mVOCÊ AINDA NÃO TEM IDADE SUFICIENTE PARA SE ALISTAR\033[m! AINDA FALTA {} ANO'S".format(18-idade))
else:
    print("> \033[33mVOCÊ JÁ DEVERIA TER SE ALISTADO À {} ANO'S\033[m".format(idade-18))
