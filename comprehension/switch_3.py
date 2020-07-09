def get_tipo_dia(dia):
    dias = {
        (1, 7): 'Fim de semana',
        tuple(range(2, 7)): 'Dia de semana'
    }
    '''
    Utilizando como retorno um generator
    O next() pode possuir um parâmetro de resposta em caso de erro
    Além disso, é muito importante esse tipo de for para correr um dicionário
    for <keys>, <values> in <dict>.items()
    '''
    return next((tipo for numero, tipo in dias.items() if dia in numero),
                'Dia inválido')


if __name__ == '__main__':
    dia = input('Informe o dia escolhido: ')
    print(f'Este é um {get_tipo_dia(int(dia)).lower()}.')
