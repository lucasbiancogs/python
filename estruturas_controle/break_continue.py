for x in range(1, 11):
    if x % 2 == 0:
        '''
        Por se tratar de um comando de laço
        ele não irá parar o if e sim o for
        embora esteja dentro do bloco if

        O continue para aquela iteração
        mas continua no laço
        '''
        continue
    print(x, end=(' '))
print()

for x in range(1, 11):
    if x == 5:
        '''
        Diferente do continue o break para a iteração
        e sai do laço
        '''
        break
    print(x, end=(' '))
print('\nFim')
