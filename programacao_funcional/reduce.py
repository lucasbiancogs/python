from functools import reduce


pessoas = [
    {'nome': 'Pedro', 'idade': 11},
    {'nome': 'Mariana', 'idade': 18},
    {'nome': 'Arthur', 'idade': 26},
    {'nome': 'Rebeca', 'idade': 6},
    {'nome': 'Tiago', 'idade': 19},
    {'nome': 'Gabriela', 'idade': 17}
]

'''
reduce() é um acumulador
ele pode gerar um único valor, novas listas, dicionários
ela recebe dois parâmetros
o acumulador que pode ser modificado
e o parâmetro atual, que pode ser um número, outra lista etc.
sua sintaxe:
reduce(<function(acumulador, itens)>, <list>, <valor inicial>)
'''

soma_idades = reduce(lambda idades, p: idades + p['idade'], pessoas, 0)
print(soma_idades)

so_idades = map(lambda p: p['idade'], pessoas)
menores = filter(lambda idade: idade < 18, so_idades)
soma_idades_menores = reduce(lambda idades, idade: idades + idade, menores, 0)
print(soma_idades_menores)
