class Humano:
    '''
    Quando você simplesmente coloca uma variável dentro de classe
    ela se torna um membro de classe, ou seja,
    esse membro é compartilhado por todas as instâncias
    geradas por Humano
    '''
    especie = 'Homo Sapiens'

    def __init__(self, nome):
        self.nome = nome

    def das_cavernas(self):
        '''
        No caso aqui há um conflito de nomes
        se existir um novo atributo para a instância
        por exemplo, chamando essa função
        então quem ganha?

        Ganha a instância.
        Basicamente um atributo de instância
        é mais forte que um atributo genérico
        '''
        self.especie = 'Homo Neanderthalensis'
        '''
        É interessante retornar self, pois ele retornando o próprio objeto
        em uma chamada pode criar todo o contexto, como é feito de exemplo
        no terceiro objeto
        '''
        return self


if __name__ == '__main__':
    jose = Humano('José')
    grokn = Humano('Grokn')
    grokn.das_cavernas()

    jabirosca = Humano('Jabirosca').das_cavernas()

    print(f'Humano.especie: {Humano.especie}')
    print(f'Humano.especie: {jose.especie}')
    print(f'Humano.especie: {grokn.especie}')
    print(f'Humano.especie: {jabirosca.especie}')
