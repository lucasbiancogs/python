from datetime import datetime


class Compra:
    def __init__(self, descricao, vendedor, valor=None, *data):
        self.descricao = descricao
        self.vendedor = vendedor
        self.data = datetime(*data) if data else datetime.now()
        self.valor = valor

    def __str__(self):
        return f'Compra: {self.descricao}\n\
Vendedor: {self.vendedor.nome}\n\
Data: {self.data}\n\
Valor: {self.valor}'
