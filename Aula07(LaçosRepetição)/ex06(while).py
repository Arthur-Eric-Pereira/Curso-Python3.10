# Crie um programa que leia dois valores e mostre um menu na tela:


fim = True
opcao = 0
n1 = float(input('Informe um número: '))
n2 = float(input('Informe outro número: '))
while opcao != 7:
    print('='*25)
    print('''
    [1]- Somar
    [2]- Subtrair
    [3]- Multiplicar
    [4]- Dividir
    [5]- Maior ou Menor
    [6]- Outros Valores
    [7]- ENCERRAR PROGRAMA...''')
    opcao = int(input('>> '))
    print('='*25)

    if opcao == 1:
        print(f'{n1} + {n2} = {n1 + n2}')
    elif opcao == 2:
        print(f'{n1} - {n2} = {n1 - n2}')
    elif opcao == 3:
        print(f'{n1} x {n2} = {n1 * n2}')
    elif opcao == 4:
        print(f'{n1} / {n2} = {n1 / n2}')
    elif opcao == 5:
        if n1 == n2:
            print(f'OS DOIS NÚMEROS SÃO IGUAIS!')
        elif n1 > n2:
            print(f'{n1} é o Valor Maior!')
        else:
            print(f'{n2} é o valor Maior!')
    elif opcao == 6:
        n1 = float(input('Valor 1nº: '))
        n2 = float(input('Valor 2nº: '))
    elif opcao == 7:
        print(f'Encerrando...')
        fim = False
    else:
        print('\033[33m[OPERAÇÃO INVÁLIDA]\033[m')
