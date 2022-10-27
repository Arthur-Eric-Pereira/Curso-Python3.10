# Crie uma tabuada utilizando o laço de repetição 'for' !

titulo = 'TABUADA'
print(f'{titulo:=^30}')
num = int(input('Digite um Nº e veja sua TaBuAdA: '))
for x in range(0,11):
    print(f'> {num} X {x} = {num * x}')
print('Fim........')
