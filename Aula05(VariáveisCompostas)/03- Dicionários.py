# DICIONARIOS {}
# dict()

# COMANDOS:
'''
del(var_dicionario)["elemento"]             -> exclui o elemento do dicionario
var_dicionario.items()                      -> mostra todos os items do dicionario
var_dicionario.keys()                       -> mostra todas as chaves do dicionario
var_dicionario.values()                     -> mostra todos os valores das chaves do dicionario
var_dicionario.update(outro_dicionario)     -> concatena 'outro_dicionario' em var_dicionario
var_dicionario.copy()                       -> copia os valores de var_dicionario
'''

dados = dict()
dados = {'nome' : 'Arthur', 'idade' : 21, 'sexo' : 'M', 'altura' : 1.80}
print(dados)
print(dados['nome'])
print(dados['idade'])
print(dados['sexo'])
print(dados['altura'])

print()
print()

filmes = {'titulo':'Os Vingadores', 'ano':2012, 'diretor':'Joss Whedon'}
for k, v in filmes.items():
    print(f'O {k} é {v}')
