# Crie um programa que leia a velocidade de um carro. Se ele ultrapassar 80Km/h,
#        mostre uma mensagem dizendo que ele foi multado.
#        A multa vai custar R$7,00 por cada Km acima do limite.

from time import sleep
from random import randint
vel_carro = randint(60, 200)
multa = (vel_carro - 80) * 7
msg = 'RADAR DE VELOCIDADE'
print()
print(f'{msg:=^46}')
sleep(3)
print(f'VEÍCULO ESTÁ PASSANDO PELO RADAR DE VELOCIDADE')
print(f'...carregando')
print()
sleep(3)
if vel_carro > 80:
    print(f'ACIMA DA VELOCIDADE PERMITIDA!')
    print(f'> {vel_carro}Km/h  -> \033[41mMULTADO!\033[m ')
    print(f'> VALOR: \033[31mR${multa}\033[m')
else:
    print(f'VELOCIDADE DENTRO DO PERMITIDO!')
    print(f'> {vel_carro}Km/h  -> \033[42mTUDO OK!\033[m ')
    print(f'> VALOR: \033[32mR$ 00\033[m' )
