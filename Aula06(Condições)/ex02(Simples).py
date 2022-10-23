#   Escreva um programa que faça o computador “pensar” em um número inteiro entre 0 e 7 e peça para o usuário
#        tentar descobrir qual foi o número escolhido pelo computador.
#        O programa deverá escrever na tela se o usuário venceu ou perdeu.

from random import randint
print()
print('\033[1;36m=-=\033[m'*20)
print('{: ^70}'.format('\033[4;36mJOGO DA ADIVINHAÇÃO\033[m'))
num = int(input('Adivinhe qual número o computador está pensando entre [0 até 7]: '))
computador = randint(0, 7)
print('\033[1;36m=-=\033[m'*20)

if num == computador:
    print('\033[1;30;42m ACERTOU ! PARABÉNS :) !\033[m ->', computador)
else:
    print('\033[1;30;41m ERROU :P Hahahaa !\033[m -> ', computador)
