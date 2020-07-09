from calendar import mdays, month_name
from locale import setlocale, LC_ALL

setlocale(LC_ALL, 'pt_BR')

'''
A abordagem imperativa é mandar o computador fazer
A declarativa você declara o que quer
'''
print('Meses com 31 dias.')
for mes in range(1, 13):
    if mdays[mes] == 31:
        print(f'- {month_name[mes]}')
