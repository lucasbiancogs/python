lista = [1, 5, 'Rebeca', 'Guilherme', 3.14156]

a = lista.index('Guilherme')
print(a)

'''
Em python pedir o índice de algo que não está na lista
Gera um erro
lista.index(42)
'''
a = lista[2]
print(a)

a = 1 in lista
print(a)

a = 'Pedro' not in lista
print(a)

a = lista[-1]
print(a)
