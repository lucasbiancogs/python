class Humano:

    especie = 'Homo Sapiens'

    def __init__(self, nome):
        '''
        Por convenção _idade é um atributo exclusivo da classe
        private
        '''
        self.nome = nome
        self._idade = None

    def get_idade(self):
        '''
        Um método lê
        '''
        return self._idade

    def set_idade(self, idade):
        '''
        O outro método edita
        Isso é bom para por exemplo validar um valor antes de inserir no objeto
        '''
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


class HomoSapiens(Humano):
    especie = Humano.especies()[-1]


if __name__ == '__main__':
    jose = HomoSapiens('José')
    jose.set_idade(48)
    '''
    # jose._idade também daria certo mas o certo é chamá-lo pelo método
    já que _idade se trata de uma instância privada
    '''
    print(f'Nome: {jose.nome} Idade: {jose.get_idade()}')
