from generator_v1 import cores_arco_iris

if __name__ == '__main__':
    '''
    Internamente o for entende que se trata de um generator
    e através da lazy evaluation verifica se ainxa exisstem retornos
    então sequer da problema usar o for com generator
    '''
    generator = cores_arco_iris()
    for cor in generator:
        print(cor)
    print('Fim!')
