#Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.

print('     AUMENTO DE SALÁRIO')
print('$-$'* 10)
print()
salario_atual = float(input('Digite seu salário atualmente:  '))
aumento = salario_atual + (salario_atual * 15 / 100)
print(f'''>>>> Você ganhou um aumento de 15%
- Seu Novo Salário equivale: \033[1;37mR${aumento:.2f} 
---------------------------------------''')
