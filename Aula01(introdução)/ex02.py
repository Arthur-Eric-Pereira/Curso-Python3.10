#ex02: Faça um programa que leia o nome de uma pessoa e mostre uma mensagem de boas-vindas!

print('>> COMPUTADOR: Olá usuário! Como você se chama ?')
nome = str(input('>> USUÁRIO: '))
print('-'*60)
print(f'Oi \033[4;34m{nome}\033[m ! Seja Bem Vindo ao Mundo da Programação em Python.')
