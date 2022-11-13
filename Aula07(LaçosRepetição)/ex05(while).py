# Melhore o jogo onde o computador vai "pensar" em um número entre 0 e 7. Só que agora o jogador
# vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer.

print()
import random
print('\033[1;36m=-=\033[m'*20)
print('{: ^70}'.format('\033[4;36mJOGO DA ADIVINHAÇÃO\033[m'))
acertou = False
palpites = 0
n = random.randint(0, 7)
while not acertou:
    num = int(input('Digite qual número o computador está pensando entre [0 até 7]: '))
    print('_'*60)
    if num == n:
        print('\033[1;30;42m ACERTOU :)     PARABÉNS!\033[m ->', n)
        break
    else:
        print('\033[1;30;41m ERROU :P     Hahahaa!\033[m')
        palpites += 1
print('_'*60)
print(f'Você precisou de {palpites} vezes até acertar !!')
