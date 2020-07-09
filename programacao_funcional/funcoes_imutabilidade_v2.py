from functools import reduce
from operator import add

'''
Outra maneira de garantir a imutabilidade é utilizar valores
por definição imutáveis, como tuplas
'''

valores = (30, 10, 25, 70, 100, 94)

print(sorted(valores))
print(valores)

'''
A tupla não aceita esse tipo de função justamente por mutarem o dado
'''
# valores.sort()
# print(valores)

print(min(valores))
print(max(valores))
print(sum(valores))
print(reduce(add, valores))
print(reversed(valores))
print(tuple(reversed(valores)))

'''
funções que mutam os valores

valores.reverse()
print(valores)
'''
