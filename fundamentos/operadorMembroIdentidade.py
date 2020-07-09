# Operador de membro
lista = [1, 2, 3, 'Nairana', 'Carla']
print(2 in lista)
print('Nairana' not in lista)
print('')

# Operador de identidade
x = 3
y = x
z = 3
print(x is y)
print(y is z)
print(x is not z)

lista_a = [1, 2, 3]
lista_b = lista_a
lista_c = [1, 2, 3]


'''
Embora as listas sejam iguais, elas não apontam para o mesmo local
e por isso são consideradas diferentes
'''
print(lista_a is lista_b)
print(lista_b is lista_c)
print(lista_a is not lista_c)
