from funcao_primeira_classe import dobro, quadrado


def processar(titulo, lista, funcao):
    print(f'Processando: {titulo}')
    for i in lista:
        print(f'{i} => {funcao(i)}')


if __name__ == '__main__':
    '''
    Funções de alta ordem são funções que recebem outras funções
    '''
    processar('Dobros de 1 a 10', range(1, 11), dobro)
    processar('Quadrados de 1 a 10', range(1, 11), quadrado)
