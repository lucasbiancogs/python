def dia_util(dia):
    dia_util = [2, 3, 4, 5, 6]
    final_de_semana = [1, 7]
    if dia in dia_util:
        validacao = 'Dia útil.'
    elif dia in final_de_semana:
        validacao = 'Final de semana'
    else:
        validacao = 'Dia inválido'
    return validacao


if __name__ == '__main__':
    for dia in range(1, 9):
        print(f'{dia}: {dia_util(dia)}')


def get_tipo_dia(dia):
    dias = {
        1: 'Final de semana',
        2: 'Dia de semana',
        3: 'Dia de semana',
        4: 'Dia de semana',
        5: 'Dia de semana',
        6: 'Dia de semana',
        7: 'Final de semana',
    }
    return dias.get(dia, 'Dia inválido')


if __name__ == '__main__':
    for dia in range(1, 9):
        print(f'{dia}: {get_tipo_dia(dia)}')
