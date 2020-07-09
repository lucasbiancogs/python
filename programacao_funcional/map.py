lista_1 = [1, 2, 3]

dobro = map(lambda x: x * 2, lista_1)
print(list(dobro))

lista_2 = [
    {'nome': 'Jõao', 'idade': 31},
    {'nome': 'Maria', 'idade': 37},
    {'nome': 'José', 'idade': 26}
]

'''
A função map() faz uma ação para cada item na lista
e possui a sintaxe:
map(<function(item)>, <list>)
'''
so_nomes = list(map(lambda p: p['nome'], lista_2))
print(so_nomes)

so_idades = list(map(lambda i: i['idade'], lista_2))
print(so_idades)

frases = list(map(lambda fr: f'{fr["nome"]} tem {fr["idade"]} anos.', lista_2))

for frase in frases:
    print(frase)
