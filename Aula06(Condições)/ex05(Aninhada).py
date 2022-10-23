#   Crie um programa que leia 3 notas de um aluno e calcule sua média, mostrando uma mensagem no final,
#   de acordo com a média atingida:
#     - Média abaixo de 5.0: REPROVADO
#     - Média entre 5.0 e 6.9: RECUPERAÇÃO
#     - Média 7.0 ou superior: APROVADO

nota1 = float(input('NOTA 1:  '))
nota2 = float(input('NOTA 2:  '))
nota3 = float(input('NOTA 3:  '))
print('-'*20)
media = (nota1 + nota2 + nota3) / 3
print(f'MÉDIA: {media:.2f}')
print('-'*20)
if media < 5:
    print('[ REPROVADO ]')
elif media >= 5 and media <= 6.9:
    print('[ RECUPERAÇÃO ]')
elif media >= 7:
    print('[ APROVADO ]')
