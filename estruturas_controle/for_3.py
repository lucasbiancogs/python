produto = {'nome': 'Caneta Chic', 'preco': 14.99,
           'importada': True, 'estoque': 793}

# Um jeito de pegar as chaves é só chamar a variável
for chave in produto:
    print(chave, end=(' '))
print()

# Para chamar os itens tem que chamar .values()
for valor in produto.values():
    print(valor, end=(' '))
print()

# Ou .items()
for chave, valor in produto.items():
    print(f'{chave} = {valor}')

# Outro jeito de pegar as chaves é com o .keys()
for chave in produto.keys():
    print(chave, end=(' '))
print()

'''
Os valores estão disponíveis mesmo depois de sair do for
e mesmo fora do bloco
Só o que limita é estar restrito a uma função ou a uma classe
'''
print(chave, valor)
