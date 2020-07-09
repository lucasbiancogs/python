class Humano:

    especie = 'Homo Sapiens'

    def __init__(self, nome):
        self.nome = nome
        self._idade = None

    @property
    def inteligente(self):
        '''
        Uma classe abstrata, é uma classe que precisa de uma maior abstração
        para realmente ser definida.
        No caso é muito complexo dizer se alguem é inteligente ou não
        só dizendo que é um humano...
        Então isso é uma propriedade abstrata.

        Por isso, se pelo menos um dos métodos, no caso esse,
        não está implementado, devido a sua complexidade
        esse fato torna a classe abstrata

        Vale ressaltar que a classe abstrata deve ser posteriormente resolvida
        no caso ainda não da para saber se Humano é inteligente
        mas um Homo Sapiens daria
        '''
        raise NotImplementedError('Propriedade não implementada')

    @property
    def idade(self):
        return self._idade

    @idade.setter
    def idade(self, idade):
        if idade < 0:
            raise ValueError('Idade deve ser um valor positivo!')
        self._idade = idade

    def das_cavernas(self):
        self.especie = 'Homo Neanderthalensis'
        return self

    @staticmethod
    def especies():
        adjetivos = ('Habilis', 'Erectus', 'Neanderthalensis', 'Sapiens')
        return ('Australopiteco',) + tuple(f'Homo {adj}' for adj in adjetivos)

    @classmethod
    def is_evoluido(cls):
        return cls.especie == cls.especies()[-1]


class Neanderthal(Humano):
    especie = Humano.especies()[-2]

    @property
    def inteligente(self):
        return False


class HomoSapiens(Humano):
    especie = Humano.especies()[-1]

    @property
    def inteligente(self):
        return True


if __name__ == '__main__':
    anonimo = Humano('John Doe')

    try:
        print(anonimo.inteligente)
    except NotImplementedError:
        print('propriedade abstrada')

    jose = HomoSapiens('José')
    print('{} da classe {} é inteligente? {}'
          .format(jose.nome, jose.__class__.__name__, jose.inteligente))

    grokn = Neanderthal('Grokn')
    print('{} da classe {} é inteligente? {}'
          .format(grokn.nome, grokn.__class__.__name__, grokn.inteligente))
