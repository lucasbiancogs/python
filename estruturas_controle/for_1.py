'''
O for vai varrer todos i dentro da variável range()
é como dizer que 1 <= range < 11
'''
for i in range(1, 11):
    print(f'i = {i}')

# Se não colocar nada ele assume que começa em 0
for j in range(10):
    print(f'i = {j}')

print('\nA tabuada:')
for x in range(1, 11):
    for y in range(1, 11):
        # A operação dentro de chaves é executada
        print(f'{x} * {y} = {x * y}')
