# Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou ÍMPAR.

print("#" * 40)
print('          JOGO DO PAR ou ÍMPAR')
print("#" * 40)
num = int(input('Digite um número inteiro -> '))
print(f'{num} -> {"[PAR]" if num % 2 == 0 else "[ÍMPAR]"}')
