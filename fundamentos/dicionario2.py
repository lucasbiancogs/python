pessoa = {'nome': 'Prof. Alberto', 'idade': 43, 'cursos': ['React', 'Python']}

print(pessoa)

pessoa['idade'] = 44
print(pessoa)

# o .append adiciona um valor no array
pessoa['cursos'].append('Angular')
print(pessoa)

# .pop() retira um valor e "externa" ele
a = pessoa.pop('idade')
print(pessoa)
print(a)

# .update adiciona valores ao final do dicionário
pessoa.update({'idade': 48, 'sexo': 'M'})
print(pessoa)

del pessoa['cursos']
print(pessoa)

pessoa.clear()
print(pessoa)
