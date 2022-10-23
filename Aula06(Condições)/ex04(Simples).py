# Desenvolva um programa que pergunte a distância de uma viagem em Km.
#        Calcule o preço da passagem cobrando:
#         - R$0,50 por Km para viagens de até 200Km
#         - R$0,45 para viagens mais longas.

distancia = float(input('''QUAL A DISTÂNCIA DE SUA VIAGEM? 
> '''))
print(f'{distancia}Km DE DISTÂNCIA! O VALOR DE SUA PASSAGEM SERÁ:')
if distancia <= 200:
    print(f'> VALOR: R${0.50 * distancia}')
else:
    print(f'> VALOR: R${0.45 * distancia}')
