'''
Usando list comprehension
[ <expressão> for <item> in <list> if <condicional> ]
'''
dobros = [i * 2 for i in range(1, 11)]
print(dobros)

'''
Exemplo sem usar list comprehension
'''
triplos = []
for i in range(1, 11):
    triplos.append(i * 3)
print(triplos)
