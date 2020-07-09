lista = ['Lia', 'Rui', 'Paulo', 'Dani', 'Nairana', 'Diogo']

# Vai de 1 até antes do 3
print(lista[1:3])

# Vai de 1 até antes do -1 (5), pq exclui o último
print(lista[1:-1])

# Começa a partir do 1
print(lista[1:])

# Acaba antes do -1 (3)
print(lista[:-1])

# Toda a lista
print(lista[:])

# Toda a lista de 2 em 2
print(lista[::2])

# Toda a lista de trás pra frente
print(lista[::-1])

del lista[2]

print(lista)

'''
Pelo que eu entendi ele ignora o que vem depois
do primeiro :
Ou seja, vai de 1 até antes de 2
Output: 'Rui'
print(lista[1:2:2])
'''
