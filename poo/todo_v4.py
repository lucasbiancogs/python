from datetime import datetime
'''
Esse import trás as datas formatadas
'''


class Projeto:
    '''
    Essa classe cria um projeto, onde nele haverão diversas tarefas
    e funcionalidades
    '''
    def __init__(self, nome):
        '''
        A inicialização ocorre com o nome
        e ao mesmo tempo inicializa uma lista de tarefas vazia
        '''
        self.nome = nome
        self.tarefas = []

    def __iter__(self):
        '''
        Essa função define o que pode ser iterado dentro da classe
        '''
        return self.tarefas.__iter__()

    def add(self, descricao, vencimento=None):
        '''
        O método add pega a descrição desejada para uma tarefa
        e dentro da lista de tarefas deste objeto
        cria um novo objeto Tarefa()
        '''
        self.tarefas.append(Tarefa(descricao, vencimento))

    def pendentes(self):
        '''
        Esse método retorna um list comprehension
        que basicamente retorna uma lista de tarefas não feitas
        caso elas tenham o tarefa.feito() = false
        '''
        return [tarefa for tarefa in self.tarefas if not tarefa.feito]

    def procurar(self, descricao):
        '''
        Nesse método ao encontrar dentro dessa lista de tarefas
        a que tenha descrição desejada
        ele retorna o objeto dela (o conteúdo da instância)
        '''
        # Possível IndexError
        return next((tarefa for tarefa in self.tarefas
                     if tarefa.descricao == descricao))

    def __str__(self):
        '''
        Retorna quantas tarefas ainda estão pendentes na lista
        '''
        return f'{self.nome} ({len(self.pendentes())} tarefa(s) pendente(s))'


class Tarefa:
    '''
    Essa classe cria uma Tarefa, que terá uma descrição
    um momento de criação e seu vencimento
    E uma propriedade booleana dizendo se foi feita ou não
    '''
    def __init__(self, descricao, vencimento=None):
        '''
        Essa inicialização ocorre com a descrição
        e cria por padrão as outras duas propriedades
        '''
        self.descricao = descricao
        self.feito = False
        self.criacao = datetime.now()
        self.vencimento = vencimento

    def concluir(self):
        '''
        Esse método somente altera o valor de self.feito
        '''
        self.feito = True

    def __str__(self):
        status = []
        if self.feito:
            status.append('(Concluída)')
        elif self.vencimento:
            if datetime.now() > self.vencimento:
                status.append('(Vencida)')
            else:
                dias = (self.vencimento - datetime.now()).days
                status.append(f'(Vence em {dias} dia(s))')
        return f'{self.descricao} ' + ' '.join(status)


def main():
    casa = Projeto('Tarefas de Casa')
    casa.add('Passar roupa')
    casa.add('Lavar prato')
    print(casa)

    casa.procurar('Lavar prato').concluir()
    for tarefa in casa:
        print(f'- {tarefa}')

    print(casa)

    compras = Projeto('Compras no Super')
    compras.add('Carne', datetime(2020, 4, 17, 1))
    compras.add('Refri', datetime(2020, 4, 14))
    compras.add('Banana')

    comprar_bananas = compras.procurar('Banana')
    comprar_bananas.concluir()
    print(compras)

    for compra in compras:
        print(f'- {compra}')


if __name__ == '__main__':
    main()
