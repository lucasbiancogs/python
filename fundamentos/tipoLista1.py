'''
Listas em python são mutáveis
E também recebem vários tipos
Porém vale ressaltar que uma lista com vários tipos
não é uma boa prática
'''
lista = [1, 2, 'Lucas']
print(lista)

a = len(lista)
print(a)

# .append adiciona o valor em parêntesis ao final da lista
lista.append(3)
print(lista)

# Remove um ítem dado o índice indicado
lista.pop(0)
print(lista)

# Reverte a lista
lista.reverse()
print(lista)

# Remove o ítem indicado
lista.remove('Lucas')
print(lista)

lista.append([1, 3, 4])
print(lista)
