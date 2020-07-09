frase = 'Python é uma linguagem excelente'

a = 'py' not in frase
print(a)

a = 'ing' in frase
print(a)

# frase.lentgh
a = len(frase)
print(a)

a = 'py' in frase.lower()
print(a)

# Separa a string em uma lista pelos espaços
a = frase.split()
print(a)

# Separa a string em uma lista pelo caractér
a = frase.split('a')
print(a)

a = frase.split('ma')
print(a)

'''
Se for usar a função split ou qualquer função que tem como imput uma String
dentro de uma função print é necessário que a chamada possua aspas
diferentes da chamada da string principal, por exemplo
print(f'Oi Nairana, sabia que {frase.split("a")}')
'''
