# Faça um programa que leia três números e mostre qual é o maior e qual é o menor.

n1 = int(input('NÚMERO 1: '))
n2 = int(input('NÚMERO 2: '))
n3 = int(input('NÚMERO 3: '))

if n1 == n2 and n2 == n3:
    print('TODOS OS VALORES SÃO IGUAIS!')
elif n1 >= n2 and n1 >= n3:
    print(f'{n1} É O MAIOR VALOR!')
elif n2 >= n1 and n2 >= n3:
    print(f'{n2} É O MAIOR VALOR!')
elif n3 >= n1 and n3 >= n2:
    print(f'{n3} É O MAIOR VALOR!')
print('------------------')
if n1 <= n2 and n1 <= n3:
    print(f'{n1} É O MENOR VALOR!')
elif n2 <= n1 and n2 <= n3:
    print(f'{n2} É O MENOR VALOR!')
elif n3 <= n1 and n3 <= n2:
    print(f'{n3} É O MENOR VALOR!')
