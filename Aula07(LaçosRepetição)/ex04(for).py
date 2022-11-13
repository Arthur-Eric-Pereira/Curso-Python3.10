# Desenvolva um programa que leia o nome, idade e sexo de 3 pessoas. No final do programa, mostre:
#        a média de idade do grupo,
#        qual é o nome do homem mais velho.
#        quantas mulheres têm menos de 20 anos.
#        quantos nomes começam com letra A.
#        quantos homens e mulheres no grupo.

for i in range(1, 6):
    print(f'=== {i}ª PESSOA ===')
    nome = str(input('>NOME: '))
    idade = int(input('>IDADE: '))
    sexo = str(input('>SEXO: '))
