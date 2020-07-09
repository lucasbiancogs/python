from pessoas.pessoa import Pessoa


class Cliente(Pessoa):
    '''
    Classe Cliente padrão.

    Nome -> str

    Idade -> int
    '''
    def __init__(self, nome, idade):
        super().__init__(nome, idade)
        self.compras = []

    def registrar_compra(self, compra):
        self.compras.append(compra)
        return self.compras

    def get_data_ultima_compra(self):
        '''
        Funções lambda serão vistas mais a frente
        '''
        return None if not self.compras else \
            sorted(self.compras, key=lambda c: c.data)[-1].data

    def __iter__(self):
        return self.compras.__iter__()

    def total_compras(self):
        self.soma = 0
        for compra in self.compras:
            self.soma += compra.valor
        return self.soma

    def __iadd__(self, compra):
        self.registrar_compra(compra)
        return self
