# WHILE (ENQUANTO ... )
#      -> usar quando eu não souber a quantidade exata ou o final !
'''
while (True):
    executa o bloco de comando....
print('Fim')

'''
r = 'S'
while r == 'S':
    n = int(input('DIGITE UM NÚMERO: '))
    r = str(input('>> Continuar? [S/N]:  ')).upper()
print('Fim_____')

print()

c = 1
while c < 10:
    print(c, end='_')
    c += 1
print('\n -FIM-')

print()

n = 1
while n != 0:
    n = int(input('Digite um valor: '))
print('ACABOU')
