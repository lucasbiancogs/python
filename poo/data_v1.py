class Data:
    '''
    Nomes de classe são dados com a primeira letra maiúscula
    e cada nova palavra também começa com a letra maiúscula
    Data de nascimento -> class DataDeNascimento
    '''
    def to_str(self):
        '''
        Todo método (função) criado dentro de uma classe necessita do self
        que seria o próprio objeto sendo chamado
        ele exige que você seja explicito ao dizer que está usando esse objeto
        '''
        return f'{self.dia}/{self.mes}/{self.ano}'

    def __str__(self):
        '''
        Porém não é necessário criar a função acima
        pois o Python possui um "método mágico" pra isso
        que transforma o objeto em uma forma String definida
        sem chamar um método
        '''
        return f'{self.dia}/{self.mes}/{self.ano}'


'''
Aqui criou-se um objeto chamado de d1
Pelo fato de Python ser uma linguagem dinâmica
É possível definir atributos a um objeto
mesmo que eles não tenham sido definidos previamente
diferentemente de Java por exemplo
'''
d1 = Data()
d1.dia = 5
d1.mes = 12
d1.ano = 2019

print(f'{d1.dia}/{d1.mes}/{d1.ano}')
print(d1.to_str())

'''
Se colocasse os atributos de forma errada, daria um erro
Por exemplo d2.diia = 11
E esse é o problema da atribuição dinâmica
'''
d2 = Data()
d2.dia = 7
d2.mes = 11
d2.ano = 2020
print(d2.to_str())
print(d2)
