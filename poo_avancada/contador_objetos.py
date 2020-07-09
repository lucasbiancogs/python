class ClasseSimples:
    contador = 0

    def __init__(self):
        self.contar()

    @classmethod
    def contar(cls):
        cls.contador += 1
        return cls.contador


if __name__ == '__main__':
    lista = [ClasseSimples(), ClasseSimples()]
    '''
    O desafio é apresentar quantas instâncias foram criadas
    '''
    print(ClasseSimples.contador)
    print(ClasseSimples.contar())
