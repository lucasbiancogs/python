from string import Template

nome, idade, peso = 'Nairana', 19, 52.23

# Versões mais antiga
print('Nome: %s \nIdade: %d \nPeso: %.1f\n' % (nome, idade, peso))
print('Nome: {0} \nIdade: {1} \nPeso: {2}\n'.format(nome, idade, peso))

# Versão mais atual e mais simples -> # python >= 3.6
print(f'Nome: {nome} \nIdade: {idade} \nPeso: {peso}\n')

s = Template('Nome: $nome \nIdade: $idade \nPeso: $peso\n')
print(s.substitute(nome=nome, idade=idade))
