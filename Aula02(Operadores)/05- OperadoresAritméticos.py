# OPERADORES ARITMÉICOS:
'''
+ Adição
- Subtração
* Multiplicação
/ Divisão
^ Potenciação
% Resto da Divisão
// Divisão Inteira

'''

import random
print('--'*20)
a = random.randint(1,100)
b = random.randint(1,100)
print(f'Número [A]: {a}')
print(f'Número [B]: {b}')
print(f' {a} + {b} = {a+b}')
print(f' {a} - {b} = {a-b}')
print(f' {a} * {b} = {a*b}')
print(f' {a} / {b} = {a/b:.2f}')
print(f' {a} // {b} = {a//b}')
print(f' {a} % {b} = {a%b}')
print(f' {a} ** {b} = {a**b:.2f}')
