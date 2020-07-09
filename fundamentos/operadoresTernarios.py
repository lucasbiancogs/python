esta_chovendo = True
'''
Se esta_chovendo for True, ele irá pegar a sentença mais próxima
Se esta_chovendo for False ele irá pegar a mais distante
'''
print('Hoje estou com as roupas ' + ('secas.', 'molhadas.')[esta_chovendo])

# Notar a proximidade do python com o inglês
print('Hoje estou com as roupas ' + (
    'molhadas.' if esta_chovendo else 'secas.'))
