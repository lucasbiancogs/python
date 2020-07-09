'''
Usando list comprehension
[ <expressão> for <item> in <list> if <condicional> ]
'''
dobro_dos_pares = [i * 2 for i in range(1, 11) if i % 2 == 0]
print(dobro_dos_pares)

'''
Exemplo sem usar list comprehension
'''
triplo_dos_pares = []
for i in range(1, 11):
    if i % 2 == 0:
        triplo_dos_pares.append(i * 3)
print(triplo_dos_pares)
