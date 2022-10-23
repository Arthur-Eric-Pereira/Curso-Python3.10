#   Escreva um programa que pergunte:
#        > a quantidade de Km percorridos por um carro alugado.
#        > a quantidade de dias pelos quais ele foi alugado.
#         - Calcule o preço a pagar, sabendo que o carro custa [R$60 por dia] e [R$0,15 por Km rodado]:

texto = 'ALUGUEL DE VEÍCULOS'
print(f'{texto:|^50}')

dias = float(input(">>Quantos dias você vai alugar o veículo?  "))
Km = float(input(">>Quantos Quilometros você vai viajar?  "))
preço = (60 * dias) + (0.15 * Km)
print('--'*25)
print(f'O valor do aluguel do veículo vai custar: R${preço:.2f}')