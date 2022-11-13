# INTERROMPENDO LAÇOS DE REPETIÇÃO EM WHILE

#       COMANDO:  break


#_____________________________Gambiarra:
n = s = 0
while n != 999:
    n = int(input('Digite um nº: '))
    s += n
s -= 999
print('A soma vale {}'.format(s))


#_____________________________FORMA CORRETA:
n = s = 0
while True:
    n = int(input('Digite um nº: '))
    if n == 999:
        break
    s += n
print('A soma vale {}'.format(s))