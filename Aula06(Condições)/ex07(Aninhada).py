#   Escreva um programa em Python que leia um número inteiro qualquer e peça para o usuário escolher qual será a
#   base de conversão:
#    - 1 para binário,
#    - 2 para octal
#    - 3 para hexadecimal.

num = int(input('>>>>>>>>>>>> DIGITE UM NÚMERO INTEIRO: '))
print('''ESCOLHA UMA BASE DE CONVERSÃO:
        [1]- Binário
        [2]- Octal
        [3]- Hexadecimal''')
opcao = int(input('>>> '))
if opcao == 1:
    print(f'{num} em Binário -> {bin(num)[2:]}')
elif opcao == 2:
    print(f'{num} em Octal -> {oct(num)[2:]}')
elif opcao == 3:
    print(f'{num} em Hexadecimal -> {hex(num)[2:]}')
else:
    print('ENCERRANDO O PROGRAMA _ _ _ _')
