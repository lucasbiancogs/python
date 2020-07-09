from pessoas.pessoa import Pessoa


class Vendedor(Pessoa):
    '''
    Classe Vendedor padrão.

    Nome -> str

    Idade -> int

    Salário -> int
    '''
    def __init__(self, nome=None, idade=None, salario=None):
        super().__init__(nome, idade)
        self.salario = salario
