def cores_arco_iris():
    '''
    yield é a produção dos valores, como um retorno parcial
    Esses tipos de função tem uma certa "memória"
    '''
    yield 'vermelho'
    yield 'laranja'
    yield 'amarelo'
    yield 'verde'
    yield 'azul'
    yield 'indigo'
    yield 'violeta'


if __name__ == '__main__':
    generator = cores_arco_iris()
    print(type(generator))
    while True:
        print(next(generator))
