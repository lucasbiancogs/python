palavra = 'paralelepípedo'

for letra in palavra:
    '''
    Se colocar o end no final ele coloca a vírgula
    por padrão ele coloca \n
    '''
    print(letra, end='.')
print('\n')

aprovados = ['Rafaela', 'Pedro', 'Maria', 'Renato']

for nome in aprovados:
    print(nome, end=', ')
print('\n')

'''
O enumerate() ajuda pois pega o índice das coisas
'''
for posicao, nome in enumerate(aprovados):
    print(f'{posicao + 1}) {nome}')
print('')


dias_semana = ('Domingo', 'Segunda', 'Terça', 'Quarta',
               'Quinta', 'Sexta', 'Sábado')

for dia in dias_semana:
    print(f'Hoje é {dia}.')
print('')

for letra in set('Muito legal'):
    print(letra, end=('.'))
print('')

for numero in {1, 2, 3, 4, 5}:
    print(numero, end=('.'))
