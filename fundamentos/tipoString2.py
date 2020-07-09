nome = 'Nairana Pavinato'

print(nome[0])
print(nome[6])

'''
O sinal negativo faz com que ele começe do fim
Lembrando que não existe -0
'''
print(nome[-2])

'''
O índice: faz com que ele comece a ler a partir do índice
até o final da String
'''
print(nome[4:])

'''
Assim como se o índice for negativo
Vai do índice contado do fim
Até o fim da String
'''
print(nome[-5:])

'''
Se for :índice
Vai desde o início da String até o valor do índice
excluíndo o caracter do índice
'''
print(nome[:3])

'''
Neste caso ele começa no índice 2 e termina no índice 4
'''
print(nome[2:5])

numeros = '1234567890'

# Os ::n pegam os valores da String a cada n índices
print(numeros[::2])

# i::n faz a mesma coisa mas começa do índice i
print(numeros[1::2])

# ::-n faz a mesma coisa mas invertido
print(numeros[::-1])

# Invertendo o nome da Nairana
print(nome[::-1])
