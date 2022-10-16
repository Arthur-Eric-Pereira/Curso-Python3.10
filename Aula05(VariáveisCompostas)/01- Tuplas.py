# TUPLAS ()
# --> são imutáveis
# COMANDOS:
'''
sorted(var_tupla)               -> organiza os elementos na tupla (ordem alfabetica)
var_tupla.index("elemento")     -> retorna o indice do elemento informado
del(var_tupla)                  -> exclui a tupla
len(var_tupla)                  -> total de elementos na tupla
var_tupla.count("elemento")     -> quantas vezes o elemento aparece na tupla

'''
simbolos = ('$', '#', '+', '@', '[]')
print(len(simbolos))
print(simbolos)
print(simbolos[2])
print(simbolos[:3])
print(simbolos[0], simbolos[1:5], simbolos[-3])
print(simbolos[2:4])
print()
print(simbolos.index('@'))
print(simbolos.count('!'))
print(simbolos)
del(simbolos)
print(simbolos)