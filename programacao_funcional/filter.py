pessoas = [
    {'nome': 'Pedro', 'idade': 11},
    {'nome': 'Mariana', 'idade': 18},
    {'nome': 'Arthur', 'idade': 26},
    {'nome': 'Rebeca', 'idade': 6},
    {'nome': 'Tiago', 'idade': 19},
    {'nome': 'Gabriela', 'idade': 17}
]

'''
Filter é uma função que recebe como parâmetro uma função
normalmente lambda
e que deve receber como retorno dessa função True ou False
sua sintaxe:
filter(<funciton(item)>, <list>)
no caso podem ser dicionários, listas e tuplas
'''
menores = filter(lambda p: p['idade'] < 18, pessoas)
print(list(menores))

nomes_grandes = filter(lambda p: len(p['nome']) > 6, pessoas)
print(list(nomes_grandes))
