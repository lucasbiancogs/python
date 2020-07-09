'''
Um dicionário em python é diferente de um objeto em JavaScript
Serve para guardar valores com diferentes tipos de índice.
'''

v = 'idade'
pessoa = {'nome': 'Nairana', v: 38, 'cursos': ['Inglês', 'Python 3']}

a = pessoa['nome']
print(a)

a = pessoa['idade']
print(a)

a = pessoa['cursos']
print(a)

# O índice do array vai fora pq
#  a primeira ação é transformar a variável em um array
a = pessoa['cursos'][1]
print(a)

# print(dir(dict))

# .keys() informa quais foram as chaves utilizadas
print(pessoa.keys())

# .values() informa quais são os valores
print(pessoa.values())

'''
.get() evita erros de compilação caso a chave não exista
como seria o caso de a = pessoa['tags']
Também tem a função de retornar um valor padrão caso não encontre a chave
'''
a = pessoa.get('idade')
print(a)

variavel = 'nome'

a = pessoa.get(variavel, 'Valor não encontrado')
print(a)

variavel = 'teste'

a = pessoa.get(variavel, 'Valor não encontrado')
print(a)
