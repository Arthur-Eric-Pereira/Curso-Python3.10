# Desenvolva um programa que leia 3 notas de um aluno, calcule e mostre a sua média.
aluno = input('== == == == NOME DO ALUNO: ')
print(f'>>> ALUNO: {aluno}')
print('-'*40)
nota1 = float(input("Nota 01: "))
nota2 = float(input("Nota 02: "))
nota3 = float(input("Nota 03: "))
print(f'''
        MÉDIA DE NOTAS:
>>> Aluno: {aluno}
>>> N1 [{nota1}]
>>> N2 [{nota2}]
>>> N3 [{nota3}]
>>> Média: {(nota1 + nota2 + nota3) / 3:.2f}''')
