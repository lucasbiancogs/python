'''
É chamado como um dicionário mas funciona como uma lista
No entanto
Conjuntos não são indexados
não garante a ordem de seção
não aceita repetição
'''
a = {1, 2, 3}
print(a)
# a[0] -> não existe índice

# O set coloca cada item da string separadamente dentro do conjunto
a = set('cod3r')
print(a)

# Ele reconhece o tipo inserido
print('3' in a, 3 in a)

# Não aceita repetições
print({1, 2, 3} == {1, 2, 3, 3, 2, 1, 1, 1})

# ###### Operações ###### #
c1 = {1, 2, 3}
c2 = {2, 3, 4}

b = c1.union(c2)
print(b)

b = c1.intersection(c2)
print(b)

c1.update(c2)
print(c1)

# c2 é subconjunto de c1?
print(c2 <= c1)

# c1 é superconjunto de c2?
print(c1 >= c2)

# A diferença existe, mas a soma não
print({1, 2, 3} - {2})

b = c1 - c2
print(b)

print(c1)
c1 -= {2}
print(c1)
