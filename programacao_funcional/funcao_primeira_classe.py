def dobro(x):
    return x * 2


def quadrado(x):
    return x ** 2


if __name__ == '__main__':
    '''
    O conceito de função de primeira classe
    significa que as funções podem ser armazenadas como dados
    aqui no caso vamos armazenar as funções dobro e quadrado
    em uma lista para serem retornadas alternadamente

    O * 5 indica que a lista será repetida 5 vezes

    A função zip une os dois valores e os atrela
    podendo ser uma lista, um dicionário ou tupla
    aqui no caso o for já reconhece como um dicionário
    lembre... ducktype
    '''
    d = dobro
    print(d(3))

    q = quadrado
    print(q(3))

    funcs = [dobro, quadrado] * 5
    for func, numero in zip(funcs, range(1, 11)):
        print(f'O {func.__name__} de {numero} é {func(numero)}')
