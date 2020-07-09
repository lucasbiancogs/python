'''
Agora gerando dicionários com o list_comprehension
O que muda na sintaxe é que necessita de chave: valor
e é definido entre chaves
'''
dicionario = {i: i * 2 for i in range(10) if i % 2 == 0}
print(dicionario)

for numero, dobro in dicionario.items():
    print(f'{numero} x 2 = {dobro}')
