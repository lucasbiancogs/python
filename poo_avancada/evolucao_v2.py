class Humano:

    especie = 'Homo Sapiens'

    def __init__(self, nome):
        self.nome = nome

    def das_cavernas(self):
        self.especie = 'Homo Neanderthalensis'
        return self

    @staticmethod
    def especies():
        '''
        Para gerar um método estático é necessário utilizar o decorator
        @staticmethod
        ele é exatamente igual a um método definido direto no módulo
        '''
        adjetivos = ('Habilis', 'Erectus', 'Neanderthalensis', 'Sapiens')
        return ('Australopiteco',) + tuple(f'Homo {adj}' for adj in adjetivos)

    @classmethod
    def is_evoluido(cls):
        '''
        Também gerado com um decorator
        ele recebe uma classe e opera em cima dela
        '''
        return cls.especie == cls.especies()[-1]


class Neanderthal(Humano):
    especie = Humano.especies()[-2]


class HomoSapiens(Humano):
    especie = Humano.especies()[-1]


if __name__ == '__main__':
    '''
    Esse é o famoso polimorfismo
    Pode chamar de diversos jeitos

    Ele retorna o is_evoluido baseado na classe
    ou seja, chamando tanto a classe
    quanto um objeto gerado na classe
    '''
    jose = HomoSapiens('José')
    grokn = Neanderthal('Grokn')
    print(
        f'Evolução (a partir da classe): {", ".join(HomoSapiens.especies())}')
    print(f'Evolução (a partir da classe): {", ".join(jose.especies())}')
    print(f'Homo Sapiens evoluído? {HomoSapiens.is_evoluido()}')
    print(f'Grokn evoluído? {grokn.is_evoluido()}')
