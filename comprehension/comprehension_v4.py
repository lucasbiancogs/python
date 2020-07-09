'''
É sensato usar o generator pois ele gera sob demanda
Ao inves de usar o next()
O próprio for entende que se trata de um generator
E por isso faz mais sentido usar for
'''
generator = (i ** 2 for i in range(10) if i % 2 == 0)

for numero in generator:
    print(numero)
