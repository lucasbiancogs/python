class ClasseSimples:
    contador = 0

    def __init__(self):
        self.__class__.contador += 1


if __name__ == '__main__':
    lista = [ClasseSimples(), ClasseSimples()]
    '''
    O desafio é apresentar quantas instâncias foram criadas
    '''
    print(ClasseSimples.contador)
