class HtmlToStringMixin:
    def __str__(self):
        '''
        Gerar um html ao invés de uma string normal.

        Pega o resultado da string gerada a partir da classe super()
        e substitui os parêntesis por tags html
        '''
        html = super().__str__() \
            .replace('(', '<strong>(') \
            .replace(')', ')</strong>')
        return f'<spam>{html}</spam>'


class Pessoa:
    def __init__(self, nome):
        self.nome = nome

    def __str__(self):
        return self.nome


class Animal:
    def __init__(self, nome, pet=True):
        self.nome = nome
        self.pet = pet

    def __str__(self):
        return self.nome + ' (pet)' if self.pet else ''


class PessoaHtml(HtmlToStringMixin, Pessoa):
    '''
    Tanto PessoaHtml quanto AnimalHtml são mixins.

    Existe uma ordenação nisso, prioridade
    pelo que vi a ordem de execução de, por exemplo:

    class Filha(Pa1, Pai2, Pai3):

    É -> Pai3, Pai2, Pai1

    Então tem que sempre começar com a classe que deve prevalecer

    No caso se fizer PessoaHtml(Pessoa, HtmlToStringMixin)
    Vai gerar apenas uma string comum de output
    '''
    pass


class AnimalHtml(HtmlToStringMixin, Animal):
    pass


if __name__ == '__main__':
    p1 = Pessoa('Maria Eduarda')
    print(p1)

    p2 = PessoaHtml('Roberto Carlos')
    print(p2)

    toto = AnimalHtml('Totó')
    print(toto)
