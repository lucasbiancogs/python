class Pessoa:
    '''
    Classe Pessoa padrão a ser usada no pacote de pessoas.

    Nome -> str

    Idade -> int
    '''
    def __init__(self, nome=None, idade=None):
        self.nome = nome
        self.idade = idade

    def __str__(self):
        return f'Nome: {self.nome}, Idade: {self.idade}'

    def is_adulto(self):
        return (self.idade or 0) >= 18
