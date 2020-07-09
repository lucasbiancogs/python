'''
Tuplas não podem ser modificadas
Não se pode alterar os elementos
Adicionar, retirar
'''
tupla = tuple()
tupla = ()

# Para criar uma tupla de um elemento
# deve se inserir a vírgula
tupla = ('um',)

print(tupla[0])

'''
tupla[0] = 'dois'
Isso não pode ser feito
pois uma tupla não pode ser mudada
'''

cores = ('verde', 'amarelo', 'azul', 'branco')
a = cores[0]
print(a)

a = cores[-1]
print(a)

a = cores[1:]
print(a)

a = cores.index('amarelo')
print(a)

'''
Sempre lembrar que ele diferencia caracteres maiúsculos
a = cores.index('Azul')
print(a)
'''

a = len(cores)
print(a)
