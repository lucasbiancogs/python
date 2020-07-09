'''
Agora trabalhando com generators
eles possuem a mesma sintaxe porém generator usa parenteses

O generator não gera uma lista e sim um número
Ele gera os valores sob demanda
Então para acessar é necessário usar o comando next()
Por isso também usa menos memória que o list comprehension
'''
generator = (i ** 2 for i in range(10) if i % 2 == 0)
# Saída 0
print(next(generator))
# Saída 4
print(next(generator))
# Saída 16
print(next(generator))
# Saída 36
print(next(generator))
# Saída 64
print(next(generator))
# Erro
# print(next(generator))
