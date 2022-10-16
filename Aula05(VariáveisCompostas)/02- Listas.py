# LISTAS []
# list()

# COMANDOS:
'''
var_lista.append("elemento")               -> adiciona o elemento na Lista
var_lista.insert(indice, "elemento")       -> insere o elemento no indice informado
var_lista.remove("elemento")               -> exclui o elemento da lista
var_lista.pop()                            -> exclui o ultimo elemento da Lista
    var_lista.pop(indice)                  -> exclui o elemento do indice informado
var_lista.sort()                           -> organiza os valores numericos em ordem crescente
    var_lista.sort(reverse=True)           -> contrário: em ordem decrescente
    '''

lista = []
lista.append(10)
lista.append(7)
lista.append(2)
lista.append(1)
lista.append(5)

print('tamanho da lista criada: ',len(lista))
print(lista)
print()

lista.sort()
print(lista)
lista.insert(3, 9)
print(lista)
lista.pop()
print(lista)
print()
print()
listaA = ['d', 'b', 'a', 'c']
listaB = ['g', 'h', 'f', 'e']
listaC = listaA + listaB
print(listaC)
lista1 = [2, 4, 7]
lista2 = lista1[:]  #cópia da lista1 !!
lista2[2] = 8
print('lista1: ', lista1)
print('lista2: ', lista2)