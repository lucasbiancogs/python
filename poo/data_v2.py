class Data:
    def __init__(self, dia=1, mes=1, ano=1970):
        '''
        Esta função é construtora
        então toda vez que for iniciado o objeto ela será chamada
        Pode haver para ela entradas,
        que definirão então os parâmetros de chamada de um objeto

        Diferentemente de outras linguagens como Java
        o Python não permite mais de um construtor
        porém para corrigir isso pode se inserir valores padrão
        Assim, se nada for chamado ele insere por si só
        '''
        self.dia = dia
        self.mes = mes
        self.ano = ano

    def __str__(self):
        return f'{self.dia}/{self.mes}/{self.ano}'


'''
Este método Data() é um método especial chamado de construtor
ele é quem constrói um objeto dada uma certa classe
'''
d1 = Data(5, 12, 2019)
print(d1)

d2 = Data(7, 11, 2020)
print(d2)
d2.dia = 12
print(d2)

d3 = Data(ano=2022)
d3.dia = 3
print(d3)
