from math import sqrt
numero = float(input('Digite um Número:\n>>> '))
print(f'RAIZ-QUADRADA: {numero} = {sqrt(numero):.2f}')
print()
#--------------------------------------------------------

import random
contador = random.randint(0,10)
print(f'Número de 0 até 10 sorteado foi {contador}')
print()
#---------------------------------------------------------

import random
nome1 = 'Chico'
nome2 = 'João'
nome3 = 'Maria'
nome4 = 'Pedro'
nome5 = 'Sara'
lista = [nome1, nome2, nome3, nome4, nome5]
escolhido = random.choice(lista)
print(lista)
print(f'>> O aluno escolhido será: {escolhido}')
print()
random.shuffle(lista)
print(lista)
print()
#---------------------------------------------------------