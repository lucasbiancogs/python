from locale import setlocale, LC_ALL
from calendar import mdays, month_name
from functools import reduce

'''
Primeira coisa é selecionar a localização para que o month_name
seja realizado em português.
'''
setlocale(LC_ALL, 'pt_BR')

'''
O próximo passo é listar todos os meses que possuem 31 dias.
'''
dicionario_de_meses = []
for i in range(1, 13):
    dicionario_de_meses.append(
        {'mes': month_name[i], 'dias': mdays[i]})

meses_31_dias = filter(lambda d_d_m: d_d_m['dias'] == 31, dicionario_de_meses)
nomes_meses = map(lambda m_31_d: m_31_d['mes'], meses_31_dias)
frase_meses = reduce(lambda frase, n_m: frase + f'\n- {n_m}', nomes_meses, '')
print(f'Os meses que possuem 31 dias são: {frase_meses}')
