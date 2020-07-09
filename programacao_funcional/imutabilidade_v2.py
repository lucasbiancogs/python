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
indices_31_dias = filter(lambda mes: mdays[mes] == 31, range(1, 13))
meses_31_dias = map(lambda i: month_name[i], indices_31_dias)
frase_meses = reduce(lambda fr, n_m: f'{fr}\n- {n_m}', meses_31_dias,
                     'Os meses com 31 dias são:')

print(frase_meses)
